<template>
  <div>
    <div
      class="modal fade"
      id="addModal"
      tabindex="-1"
      aria-labelledby="addModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content" style="background-color: rgb(133 178 211)">
          <div class="modal-header">
            <h1 class="modal-title fs-5" style=" font-weight: revert;
  font-size: x-large;" id="addModalLabel">Modal title</h1>
            <button
              type="button"
              class="btn-close"
              data-bs-dismiss="modal"
              aria-label="Close"
            ></button>
          </div>
          <div class="modal-body">
            <!-- <h1>추천 영화 추가하기</h1> -->
            <MovieForm :id="id" />
          </div>
          <div class="modal-footer">
            <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button>
            <button
              type="button"
              class="btn btn-primary"
              data-bs-toggle="modal"
              data-bs-target="#recommendModal"
              :data-bs-whatever="id"
            >
              add를 누른후 누르세요
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieForm from "@/components/MovieForm";

export default {
  name: "AddMovieView",
  data() {
    return {
      id: null,
    };
  },
  components: {
    MovieForm,
  },
  mounted() {
    const exampleModal = document.getElementById("addModal");
    exampleModal.addEventListener("show.bs.modal", (event) => {
      const button = event.relatedTarget;
      const recipient = button.getAttribute("data-bs-whatever");
      const modalTitle = exampleModal.querySelector(".modal-title");
      const master = this.$store.state.residents[Number(recipient)].name;
      modalTitle.textContent = `ADD TO ${master}'S MOVIES`;
      this.id = recipient;
      console.log(this.id);
    });
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Marcellus+SC&display=swap");

.modal-dialog {
  position: relative;
  display: flex;
  justify-content: center;
  top: 15%;
  max-width: none;
  width: 100%;
  height: 60%;
}

.modal-body {
  overflow: auto;
  
}

.modal-content {
  position: relative;
  display: flex;
  width: 80%;
  height: 100%;
  scrollbar-width: none;
  /* overflow: auto; */
}

.modal-header {
  border: none;
  justify-content: center;
  padding-bottom: 0;
}



.modal-title {
  font-family: "Marcellus SC", serif;
  font-weight: revert;
  font-size: x-large;
}

</style>