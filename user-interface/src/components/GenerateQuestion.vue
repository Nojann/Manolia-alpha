<script setup lang="ts">
    import { onMounted } from 'vue'
    import { BProgress } from "buefy";
    import type { Knowledge } from "@/types/types";

    import api from "@/services/api";
    import { useItemStore } from '@/stores/item'
    import { useStepStore } from '@/stores/step'

    import { ProcessStep } from '@/services/knowledgeWorklow'

    const stepStore = useStepStore()
    const itemStore = useItemStore()

    onMounted(() => {
        if(itemStore.knowledge != undefined){
            generateQuestions(itemStore.knowledge)
        } 
    })
    
    async function generateQuestions (knowledge: Knowledge) {
        await api.post(`api/v1/knowledges/${knowledge.id}/questions`)
        if(stepStore.indexStep == ProcessStep.WaitGeneration)
            stepStore.nextStep()
    }
</script>

<template>
    <div class="container">
        <div class="title-container">
            <div class="title-icon">
                <img src="../assets/svg/a-b-2.svg" alt="generation icon" />
            </div>
            <h2>Génération de questions</h2>
        </div>
        <p>La génération par Small Language Model (SML) peut prendre plusieurs minutes, nous éxécutons le modèle sur CPU.</p>
        <p>En attendant, vous pouvez ajouter des nouvelles connaissances.</p>
        <div>
                <img src="../assets/svg/neural-network.svg" alt="neural network" />
            </div>
        <b-progress></b-progress>
    </div>
</template>

<style scoped>

</style>