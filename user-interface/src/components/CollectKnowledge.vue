<script setup lang="ts">
    import { BField, BInput, BButton } from "buefy";
    import { apiClient } from "@/services/api";

    let knowledgeText = ""
    function postKnowledge(){
        let knowlegde = {
            content: knowledgeText,
            uri: "wiki"
        }
        apiClient.post("api/v1/knowledges/", knowlegde)
    }
</script>

<template>
<div class="container">
    <h2>Collect Knowledge</h2>
    <b-field label="Knowledge">
         <b-input maxlength="1200" type="textarea" v-model="knowledgeText"></b-input>
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