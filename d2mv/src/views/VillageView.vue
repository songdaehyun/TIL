<template>
  <div style="width:3400px">
    <div class="container">
      <img
        id="b1"
        data-bs-whatever="0"
        data-bs-toggle="modal"
        data-bs-target="#recommendModal"
        src="../assets/img/5.png"
        alt=""
      />
      <img
        id="b2"
        data-bs-whatever="1"
        data-bs-toggle="modal"
        data-bs-target="#recommendModal"
        src="../assets/img/7.png"
        alt=""
      />
      <img 
        id="b3" 
        data-bs-whatever="2"
        data-bs-toggle="modal"
        data-bs-target="#recommendModal" 
        src="../assets/img/8.png" 
        alt="" />
      <img 
        id="b4"
        data-bs-whatever="3"
        data-bs-toggle="modal"
        data-bs-target="#recommendModal"  
        src="../assets/img/9-1.png" 
        alt="" />
      <img 
        id="b5"
        data-bs-whatever="4"
        data-bs-toggle="modal"
        data-bs-target="#recommendModal"  
        src="../assets/img/10.png" 
        alt="" />
      <img id="b6" data-bs-whatever="6" data-bs-toggle="modal" data-bs-target="#recommendModal"  src="../assets/img/11-1.png" alt=""/>
      <img id="b7"  src="../assets/img/12-1.png" alt="" />
      <img 
        id="b8"
        data-bs-whatever="7"
        data-bs-toggle="modal"
        data-bs-target="#recommendModal"   
        src="../assets/img/13-1.png" 
        alt="" />
      <img id="b9"  src="../assets/img/14.png" alt="" />
      <img id="b10" src="../assets/img/15.png" alt="" />
      <!-- <img id="l1" src="../assets/img/1-1.png" alt="" /> -->
      <img id="t2" src="../assets/img/20.png" alt="" />
      <img id="l2" src="../assets/img/2.png" alt="" />
      <!-- <img id="l3" src="../assets/img/3.png" alt="" /> -->
      <!-- <img id="l4" src="../assets/img/4.png" alt="" /> -->
      <img id="l5" src="../assets/img/4.png" alt="" />
      <img id="t1" src="../assets/img/18.png" alt="" />
      <img id="l6" src="../assets/img/2.png" alt="" />
      <img id="l7" src="../assets/img/4.png" alt="" />
      <!-- <img id="t1" class="shadow-pop-tr" src="../assets/20.png" alt="" /> -->
      <img id="b11"  src="../assets/img/11-1.png" alt=""/>
      <img id="b12"  src="../assets/img/12-1.png" alt="" />
      <img id="b13"  src="../assets/img/11-1.png" alt=""/>
      
      <img id="b15"  src="../assets/img/7.png" alt=""/>
      <img id="b16"  src="../assets/img/12-1.png" alt="" />
      <img id="b17"  src="../assets/img/8.png" alt=""/>
      <img id="b18"  src="../assets/img/9-1.png" alt="" />
      <img id="b19"  src="../assets/img/11-1.png" alt=""/>
      <img id="b20"  src="../assets/img/12-1.png" alt="" />
      <img id="b21"  src="../assets/img/8.png" alt=""/>
      <img id="b22"  src="../assets/img/9-1.png" alt="" />
      <img id="b23"  src="../assets/img/13-1.png" alt=""/>
      <img id="b24"  src="../assets/img/5.png" alt="" />
    </div>
    <RecommendMoviesView/>
    <PasswordView />
    <AddMovieView />
    <a href="#b24" style="position: absolute; right:3%; top: 35%; text-decoration: none; color: azure; ">옆마을 가기 &#9755;</a>
    <a href="#b1" style="position: absolute; right:-20%; top: 35%; text-decoration: none; color: azure; ">옆마을 가기 &#9754;</a>
    <div style="width:1700px;">
      <a href="#">&nbsp;</a>
    </div>
  </div>
</template>


<script>
import RecommendMoviesView from "./RecommendMoviesView.vue";
import PasswordView from "./PasswordView.vue";
import AddMovieView from "./AddMovieView.vue";

export default {
  name: "VillageView",
  data() {
    return {
      santa: false,
      snowing: false,
      id: null,
    };
  },
  components: {
    RecommendMoviesView,
    PasswordView,
    AddMovieView,
  },

  methods: {
    getSnow() {
      this.snowing = !this.snowing;
      this.santa = !this.santa;
    },
    goToTop20() {
      this.$router.push({ name: 'top20' })
    }
  },
};
</script>

<style scoped>


button {
  /* position: absolute; */
  border: 0;
  outline: 0;
  /* left: 2%; */
  color: aliceblue;
  background-color: transparent;
  font-size: 25px;
}

/* .router-link {
  top: 0%;
} */
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
img:hover {
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
  left: 76.6%;
}

#b10 {
  bottom: 14.1vh;
  right: 0;
}

#l1 {
  bottom: 8.7vh;
  width: 1920px;
  left: 0%;
}

