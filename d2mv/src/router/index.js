import Vue from 'vue'
import VueRouter from 'vue-router'
import VillageView from '../views/VillageView.vue'
import RecommendMoviesView from '../views/RecommendMoviesView.vue'
import MovieCardView from '../views/MovieCardView.vue'
import AddMovieView from '../views/AddMovieView.vue'
import PasswordView from '../views/PasswordView.vue'
import Top20MovieView from '../views/Top20MovieView.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'village',
    component: VillageView
  },
  {
    path: '/recommend/:id',
    name: 'recommend',
    component: RecommendMoviesView
  },
  {
    path: '/movie',
    name: 'movie',
    component: MovieCardView
  },
  {
    path: '/add/:id',
    name: 'add',
    component: AddMovieView
  },
  {
    path: '/password/:id',
    name: 'password',
    component: PasswordView
  },
  {
    path: '/top20',
    name: 'top20',
    component: Top20MovieView
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
