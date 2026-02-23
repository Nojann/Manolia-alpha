<script setup lang="ts">
import { RouterView } from 'vue-router'
import AppTopbar from '@/components/AppTopbar.vue'
</script>

<template>
  <header>
    <AppTopbar />
  </header>
  <main>
    <RouterView />
  </main>
  <!-- <footer>
    <AppFooter />
  </footer> -->
</template>

<style>
#app {
  background-color: #FFF4EA;
  padding-inline: 5%;
  height: 100vh;
}

/* main {
  height: 100%;
}

@media screen and (min-width: 768px) {
  #app {
    height: 100vh;
  }
} */
</style>
