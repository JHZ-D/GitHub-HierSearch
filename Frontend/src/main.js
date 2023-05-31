import {
  createApp
} from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import naive from 'naive-ui'
import axios from 'axios'
import VueAxios from 'vue-axios'
import './index.css'

// axios.defaults.baseURL = 'http://localhost:3001/api'
axios.defaults.baseURL = 'http://162.105.16.191:5000'

createApp(App).use(naive).use(store).use(router).use(VueAxios, axios).mount('#app')
