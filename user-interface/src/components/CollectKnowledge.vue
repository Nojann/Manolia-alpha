<script setup lang="ts">
    import { BField, BInput, BButton, useToast } from "buefy"
    import api from "@/services/api"
    import type { AxiosResponse } from "axios"
    import { ref } from "vue"

    import type { Knowledge, KnowledgeCreate } from "@/types/types"
    import { useStepStore } from '@/stores/step'
    import { useItemStore } from '@/stores/item'


    const stepStore = useStepStore()
    const itemStore = useItemStore()

    const knowledgeModel = ref<string>("")
    const uriModel = ref<string>("")
    
    const Toast = useToast()

    async function postKnowledge(){
        const knowledge: KnowledgeCreate = {
            content: knowledgeModel.value,
            uri: uriModel.value
        }
        if(validation(knowledge)){
            try {
                const response: AxiosResponse = await api.post("api/v1/knowledges/", knowledge)
                const knowledge_data: Knowledge = response.data
                Toast.open({message: "Knowledge collected", type: "is-success"})
                itemStore.$patch({ knowledge: knowledge_data })
                stepStore.nextStep()
            }
            catch {
                Toast.open({message: "Data entry error", type: "is-danger"})
            }
        }
    }

    function validation(knowledge: KnowledgeCreate){
        return knowledge.content && knowledge.uri
    }

</script>

<template>
<div class="container">
    <h2>Ajouter une connaissance</h2>
    <b-field label="Connaissance">
    <!-- @vue-ignore -->
    <b-input
        v-model="knowledgeModel"
        placeholder="Knowledge is an awareness of facts, a familiarity with individuals and situations, or a practical skill."
        maxlength="1200" 
        type="textarea" 
        required
        ></b-input>
    </b-field>
    <b-field label="URI">
        <!-- @vue-ignore -->
        <b-input 
            v-model="uriModel" 
            placeholder="en.wikipedia.org/wiki/Knowledge"
            maxlength="100"
            required
        ></b-input>
    </b-field>
    <div class="btn-container">
        <b-field>
        <div class="control">
            <b-button type="is-primary" @click="postKnowledge" >Partager</b-button>
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