import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import Buefy from "buefy";
import "buefy/dist/css/buefy.css";
import "@/assets/fonts.css"
import "@/assets/global.css"


const app = createApp(App)

app.use(createPinia())
app.use(router)
app.use(Buefy)

app.mount('#app')
