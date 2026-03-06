<script setup lang="ts">
    import ReadKnowledges from '@/components/ReadKnowledges.vue';
    import { useStepStore } from '@/stores/step'

    const stepStore = useStepStore()
</script>

<template>
    <div class="experiment-container">
        <section id="section-left">
            <ReadKnowledges/>
        </section>
        <section id="section-central">
            <component :is="stepStore.getCurrentComponent"></component>
        </section>
    </div>
</template>

<style scoped>
    .experiment-container{
        display: grid;
        grid-template-columns: 1fr 3fr;
        gap: 24px;
    }
</style>