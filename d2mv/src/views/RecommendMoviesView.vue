<template>
  <div>
    <div
      class="modal fade"
      id="recommendModal"
      tabindex="-1"
      aria-labelledby="recommendModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-xl">
        <div
          class="modal-content bg-opacity-50"
          style="background-color:  rgb(133 178 211)"
        >
          <div class="modal-body">
            <h1 class="modal-title" id="recommendModalLabel">Modal title</h1>
            <div class="cardlist">
              <MovieCardView
                v-for="movie in getList"
                :key="movie.id"
                :movie="movie"
              />
            </div>
          </div>
          <div class="modal-footer">
            <div id="container">
              <button
                id="passwordButton"
                class="learn-more"
                data-bs-toggle="modal"
                data-bs-target="#passwordModal"
              >
                <span class="circle" aria-hidden="true">
                  <span class="icon arrow"></span>
                </span>
                <span class="button-text">ADD</span>
              </button>
            </div>
            <!-- <button
              type="button"
              class="btn btn-secondary"
              data-bs-dismiss="modal"
            >
              Close
            </button> -->
            <!-- <button
              id="passwordButton"
              type="button"
              class="btn btn-primary"
              data-bs-toggle="modal"
              data-bs-target="#passwordModal"
            >
              Add
            </button> -->
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import MovieCardView from "@/views/MovieCardView.vue";

export default {
  name: "RecommendMoviesView",
  data() {
    return {
      id: "3",
      showModal: false,
    };
  },
  components: {
    MovieCardView,
  },
  computed: {
    getList() {
      const id = this.id;
      let who;
      for (const person of this.$store.state.residents) {
        if (person.id === id) {
          who = person;
        }
      }
      return who.movies;
    },
    getId() {
      const id = this.$route.params.id;
      return id;
    },
  },
  methods: {
    goPass() {
      this.$router.push({ name: "password" });
    },
  },
  mounted() {
    const exampleModal = document.getElementById("recommendModal");
    exampleModal.addEventListener("show.bs.modal", (event) => {
      const button = event.relatedTarget;
      const recipient = button.getAttribute("data-bs-whatever");
      const modalTitle = exampleModal.querySelector(".modal-title");
      const master = this.$store.state.residents[Number(recipient)].name;
      modalTitle.textContent = `${master}'s RECOMMENDED MOVIES`;
      this.id = recipient;
      console.log(recipient);
      const passbutton = document.getElementById("passwordButton");
      passbutton.setAttribute("data-bs-whatever", recipient);
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
  top: 8%;
  max-width: none;
  width: 100%;
  height: 80%;
}

.modal-content {
  position: relative;
  display: flex;
  width: 70%;
  height: 100%;
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

.modal-body {
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  display: grid;
  place-items: center;
  border: none;
}

.modal-footer {
  border: none;
}

.cardlist {
  display: flex;
  grid-gap: 1rem;
  padding: 1rem;
  max-width: 1024px;
  margin: 0;
  grid-template-columns: repeat(auto-fill, minmax(auto, auto));
  grid-template-rows: 1;
}

.card {
  /* position: absolute;
  display: block; */
  position: relative;
  display: flex;
  align-items: flex-end;
  overflow: hidden;
  height: 500px;
  width: 350px;
}

@import url("https://fonts.googleapis.com/css?family=Mukta:700");
* {
  box-sizing: border-box;
}
*::before,
*::after {
  box-sizing: border-box;
}

body {
  font-family: "Mukta", sans-serif;
  font-size: 1rem;
  line-height: 1.5;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0;
  min-height: 100vh;
  background: #f3f8fa;
}

button {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  background: transparent;
  padding: 0;
  font-size: inherit;
  font-family: inherit;
}

button.learn-more {
  width: 12rem;
  height: auto;
}

button.learn-more .circle {
  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
  position: relative;
  display: block;
  margin: 0;
  width: 3rem;
  height: 3rem;
  background: #282936;
  border-radius: 1.625rem;
}

button.learn-more .circle .icon {
  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
  position: absolute;
  top: 0;
  bottom: 0;
  margin: auto;
  background: #fff;
}

button.learn-more .circle .icon.arrow {
  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
  left: 0.625rem;
  width: 1.125rem;
  height: 0.125rem;
  background: none;
}

button.learn-more .circle .icon.arrow::before {
  position: absolute;
  content: "";
  top: -0.25rem;
  right: 0.0625rem;
  width: 0.625rem;
  height: 0.625rem;
  border-top: 0.125rem solid #fff;
  border-right: 0.125rem solid #fff;
  transform: rotate(45deg);
}

button.learn-more .button-text {
  transition: all 0.45s cubic-bezier(0.65, 0, 0.076, 1);
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  padding: 0.75rem 0;
  margin: 0 0 0 1.85rem;
  color: #282936;
  font-weight: 700;
  line-height: 1.6;
  text-align: center;
  text-transform: uppercase;
}

button:hover .circle {
  width: 100%;
}

button:hover .circle .icon.arrow {
  background: #fff;
  transform: translate(1rem, 0);
}

button:hover .button-text {
  color: #fff;
}

@supports (display: grid) {
  body {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-gap: 0.625rem;
    grid-template-areas: ". main main ." ". main main .";
  }

  #container {
    grid-area: main;
    align-self: center;
    justify-self: center;
  }
}
</style>

