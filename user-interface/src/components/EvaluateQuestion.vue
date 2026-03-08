<script setup lang="ts">
    import { onBeforeMount, ref, watch } from "vue";

    import type { Knowledge, Question, MetricCreate, Metric } from "@/types/types"
    import { BCollapse, BSlider } from "buefy";

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
        <div class="title-container">
            <div class="title-icon">
                <img src="../assets/svg/message-circle-star.svg" alt="evaluate icon" />
            </div>
            <h2>Evaluer les questions</h2>
        </div>
        <div>
            <ul class="list">
                <li class="list-item">
                    <span class="list-index">1</span>
                    <p>Un ensemble de questions a été généré à partir d'une connaissance que vous avez saisie (ci-dessous).</p>
                </li>
                <li class="list-item">
                    <span class="list-index">2</span>
                    <p>Mise en situation : si vous deviez vous adresser à une personne capable d'améliorer la connaissance incertaine, la question générée serait-elle pertinente ?</p>
                </li>
                <li class="list-item">
                    <span class="list-index">3</span>
                    <p>Evaluez de 0 à 100, pour chaque question, la pertinence de celle-ci.</p>
                </li>
            </ul>
        </div>
        <b-collapse class="card" animation="slide" aria-id="contentIdForA11y3">
            <template #trigger="props">
                <div
                    class="card-header"
                    role="button"
                    aria-controls="contentIdForA11y3"
                    :aria-expanded="props.open"
                >
                    <p class="card-header-title">Connaissance</p>
                    <a class="card-header-icon">
                        {{ props.open ? "▲" : "▼" }}
                    </a>
                </div>
            </template>

            <div class="card-content">
                <div class="content">
                    {{ itemStore.knowledge?.content }}
                </div>
            </div>
        </b-collapse>
        <ul class="question-list">
            <li v-for="(question, index) in questions" :key="index" class="question-list-item">
                <div class="question">
                    <img src="../assets/svg/question-mark.svg" alt="question-mark " />
                    {{ question.question }}
                </div>
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
    .btn-container{
            display: flex;
            justify-content: end;
        }
    .list{
        padding-left: 24px;
        display: flex;
        flex-direction: column;
        gap: 16px;
    }
    .list-item{
        display: flex;
        flex-direction: raw;
        align-items: center;
        gap: 8px;
    }
    .list-index{
        display: flex;
        justify-content: center;
        align-items: center;
        width: 24px;
        height: 24px;
        border: 1px solid #D6D9E0;
        border-radius: 4px;
    }
    .card-header{
        box-shadow: none;
    }
    .card{
        box-shadow: none;
        border: 1px solid #D6D9E0;
    }
    .question-list{
        display: flex;
        flex-direction: column;
        gap: 12px;
    }
    .question-list-item{
        padding: 24px;
        border: 1px solid #D6D9E0;
        border-radius: 16px;
    }
    .question{
        background-color: #ebebeb;
        display: flex;
        align-items: center;
        gap: 8px;
        padding: 8px;
        border-radius: 4px;
        img{
            border-right: 1px solid;
        }
    }
</style>