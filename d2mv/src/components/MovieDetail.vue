<template>
  <div>
    <vue-final-modal
      v-model="showModal"
      classes="modal-container"
      content-class="modal-content"
      style="margin: 0; padding: 0;"
    >
      <div class="modal__content" style="background-color: rgb(133 178 211)">
        <div>
          <div>
            <img :src="poster_path" alt="" />
          </div>
        </div>
        <div>
          <h1>&nbsp;&nbsp;&nbsp;</h1>
        </div>
        <div>
          <span class="modal__title">{{ movie.title }}</span>
          <br />
          <br />
          <p>시놉시스</p>
          <div>
            <p>{{ movie.overview }}</p>
          </div>
          <br />
          <p>트레일러</p>
          <div id="area">
            <iframe
              :src="youTubeURL"
              frameborder="0"
              v-if="showModal"
              id="video"
            ></iframe>
          </div>
        </div>
      </div>
    </vue-final-modal>
    <img
      :src="poster_path"
      class="card-img-top"
      alt=""
      @click="showModal = true"
    />
    <!-- <button @click="showModal = true">More Detail</button> -->
  </div>
</template>

<script>
import { VueFinalModal } from "vue-final-modal";
import axios from "axios";

export default {
  name: "MovieDetail",
  data() {
    return {
      showModal: false,
      youTubeURL: null,
    };
  },
  components: {
    VueFinalModal,
  },
  props: {
    movie: Object,
    show: Number,
  },
  computed: {
    poster_path() {
      const baseURL = "https://image.tmdb.org/t/p/w500";
      return baseURL + this.movie.poster_path;
    },
  },
  methods: {},
  mounted() {
    const apiKey = "4cdf408509bad3e333bfd82fc3c222bb";
    const baseURL = `https://api.themoviedb.org/3/movie/${this.movie.id}/videos?api_key=${apiKey}&language=en-US`;
    axios({
      method: "get",
      url: baseURL,
    })
      .then((response) => {
        const key = response.data.results[0].key;
        const URL = `https://www.youtube.com/embed/${key}`;
        this.youTubeURL = URL;
      })
      .catch((error) => {
        console.log(error);
      });
  },
};
</script>

<style scoped>
::v-deep .modal-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
::v-deep .modal-content {
  display: flex;
  flex-direction: column;
  max-height: 90%;
  margin: 20rem;
  padding: 1rem;
  border: 1px solid #527cb2;
  border-radius: 0.25rem;
  background: #fff;
}
.modal__title {
  font-size: 1.5rem;
  font-weight: 700;
}
.modal__content {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow-y: auto;
}
#area {
  position: relative;
  height: 0;
  padding-bottom: 56.25%;
}

#video {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
}

.dark-mode div::v-deep .modal-content {
  border-color: #2d3748;
  background-color: #1a202c;
}
</style>
