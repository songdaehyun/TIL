import re
import serial
import threading
from qt_form import Ui_Form
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from PySide6.QtSerialPort import QSerialPortInfo
from PySide6.QtCore import QObject, Signal, QTimer, QDateTime


class SerialMonitor(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super(SerialMonitor, self).__init__(parent)
        self.setupUi(self)
        self.timer.timeout.connect(self.update_lcd_datetime)
        self.timer.start(1000)

        port_list = QSerialPortInfo().availablePorts()
        for i, port_info in enumerate(port_list):
            self.comboBox.insertItem(i, port_info.portName())

        baudrate_list = ['9600', '115200', '128000']
        for i, baudrate_info in enumerate(baudrate_list):
            self.comboBox_2.insertItem(i, baudrate_info)

        self.dev = None
        self.receiver = Receiver(self)
        self.receiver.data_received.connect(self.update_display)

    #프로그램 종료시 다시한번 확인
    def closeEvent(self, event):
        re = QMessageBox.question(self, "종료 확인", "종료 하시겠습니까?", QMessageBox.Yes | QMessageBox.No)

        if re == QMessageBox.Yes:
            if self.dev:
                self.port_close()
            event.accept()
        else:
            event.ignore()

    def update_lcd_datetime(self):
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.lcdNumberDateTime.display(formatted_datetime)

    def port_open(self):
        current_port = self.comboBox.currentText()
        current_baudrate = int(self.comboBox_2.currentText())
        if not self.dev:
            self.dev = serial.Serial(current_port, current_baudrate, timeout=0.1)
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText(f"Port {current_port} has opened. Wait a sec")
            try:
                self.receiver.start_read()
            except:
                print("receiver has a problem")
                self.plainTextEdit.appendPlainText("receiver has a problem")
        else:
            print(f"{current_port} has already opened")
            self.plainTextEdit.appendPlainText(f"Port {current_port} has already opened")

    def port_close(self):
        if self.dev:
            if self.dev.isOpen():
                self.receiver.stop_read()
                self.dev.close()
                self.dev = None
                self.plainTextEdit.appendPlainText("Port has closed")
                print("Port has closed")
            else:
                self.plainTextEdit.appendPlainText("Port has Already closed")
                print("Port has Already closed")
        else:
            self.plainTextEdit.appendPlainText("there is no serial connection")
            print("there is no serial connection")

    def serial_write(self):
        if self.dev:
            tx_msg = self.lineEdit.text()
            tx_msg += "\r"
            self.dev.write(tx_msg.encode('utf-8'))
            self.lineEdit.clear()

    #Receiver가 디바이스에서 읽어온 메시지 업데이트
    def update_display(self, data):
        if data == 'error':
            self.port_close()
            QTimer.singleShot(6000, self.port_open)
            self.plainTextEdit.clear()
            self.plainTextEdit.appendPlainText("Please wait")
        else:
            self.plainTextEdit.appendPlainText(data)


class Receiver(QObject):
    data_received = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.serial_monitor = parent
        self.flag_1 = threading.Event()
        self.t = None
        self.ansi_escape = re.compile(r'(?:\x1B[@-_]|[\x80-\x9F])[0-?]*[ -/]*[@-~]')

    def run(self):
        while not self.flag_1.is_set():
            try:
                data = self.serial_monitor.dev.readline().decode('utf-8').strip()
                data = self.remove_ansi_escape_codes(data)
                if data:
                    self.data_received.emit(data)
                else:
                    pass
            except Exception as e:
                self.flag_1.set()
                self.data_received.emit("error")

    def start_read(self):
        self.flag_1.clear()
        self.t = threading.Thread(target=self.run)
        self.t.start()
        print(f"Start thread ID: {self.t.ident}")

    def stop_read(self):
        print(f"Stop thread ID: {self.t.ident}")
        self.flag_1.set()
        print("Waiting for thread to finish")
        self.t.join()  # 쓰레드가 안전하게 종료될 때까지 대기
        print("Thread has finished")

    def remove_ansi_escape_codes(self, input_string):
        return self.ansi_escape.sub('', input_string)


if __name__ == '__main__':
    app = QApplication()
    window = SerialMonitor()
    window.show()
    app.exec()
