<template>
  <div>
    <audio autoplay v-if="santa">
      <source src="@/assets/Santa Tell Me-1-Ariana Grande.mp3" type="audio/mp3">
    </audio>
    <button @click="getSnow">snow</button>
    <div class="snowflakes" aria-hidden="true" v-if="snowing">
      <div class="snowflake">
      ❅
      </div>
      <div class="snowflake">
      ❆
      </div>
      <div class="snowflake">
      ❅
      </div>
      <div class="snowflake">
      ❆
      </div>
      <div class="snowflake">
      ❅
      </div>
      <div class="snowflake">
      ❆
      </div>
      <div class="snowflake">
        ❅
      </div>
      <div class="snowflake">
        ❆
      </div>
      <div class="snowflake">
        ❅
      </div>
      <div class="snowflake">
        ❆
      </div>
      <div class="snowflake">
        ❅
      </div>
      <div class="snowflake">
        ❆
      </div>
    </div>
    
    <div class="container">
      <img id="b1" data-bs-whatever="0" data-bs-toggle="modal" data-bs-target="#recommendModal"  src="../assets/img/5.png" alt="" />
      <img id="b2" data-bs-whatever="1" data-bs-toggle="modal" data-bs-target="#recommendModal"  src="../assets/img/7.png" alt="" />
      <img id="b3" class="shadow-pop-tr" src="../assets/img/8.png" alt="" />
      <img id="b4" class="shadow-pop-tr" src="../assets/img/9-1.png" alt="" />
      <img id="b5" class="shadow-pop-tr" src="../assets/img/10.png" alt="" />
      <img id="b6" class="shadow-pop-tr" src="../assets/img/11-1.png" alt="" />
      <img id="b7" class="shadow-pop-tr" src="../assets/img/12-1.png" alt="" />
      <img id="b8" class="shadow-pop-tr" src="../assets/img/13-1.png" alt="" />
      <img id="b9" class="shadow-pop-tr" src="../assets/img/14.png" alt="" />
      <img id="b10" class="shadow-pop-tr" src="../assets/img/15.png" alt="" />
      <!-- <img id="t1" class="shadow-pop-tr" src="../assets/20.png" alt="" /> -->
    </div>
      <RecommendMoviesView/>
      <PasswordView />
      <AddMovieView/>
  </div>
</template>


<script>
import RecommendMoviesView from './RecommendMoviesView.vue';
import PasswordView from './PasswordView.vue';
import AddMovieView from './AddMovieView.vue';

export default {
  name: "VillageView",
  data() {
    return{
      santa: false,
      snowing: false,
      id: null,
    }
  },
  components: {
    RecommendMoviesView,
    PasswordView,
    AddMovieView
  },
  
  methods: {   
    getSnow() {
      this.snowing = !this.snowing
      this.santa = !this.santa

    },
  }

};
</script>

<style scoped>

button {
  position: absolute;
  border: 0;
  outline: 0;
  left: 2%;
  color: aliceblue;
  background-color: transparent;
  font-size: 50px;
}

/* .background {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
  margin: 0;
  padding: 0;
  background-image: url("../assets/배경6.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  filter: brightness(1.1);
} */

/* .container {
  position: relative;
  top: 41vh;
  width: 100%;
  height: 45vh;
  margin: 0;
  padding: 0;
  max-width: 100%;
} */

img {
  display: inline-block;
  position: absolute;
  filter: brightness(1.1);
}

#b1 {
  bottom: 14.1vh;
  left: 0;
}
img:hover
{
  border: solid 5px transparent;
}


#b2 {
  bottom: 14.1vh;
  left: 10%;
}

#b3 {
  bottom: 14.1vh;
  left: 22%;
}

#b4 {
  bottom: 12.7vh;
  left: 30%;
}

#b5 {
  bottom: 14.1vh;
  left: 40%;
}

#b6 {
  bottom: 14.1vh;
  left: 47.2%;
}

#b7 {
  bottom: 13.95vh;
  left: 58%;
}

#b8 {
  bottom: 13.1%;
  left: 65%;
}

#b9 {
  bottom: 14.1vh;
  left: 76.5%;
}

#b10 {
  bottom: 14.1vh;
  right: 0;
}


img:hover {
  opacity: 1;
}

  .snowflake {
  color: #fff;
  font-size: 1em;
  font-family: Arial, sans-serif;
  text-shadow: 0 0 5px rgb(233, 225, 225);
}


@-webkit-keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@-webkit-keyframes snowflakes-shake{0%,100%{-webkit-transform:translateX(0);transform:translateX(0)}50%{-webkit-transform:translateX(80px);transform:translateX(80px)}}@keyframes snowflakes-fall{0%{top:-10%}100%{top:100%}}@keyframes snowflakes-shake{0%,100%{transform:translateX(0)}50%{transform:translateX(80px)}}.snowflake{position:fixed;top:-10%;z-index:9999;-webkit-user-select:none;-moz-user-select:none;-ms-user-select:none;user-select:none;cursor:default;-webkit-animation-name:snowflakes-fall,snowflakes-shake;-webkit-animation-duration:10s,3s;-webkit-animation-timing-function:linear,ease-in-out;-webkit-animation-iteration-count:infinite,infinite;-webkit-animation-play-state:running,running;animation-name:snowflakes-fall,snowflakes-shake;animation-duration:10s,3s;animation-timing-function:linear,ease-in-out;animation-iteration-count:infinite,infinite;animation-play-state:running,running}.snowflake:nth-of-type(0){left:1%;-webkit-animation-delay:0s,0s;animation-delay:0s,0s}.snowflake:nth-of-type(1){left:10%;-webkit-animation-delay:1s,1s;animation-delay:1s,1s}.snowflake:nth-of-type(2){left:20%;-webkit-animation-delay:6s,.5s;animation-delay:6s,.5s}.snowflake:nth-of-type(3){left:30%;-webkit-animation-delay:4s,2s;animation-delay:4s,2s}.snowflake:nth-of-type(4){left:40%;-webkit-animation-delay:2s,2s;animation-delay:2s,2s}.snowflake:nth-of-type(5){left:50%;-webkit-animation-delay:8s,3s;animation-delay:8s,3s}.snowflake:nth-of-type(6){left:60%;-webkit-animation-delay:6s,2s;animation-delay:6s,2s}.snowflake:nth-of-type(7){left:70%;-webkit-animation-delay:2.5s,1s;animation-delay:2.5s,1s}.snowflake:nth-of-type(8){left:80%;-webkit-animation-delay:1s,0s;animation-delay:1s,0s}.snowflake:nth-of-type(9){left:90%;-webkit-animation-delay:3s,1.5s;animation-delay:3s,1.5s}.snowflake:nth-of-type(10){left:25%;-webkit-animation-delay:2s,0s;animation-delay:2s,0s}.snowflake:nth-of-type(11){left:65%;-webkit-animation-delay:4s,2.5s;animation-delay:4s,2.5s}
</style>