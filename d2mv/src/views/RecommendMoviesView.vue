<template>
  <div>
    <nav>
      <router-link :to="{name: 'village'}">마을로 돌아가기</router-link>
    </nav>
    <h1>Recommended Movies</h1>
    <div class="row row-cols-1 row-cols-md-3 g-4">
      <MovieCardView
        v-for="movie in getList"
        :key = "movie.id"
        :movie="movie"
      />
    </div>
    <button @click="goPass">Add Movie</button>
    
  </div>
</template>

<script>
import MovieCardView from '@/views/MovieCardView.vue';

export default {
  name: "RecommendMoviesView",
  data() {
    return {
      id: null,
      showModal: false
    }
  },
  components: {
    MovieCardView
  },
  computed: {
    getList() {
      const id = this.$route.params.id
      let who
      for (const person of this.$store.state.residents) {
        if (person.id === id) {
          who = person
        }
      }
      return who.movies
    },
    
  },
  methods: {
    goPass() {
      this.$router.push({ name: 'password' })
    }
  }
  // created() {
  //   this.id = this.$route.params.id
  //   console.log(this.id)
  // }
  
};
</script>

<style>

</style>

