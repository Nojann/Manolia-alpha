<script setup lang="ts">
    import ReadKnowledges from '@/components/ReadKnowledges.vue';
    import { useStepsStore } from '@/stores/steps'

    const stepsStore = useStepsStore()
    stepsStore
</script>

<template>
    <div class="experiment-container">
        <section id="section-left">
            <ReadKnowledges/>
        </section>
        <section id="section-central">
            <component :is="stepsStore.getCurrentComponent"></component>
        </section>
        <!-- <section>
            <EvaluateQuestion/>
        </section> -->
    </div>
</template>

<style scoped>
    .experiment-container{
        display: grid;
        grid-template-columns: 1fr 3fr;
        gap: 24px;
    }
</style>