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
  padding-inline: 5%;
  padding-top: 8px;
  padding-bottom: 32px;
  min-height: 100vh;

  display: flex;
  flex-direction: column;
}
main{
  flex: 1;
  display: flex;
  flex-direction: column;
}
</style>
