<template>
  <div class="card" style="width: 100%; height: 100%; background: none">
    <!-- <img :src="poster_path" class="card-img-top" alt=""> -->
    <div class="card-body" style="padding: 0">
      <!-- <img :src="poster_path" class="card-img-top" alt=""> -->
      <!-- <h5 class="card-title">{{ movie.title}}</h5> -->
      <MovieDetail :movie="movie" style="background-color: rgb(133 178 211)"/>
    </div>
  </div>
</template>

<script>
import MovieDetail from "@/components/MovieDetail.vue";

export default {
  name: "MovieCardView",
  components: {
    MovieDetail,
  },

  data() {
    return {
      youTubeURL: null,
      movie_d: null,
    };
  },
  props: {
    movie: Object,
  },
  computed: {
    poster_path() {
      const baseURL = "https://image.tmdb.org/t/p/w500";
      return baseURL + this.movie.poster_path;
    },
  },
  methods: {},
};
</script>

<style>
.card-body {
  display: block;
  margin: 0;
  padding: 0;
}
</style>