#l2 {
  bottom: 14.1vh;
  left: 15%;
}

#l3 {
  bottom: 14.1vh;
  left: 50%;
}

#l4 {
  bottom: 13.5vh;
  height: 302px;
  left: 44.2%;
}

#l5 {
  bottom: 13.5vh;
  height: 302px;
  left: 11.1%;
}

#t1 {
  bottom: 12.1vh;
  left: 73%;
}

#l6 {
  bottom: 14.1vh;
  left: 70%;
}

#l7 {
  bottom: 13.5vh;
  height: 302px;
  left: 66.1%;
}

#t2 {
  bottom: 13.8vh;
  left: 21%;
}

#b11 {
  bottom: 14.1vh;
  left: 94.6%;
}

#b12 {
  bottom: 14.1vh;
  left: 105.6%;
}
#b13 {
  bottom: 14.1vh;
  left: 115.6%;
}

#b15 {
  bottom: 14.1vh;
  left: 123.6%;;
}
#b16 {
  bottom: 14.1vh;
  left: 136.6%;;
}
#b17 {
  bottom: 14.1vh;
  left: 143.6%;;
}
#b18 {
  bottom: 12.7vh;
  left: 148.6%;;
}
#b19 {
  bottom: 14.1vh;
  left: 158.6%;;
}
#b20 {
  bottom: 14.1vh;
  left: 167.6%;;
}
#b21 {
  bottom: 14.1vh;
  left: 174.6%;;
}
#b22 {
  bottom: 12.7vh;
  left: 178.6%;;
}
#b23 {
  bottom: 13.1vh;
  left: 189.6%;;
}
#b24 {
  bottom: 14.1vh;
  left: 200.6%;;
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

@-webkit-keyframes snowflakes-fall {
  0% {
    top: -10%;
  }
  100% {
    top: 100%;
  }
}
@-webkit-keyframes snowflakes-shake {
  0%,
  100% {
    -webkit-transform: translateX(0);
    transform: translateX(0);
  }
  50% {
    -webkit-transform: translateX(80px);
    transform: translateX(80px);
  }
}
@keyframes snowflakes-fall {
  0% {
    top: -10%;
  }
  100% {
    top: 100%;
  }
}
@keyframes snowflakes-shake {
  0%,
  100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(80px);
  }
}
.snowflake {
  position: fixed;
  top: -10%;
  z-index: 9999;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  cursor: default;
  -webkit-animation-name: snowflakes-fall, snowflakes-shake;
  -webkit-animation-duration: 10s, 3s;
  -webkit-animation-timing-function: linear, ease-in-out;
  -webkit-animation-iteration-count: infinite, infinite;
  -webkit-animation-play-state: running, running;
  animation-name: snowflakes-fall, snowflakes-shake;
  animation-duration: 10s, 3s;
  animation-timing-function: linear, ease-in-out;
  animation-iteration-count: infinite, infinite;
  animation-play-state: running, running;
}
.snowflake:nth-of-type(0) {
  left: 1%;
  -webkit-animation-delay: 0s, 0s;
  animation-delay: 0s, 0s;
}
.snowflake:nth-of-type(1) {
  left: 10%;
  -webkit-animation-delay: 1s, 1s;
  animation-delay: 1s, 1s;
}
.snowflake:nth-of-type(2) {
  left: 20%;
  -webkit-animation-delay: 6s, 0.5s;
  animation-delay: 6s, 0.5s;
}
.snowflake:nth-of-type(3) {
  left: 30%;
  -webkit-animation-delay: 4s, 2s;
  animation-delay: 4s, 2s;
}
.snowflake:nth-of-type(4) {
  left: 40%;
  -webkit-animation-delay: 2s, 2s;
  animation-delay: 2s, 2s;
}
.snowflake:nth-of-type(5) {
  left: 50%;
  -webkit-animation-delay: 8s, 3s;
  animation-delay: 8s, 3s;
}
.snowflake:nth-of-type(6) {
  left: 60%;
  -webkit-animation-delay: 6s, 2s;
  animation-delay: 6s, 2s;
}
.snowflake:nth-of-type(7) {
  left: 70%;
  -webkit-animation-delay: 2.5s, 1s;
  animation-delay: 2.5s, 1s;
}
.snowflake:nth-of-type(8) {
  left: 80%;
  -webkit-animation-delay: 1s, 0s;
  animation-delay: 1s, 0s;
}
.snowflake:nth-of-type(9) {
  left: 90%;
  -webkit-animation-delay: 3s, 1.5s;
  animation-delay: 3s, 1.5s;
}
.snowflake:nth-of-type(10) {
  left: 25%;
  -webkit-animation-delay: 2s, 0s;
  animation-delay: 2s, 0s;
}
.snowflake:nth-of-type(11) {
  left: 65%;
  -webkit-animation-delay: 4s, 2.5s;
  animation-delay: 4s, 2.5s;
}
</style>