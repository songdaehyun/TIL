<template>
  <div id="app" >
    <img src="@/assets/배경6.jpg" alt="" id="bg">
    <nav>
      <a href="#">Home</a>
      <a href="#">Movies</a>
      <a href="#">Recommend</a>
    </nav>
    <footer>(주) 송은희 건설</footer>
    <router-view />
  </div>
</template>

<style scoped>
#bg {
  position: fixed; 
  top: 0; 
  left: 0; 
    
  /* Preserve aspet ratio */
  min-width: 100%;
  min-height: 100%;
}


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}



footer {
  width: 100%;
  position: fixed;
  bottom: 2%;
  text-align: center;
  color: white;
  z-index: 1;
}
</style>
