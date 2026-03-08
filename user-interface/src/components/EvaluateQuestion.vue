<script setup lang="ts">
    import { onBeforeMount, ref, watch } from "vue";

    import type { Knowledge, Question, MetricCreate, Metric } from "@/types/types"

    import { useStepStore } from '@/stores/step'
    import { useItemStore } from '@/stores/item'

    import api from "@/services/api"
    import type { AxiosResponse } from "axios";

    const stepStore = useStepStore()
    const itemStore = useItemStore()

    const questions = ref<Question[]>()
    const metrics = ref<Metric[]>([])

    onBeforeMount(async () => {
        if(!itemStore.knowledge){
            throw new Error("There is no knowledge element in itemStore.");
        }
        questions.value = await getQuestions(itemStore.knowledge)

        if(!questions.value){
            throw new Error("There is no questions element from API.");
        }
        initializeMetrics(questions.value)
    })

    watch( () => itemStore.knowledge, async () =>{
        metrics.value = []
        if(!itemStore.knowledge){
            throw new Error("There is no knowledge element in itemStore.");
        }
        questions.value = await getQuestions(itemStore.knowledge)

        if(!questions.value){
            throw new Error("There is no questions element from API.");
        }
        initializeMetrics(questions.value)
    })

    async function getQuestions(knowledge: Knowledge): Promise<Question[]>{
        const response: AxiosResponse = await api.get(`api/v1/knowledges/${knowledge.id}/questions`)
        const questions: Question[] = response.data
        return questions
    }

    function initializeMetrics(questions: Question[]){
        questions.forEach((q)=>{
              const metric: Metric = {
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
            throw new Error("The is no metrics element")
        }
    }

    async function postMetrics(){
        console.log( metrics.value)
        metrics.value?.forEach(async (metric) => {
            const metricCreate: MetricCreate = { need_index: metric.need_index }
            const response = await api.post(`api/v1/questions/${metric.question_id}/metrics`, metricCreate)
            // eslint-disable-next-line @typescript-eslint/no-unused-vars
            const metric_data = response.data
        })
        stepStore.nextStep()
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
                <b-button type="is-primary" @click="postMetrics" >Partager</b-button>
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