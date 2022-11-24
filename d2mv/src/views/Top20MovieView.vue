<template>
  <div>
    <div v-for="movie in getMovies" :key="movie.id">
      <div>{{ movie.title }}</div>
      <div v-if="movie">
      <img
        :src="`https://image.tmdb.org/t/p/w500/${movie?.poster_path}`"
        alt=""
      />
      <p>{{ movie?.title }}</p>
    </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const TMDB_KEY = '0e8d3fc01fe7a24c7b15c89f38fc06a9'
const TMDB_URL = 'https://api.themoviedb.org/3/movie'

export default {
  name: 'Top20MovieView',
  data() {
    return {
      movies: [],
    }
  },
  computed: {
    getMovies() {
      // return this.$store.state.getTop20Movies 
      console.log("ff", this.movies.results)
      return this.movies.results
    }
  },
  methods: {
    getTop20Movies() {
      axios({
        method: 'get',
        url: `${TMDB_URL}/popular`,
        params: {
          api_key: TMDB_KEY,
          language: 'ko-KR',
        }
      })
        .then((res) => {
          console.log(res.data)
          this.movies = res.data
        })
    }
  },
  created() {
    this.getTop20Movies()
  }
}
</script>

<style>
.top20movies {
  z-index: 999
}
</style>