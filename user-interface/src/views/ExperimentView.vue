<script setup lang="ts">
import ReadKnowledges from '@/components/ReadKnowledges.vue';
import CollectKnowledge from '@/components/CollectKnowledge.vue';
//import EvaluateQuestion from '@/components/EvaluateQuestion.vue';
</script>

<template>
    <div class="experiment-container">
        <section id="section-left">
            <ReadKnowledges/>
        </section>
        <section id="section-central">
            <CollectKnowledge/>
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