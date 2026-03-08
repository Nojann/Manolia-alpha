<script setup lang="ts">
  import { BNavbar, BNavbarItem } from "buefy";
</script>

<template>
    <b-navbar class="navbar" shadow >
      <template #brand>
         <b-navbar-item tag="router-link" :to="{ path: '/' }" id="brand">
                    <img class="logo" src="../assets/svg/manolia-logo.svg" alt="Manolia logo" />
                    <h1 class="title">MANOLIA</h1>
          </b-navbar-item>
      </template>
    </b-navbar>
</template>

<style scoped>
  .navbar{
    border-radius: 16px;
    margin-bottom: 24px;
    height: 4rem;
  }

  #brand:hover, #brand:focus, #brand:active{
    background-color: inherit;
  }

  .title{
    font-size: 1.5rem;
    font-family: "Exo-Black";
  }


</style>