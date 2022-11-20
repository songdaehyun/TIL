<template>
  <div class="card">
    <img :src="poster_path" class="card-img-top" alt="">
    <div class="card-body">
      <h5 class="card-title">{{ movie.title}}</h5>
    </div>
    <MovieDetail :movie="movie"/>
  </div>
</template>

<script>
import MovieDetail from '@/components/MovieDetail.vue'

export default {
  name: "MovieCardView",
  components: {
    MovieDetail
  },
  
  data() {
    return {
      youTubeURL: null,
      movie_d: null,
    }
  },
  props: {
    movie: Object
  },
  computed: {
    poster_path() {
      const baseURL = 'https://image.tmdb.org/t/p/w500'
      return baseURL + this.movie.poster_path
    }
  },  
};
</script>

<style>
</style>