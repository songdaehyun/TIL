<template>
  <div class="card">
    <!-- <span>{{ result.title }}</span>
    <br/>
    <img :src="imgUrl" @click="addChoice"/> -->
    <div class="card_image">
      <img :src="imgUrl" @click="addChoice"/>
    </div>
    <div class="card_title title-white">
			<p>{{ result.title }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "MovieFormItem",
  props: {
    result: Object,
  },
  data() {
    return {
      // choice: false,
    };
  },
  computed: {
    imgUrl() {
      return `https://image.tmdb.org/t/p/w200${this.result.poster_path}`;
    },
  },
  methods: {
    addChoice() {
      console.log(1)
      // this.choice = !this.choice;
      // const choicemovie = {
      //   movie: this.result,
      //   add: this.choice,
      // }
      this.$store.commit("ADD_MOVIE", this.result);
    },
  },
};
</script>

<style scoped>
.cards-list {
  z-index: 0;
  width: 100%;
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
}

.card {
  margin: 30px auto;
  width: 300px;
  height: 300px;
  border-radius: 40px;
box-shadow: 5px 5px 30px 7px rgba(0,0,0,0.25), -5px -5px 30px 7px rgba(0,0,0,0.22);
  cursor: pointer;
  transition: 0.4s;
}

.card .card_image {
  width: inherit;
  height: inherit;
  border-radius: 40px;
}

.card .card_image img {
  width: inherit;
  height: inherit;
  border-radius: 40px;
  object-fit: cover;
}

.card .card_title {
  text-align: center;
  border-radius: 0px 0px 40px 40px;
  font-family: sans-serif;
  font-weight: bold;
  font-size: 30px;
  margin-top: -80px;
  height: 40px;
}

.card:hover {
  transform: scale(0.9, 0.9);
  box-shadow: 5px 5px 30px 15px rgba(0,0,0,0.25), 
    -5px -5px 30px 15px rgba(0,0,0,0.22);
}

.title-white {
  color: white;
}

.title-black {
  color: black;
}

@media all and (max-width: 500px) {
  .card-list {
    /* On small screens, we are no longer using row direction but column */
    flex-direction: column;
  }
}

</style>