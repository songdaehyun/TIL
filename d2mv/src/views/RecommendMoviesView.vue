<template>
  <div>
    <div class="modal fade" id="recommendModal" tabindex="-1" aria-labelledby="recommendModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-xl" >
        <div class="modal-content bg-secondary bg-opacity-50">
          <div class="modal-header">
            <h1 class="modal-title fs-5" id="recommendModalLabel">Modal title</h1>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">
            <h1>Recommended Movies</h1>
            <div class="row row-cols-1 row-cols-md-3 g-4">
              <MovieCardView
                v-for="movie in getList"
                :key = "movie.id"
                :movie="movie"
              />
            </div>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
            <button id="passwordButton" type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#passwordModal" >영화 추가하러가기(비번입력)</button>
          </div>
        </div>
      </div>
    </div>   
  </div>
</template>

<script>
import MovieCardView from '@/views/MovieCardView.vue';


export default {
  name: "RecommendMoviesView",
  data() {
    return {
      id: '0',
      showModal: false
    }
  },
  components: {
    MovieCardView,
  },
  computed: {
    getList() {
      const id = this.id
      let who
      for (const person of this.$store.state.residents) {
        if (person.id === id) {
          who = person
        }
      }
      return who.movies
    },
    getId() {
      const id = this.$route.params.id
      return id
    }
    
  },
  methods: {
    goPass() {
      this.$router.push({ name: 'password' })
    }
  },
  mounted() {
    const exampleModal = document.getElementById('recommendModal')
    exampleModal.addEventListener('show.bs.modal', event => {
      const button = event.relatedTarget 
      const recipient = button.getAttribute('data-bs-whatever')
      const modalTitle = exampleModal.querySelector('.modal-title')
      const master = this.$store.state.residents[Number(recipient)].name
      modalTitle.textContent = `${master}의 추천영화`
      this.id = recipient
      console.log(recipient)
      const passbutton = document.getElementById('passwordButton')
      passbutton.setAttribute('data-bs-whatever', recipient)
      
    })
  }  
};
</script>

<style>
 
</style>

