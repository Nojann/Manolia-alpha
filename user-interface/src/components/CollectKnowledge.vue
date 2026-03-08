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
    <div class="title-container">
        <div class="title-icon">
            <img src="../assets/svg/file-import.svg" alt="file import" />
        </div>
        <h2>Collecter une connaissance</h2>
    </div>
    <div class="body-container">
        <div>
            <ul class="list">
                <li class="list-item">
                    <span class="list-index">1</span>
                    <p>Dans votre base de connaissances, identifiez un texte contenant de l'incertitude.</p>
                </li>
                <li class="list-item">
                    <span class="list-index">2</span>
                    <p>Selectionnez la partie du texte qui nécessite des précisions et copiez/coller vers le formulaire.</p>
                </li>
                <li class="list-item">
                    <span class="list-index">3</span>
                    <p>Selectionnez l'URI où se trouve la connaissance et copiez/coller vers le formulaire.</p>
                </li>
                <li class="list-item">
                    <span class="list-index">4</span>
                    <p>Partager via le formulaire.</p>
                </li>
            </ul>
        </div>
        <div class="form">
            <b-field label="Connaissance">
            <!-- @vue-ignore -->
            <b-input
                v-model="knowledgeModel"
                placeholder="La connaissance est une notion aux sens multiples, à la fois utilisée dans le langage courant et objet d'étude poussée de la part des sciences cognitives et des philosophes contemporains."
                maxlength="1200" 
                type="textarea" 
                required
                ></b-input>
            </b-field>
            <b-field label="URI">
                <!-- @vue-ignore -->
                <b-input 
                    v-model="uriModel" 
                    placeholder="fr.wikipedia.org/wiki/Connaissance"
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
    </div>
</div>

</template>

<style scoped>
    .body-container{
        display: flex;
        flex-direction: column;
        gap: 48px;
    }
    .btn-container{
        height: 100%;
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
    .form{
        border: 1px solid #D6D9E0;
        padding: 24px;
        border-radius: 16px;
    }

</style>