<script setup lang="ts">
    import { BField, BInput, BButton, useToast } from "buefy";
    import { apiClient } from "@/services/api";
    import { ref } from "vue";

    import type { Knowledge } from "@/types/types";
    import { useStepStore } from '@/stores/step'
    import { useItemStore } from '@/stores/item'

    const stepStore = useStepStore()
    const itemStore = useItemStore()

    const knowledgeModel = ref<string>("")
    const uriModel = ref<string>("")
    
    const Toast = useToast()

    async function postKnowledge(){
        const knowledge: Knowledge = {
            id: null,
            content: knowledgeModel.value,
            uri: uriModel.value
        }
        if(validation(knowledge)){
            try {
                const response: Knowledge = await apiClient.post("api/v1/knowledges/", knowledge)
                Toast.open({message: "Knowledge collected", type: "is-success"})
                itemStore.$patch({ knowledge:response })
                stepStore.nextStep()
            }
            catch {
                Toast.open({message: "Data entry error", type: "is-danger"})
            }
        }
    }

    function validation(knowledge: Knowledge){
        return knowledge.content && knowledge.uri
    }

</script>

<template>
<div class="container">
    <h2>Collect Knowledge</h2>
    <b-field label="Knowledge">
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
            <b-button type="is-primary" @click="postKnowledge" >Share</b-button>
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