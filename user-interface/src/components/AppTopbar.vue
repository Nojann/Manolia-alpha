<template>
    <div class="topbar-container">
        <div class="logo-container">
            <img class="logo" src="../assets/svg/manolia-logo.svg" alt="Manolia logo" />
            <span>MANOLIA</span>
        </div>
    </div>
</template>

<style scoped>
.topbar-container {
  height: 4rem;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: left;
}
.logo-container {
  width: 20rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;

  img {
    width: 2rem;
  }
}

</style>