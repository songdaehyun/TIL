<template>
  <div>
    <div>
      <form @submit.prevent="searchMovie">
        <input type="text" v-model.trim="addmovietitle" />
        <button @click="searchMovie">검색</button>
      </form>
    </div>
      <MovieFormItem
        v-for="(result, index) in results"
        :key="index"
        :result="result"
      />
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
    id: String
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
            language: "ko",
          },
        })
          .then((responese) => {
            console.log(responese);
            this.results = responese.data.results;
          })
          .catch((error) => {
            console.log(error);
          });
      }
    },
    AddToMovies() {
      console.log(2)
      this.$store.dispatch("AddToMovies", this.id);
    },
  },
};
</script>

<style>


</style>