<script setup lang="ts">
    import { reactive, onMounted, onBeforeMount } from "vue"
    import api from "@/services/api"
    import { BButton } from "buefy"
    import { identifyProcessStep, ProcessStep }from "@/services/knowledgeWorklow"
    
    import type { AxiosResponse } from "axios"
    import type { Knowledge } from "@/types/types"

    import { useStepStore } from '@/stores/step'
    import { useItemStore } from '@/stores/item'

    const stepStore = useStepStore()
    const itemStore = useItemStore()

    interface KnowledgesWorkflow {
        knowledge: Knowledge,
        processStep: ProcessStep,
        isSelected: boolean
    }

    const knowledgesWorkflow = reactive<KnowledgesWorkflow[]>([])

    async function getKnowledges(): Promise<Knowledge[]>{
        const response: AxiosResponse<Knowledge[]> = await api.get("api/v1/knowledges/")
        return response.data
    }

    function truncateString(str: string){
        return (str.length <= 18) ? str : str.slice(0, 9) + "..." + str.slice(-9)
    }
    
    async function initializeKnowledgeWorkflow(){
        const knowledges: Knowledge[] = await getKnowledges()
        knowledges.forEach(async (knowledge) => {
            const kWorkflow: KnowledgesWorkflow = {
                knowledge,
                processStep: await identifyProcessStep(knowledge as Knowledge),
                isSelected: false
            }
            knowledgesWorkflow.push(kWorkflow)
        })
    }

    async function getKnowledgeWorkflow(){
        if(knowledgesWorkflow.length == 0){
            initializeKnowledgeWorkflow()
        } else {
            const knowledges: Knowledge[] = await getKnowledges()

            knowledges.forEach(async (knowledge) => {
                const kWorkflow: KnowledgesWorkflow = {
                    knowledge,
                    processStep: await identifyProcessStep(knowledge as Knowledge),
                    isSelected: false
                }

                const indexKW = knowledgesWorkflow.findIndex((kW: KnowledgesWorkflow) => kW.knowledge.id === knowledge.id)
                indexKW != -1 ? knowledgesWorkflow[indexKW] = kWorkflow : knowledgesWorkflow.push(kWorkflow)
            })
        }
    }

    onBeforeMount(() => getKnowledgeWorkflow())

    onMounted(()=>{
        setInterval(() => getKnowledgeWorkflow(), 10000)
    })

    function goToEvaluateQuestion(knowledge_data: Knowledge){
        itemStore.$patch({ knowledge: knowledge_data })
        stepStore.goToStep(ProcessStep.EvaluateQuestion)
    }

    function goToCollectKnowledge(){
        stepStore.goToStep(ProcessStep.CollectKnowledge)
    }

</script>

<template>
    <div class="container">
        <h2>Connaissances</h2>
        <ul>
            <li v-for="(kW, index) in knowledgesWorkflow" :key="index" class="list-element">
                <div class="list-element-index">
                    {{ index + 1 }}
                </div>
                <div class="list-element-body">
                    <span class="list-element-text">
                        {{ truncateString(kW.knowledge.uri) }}
                    </span>
                    
                    <!-- <b-button v-if="kW.processStep == ProcessStep.CollectKnowledge" type="is-primary" @click="goTo" >
                        Collect
                    </b-button> -->
                    <b-button v-if="kW.processStep == ProcessStep.WaitGeneration" type="is-info is-light" loading >
                        ...
                    </b-button>
                    <b-button v-if="kW.processStep == ProcessStep.EvaluateQuestion" type="is-warning" @click="goToEvaluateQuestion(kW.knowledge)" >
                        Evaluer
                    </b-button>
                    <b-button v-if="kW.processStep == ProcessStep.ProcessDone" type="is-success is-light" disabled >
                        Fait
                    </b-button>
                </div>
            </li>
            <li >
                <b-button type="is-primary" outlined @click="goToCollectKnowledge()" >
                        Ajouter une connaissance
                </b-button>
            </li>
        </ul>
    </div>
</template>

<style scoped>
    .container{
        background-color: #ffffff;
        border-radius: 16px;
        padding: 34px;
    }
    .list-element{
        margin-bottom: 8px;

        border: 1px solid #D6D9E0;
        border-radius: 8px;

        display: grid;
        grid-template-columns: 40px 1fr;

    }
    .list-element-index{
        display: flex;
        justify-content: center;
        align-items: center;
        border-right: 1px solid #D6D9E0;
    }
    .list-element-body{
        display: grid;
        grid-template-columns: 66% 34%;
    }
    .list-element-text{
        display: flex;
        align-items: center;
        padding-left: 12px;
    }
</style>