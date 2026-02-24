<script setup lang="ts">
    import { BField, BInput, BButton, useToast } from "buefy";
    import { apiClient } from "@/services/api";
    import { ref } from "vue";

    import type { Knowledge } from "@/types/types";

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
                await apiClient.post("api/v1/knowledges/", knowledge)
                Toast.open({message: "Knowledge collected", type: "is-success"})
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
            maxlength="1200" 
            type="textarea" 
            required
            ></b-input>
    </b-field>
    <b-field label="URI">
        <!-- @vue-ignore -->
        <b-input 
            v-model="uriModel" 
            maxlength="100"
            required
        ></b-input>
    </b-field>
    <b-button type="is-primary" @click="postKnowledge" >Submit</b-button>
</div>

</template>

<style scoped>
.container{
    background-color: #ffffff;
    border-radius: 16px;
    padding: 34px;
}

</style>