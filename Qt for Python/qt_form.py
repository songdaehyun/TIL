
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'qt_form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QTimer,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
                               QPlainTextEdit, QPushButton, QSizePolicy, QWidget, QDateTimeEdit, QLCDNumber)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(522, 463)
        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(70, 80, 68, 22))
        self.comboBox_2 = QComboBox(Form)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(230, 80, 68, 22))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 80, 31, 16))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 80, 50, 16))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 110, 181, 24))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 110, 161, 24))
        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(400, 160, 75, 24))
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 160, 351, 21))
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(30, 200, 461, 241))

        #lcd
        self.lcdNumberDateTime = QLCDNumber(Form)
        self.lcdNumberDateTime.setObjectName(u"lcdNumberDateTime")
        self.lcdNumberDateTime.setGeometry(60, 15, 380, 50)
        self.lcdNumberDateTime.setDigitCount(19)
        self.lcdNumberDateTime.setStyleSheet("QLCDNumber { background-color: white; color: black; }")
        current_datetime = QDateTime.currentDateTime()
        formatted_datetime = current_datetime.toString("yyyy-MM-dd hh:mm:ss")
        self.lcdNumberDateTime.display(formatted_datetime)

        #timer
        self.timer = QTimer(Form)


        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.port_open)
        self.pushButton_2.clicked.connect(Form.port_close)
        self.pushButton_3.clicked.connect(Form.serial_write)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Port", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Baudrate", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Open", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Close", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Write", None))
    # retranslateUi

