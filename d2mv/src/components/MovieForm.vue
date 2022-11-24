<template>
  <div class="topdiv">
      <form @submit.prevent="searchMovie">
        <div class="" style="display: inline-block">
          <input type="text" v-model.trim="addmovietitle" style="backgound: none; border:0 solid black; border-radius: 10px;"/>
          <button class="search jello-horizontal " @click="searchMovie">
            👀
          </button>
        </div>
      </form>
    <div class="cards_list">
      <MovieFormItem
        v-for="(result, index) in results"
        :key="index"
        :result="result"
      />
    </div>
    <br />
    <button @click="AddToMovies">Add</button>
  </div>
</template>

<script>
import axios from "axios";
import MovieFormItem from "@/components/MovieFormItem";

export default {
  name: "MovieForm",
  components: {
    MovieFormItem,
  },
  data() {
    return {
      addmovietitle: null,
      results: null,
    };
  },
  props: {
    id: String,
  },
  methods: {
    searchMovie() {
      if (this.addmovietitle) {
        const API_KEY = process.env.VUE_APP_API_KEY;
        const SEARCH_URL = "https://api.themoviedb.org/3/search/movie";

        axios({
          method: "get",
          url: SEARCH_URL,
          params: {
            api_key: API_KEY,
            query: this.addmovietitle,
            language: "en",
          },
        })
          .then((responese) => {
            console.log(responese);
            this.results = responese.data.results;
          })
          .catch((error) => {
            console.log(error);
          });
        this.addmovietitle = null
      }
    },
    AddToMovies() {
      console.log(2);
      this.$store.dispatch("AddToMovies", this.id);
    },
  },
};
</script>

<style scoped>
.jello-horizontal:hover{
	animation: jello-horizontal 0.9s both;
}

@keyframes jello-horizontal {
  0% {
    transform: scale3d(1, 1, 1);
  }
  30% {
    transform: scale3d(1.25, 0.75, 1);
  }
  40% {
    transform: scale3d(0.75, 1.25, 1);
  }
  50% {
    transform: scale3d(1.15, 0.85, 1);
  }
  65% {
    transform: scale3d(0.95, 1.05, 1);
  }
  75% {
    transform: scale3d(1.05, 0.95, 1);
  }
  100% {
    transform: scale3d(1, 1, 1);
  }
}


.cards_list {
  z-index: 0;
  width: 100%;
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
}

input {
  width: 250px;
  height: 40px;
  border-top: none;
  border-left: none;
  border-right: none;
  border-bottom: 2px solid rgb(7, 3, 31);
}

.search {
  border: 0;
  outline: 0;
  background-color: transparent;
  font-size: 50px;
}
</style>