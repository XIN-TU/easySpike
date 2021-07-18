import Vue from 'vue'
import Router from 'vue-router'
// import Home from './views/Home.vue'
import Api from './views/Api.vue'
import Search from './views/Search.vue'
import Credit from './views/Credit.vue'
import Spike from './views/Spike.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'spike',
      component: Spike
    },
    {
      path: '/api',
      name: 'api',
      component: Api
    },
    {
      path: '/search',
      name: 'search',
      component: Search
    },
    {
      path: '/credit',
      name: 'credit',
      component: Credit
    }
  ]
})
