<script setup lang="ts">
    import { ref } from "vue";
    import { onBeforeMount } from 'vue'
    import type { Knowledge } from "@/types/types";
    import type { Question } from "@/types/types";
    import type { Metric } from "@/types/types";

    //import { useStepStore } from '@/stores/step'
    import { useItemStore } from '@/stores/item'

    import { apiClient } from "@/services/api";

    //const stepStore = useStepStore()
    const itemStore = useItemStore()

    const questions = ref<Question[]>()
    const metrics = ref<Metric[]>([])

    onBeforeMount(async () => {
        if(itemStore.knowledge != undefined){
            questions.value = await getQuestions(itemStore.knowledge)
        }
        else{
            throw new Error("There is no knowledge element in itemStore.");
        }
        if(questions.value != undefined){
            initializeMetrics(questions.value)
        }
        else{
            throw new Error("There is no questions element from API.");
        }

    })

    async function getQuestions(knowledge: Knowledge): Promise<Question[]>{
        return apiClient.get(`api/v1/knowledges/${knowledge.id}/questions`)
    }

    function initializeMetrics(questions: Question[]){
        questions.forEach((q)=>{
              const metric: Metric = {
                //id: null,
                question_id: q.id!,
                need_index: -1
            }
            metrics.value!.push(metric)
        })
    }

    function getIndexMetrics(question: Question){
        if(metrics.value != undefined){
            return metrics.value.findIndex((metric) => metric.question_id === question.id)
        }
        else{
            throw new Error("The is no metrics element");
        }
    }

    async function postMetrics(){
        console.log(metrics.value)
        metrics.value?.forEach(async (metric) => {
            await apiClient.post(`api/v1/metrics/`, metric)
        })
    }
</script>

<template>
    <div class="container">
        <h2>Evaluate Questions</h2>
        <ul>
            <li v-for="(question, index) in questions" :key="index">
                <p>{{ question.question }}</p>
                <b-field>
                    <b-slider v-model="metrics![getIndexMetrics(question)]!.need_index"></b-slider>
                </b-field>
            </li>
        </ul>
        <div class="btn-container">
            <b-field>
            <div class="control">
                <b-button type="is-primary" @click="postMetrics" >Share</b-button>
            </div>
            </b-field>
        </div>
    </div>
</template>

<style scoped>
    .container{
        background-color: #ffffff;
        border-radius: 16px;
        padding: 34px;
    }
    .btn-container{
            display: flex;
            justify-content: end;
        }
</style>