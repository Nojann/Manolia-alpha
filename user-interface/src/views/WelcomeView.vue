<script setup lang="ts">
    import { BButton } from "buefy"
</script>

<template>
    <section>
        <b-button type="is-primary" size="is-medium" rounded>
            <RouterLink to="/experiment"><span>Lancer l'expérience</span></RouterLink>
        </b-button>
    </section>
</template>

<style scoped>
    section{
        display: flex;
        height: 80vh;
        justify-content: center;
        align-items: center;
    }
    span{
        color: black;
    }
</style>