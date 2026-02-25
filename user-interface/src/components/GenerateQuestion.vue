<script setup lang="ts">
    import { onMounted } from 'vue'
    import { BProgress } from "buefy";
    import type { Knowledge } from "@/types/types";

    import { apiClient } from "@/services/api";
    import { useItemStore } from '@/stores/item'
    import { useStepStore } from '@/stores/step'

    const stepStore = useStepStore()
    const itemStore = useItemStore()

    onMounted(() => {
        if(itemStore.knowledge != undefined){
            generateQuestions(itemStore.knowledge)
        } 
    })
    
    async function generateQuestions (knowledge: Knowledge) {
        await apiClient.post(`api/v1/knowledges/${knowledge.id}/questions`, null)
        stepStore.nextStep()
    }
</script>

<template>
    <div class="container">
        <h2>Generation</h2>
        <b-progress></b-progress>
    </div>
</template>

<style scoped>
.container{
    background-color: #ffffff;
    border-radius: 16px;
    padding: 34px;
}
</style>