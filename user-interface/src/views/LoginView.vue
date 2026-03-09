<script setup lang="ts">
    import router from '@/router/index' 
    import { BField, BInput, BButton, useToast } from "buefy";
    import { ref } from "vue"
    import { authAPI } from '@/services/api'
    
    const username = ref<string>("")
    const password = ref<string>("")

    const Toast = useToast()

    async function login() {
        try {
            const response = await authAPI.login(username.value, password.value)
            const { access_token, refresh_token } = response.data

            localStorage.setItem('access_token', access_token)
            localStorage.setItem('refresh_token', refresh_token)
            
            router.push({ path: '/experiment' })
        } catch (err){
            console.log(err)
            Toast.open({message: "Login failed", type: "is-danger"})
        }
    }
    
</script>

<template>
    <div class="container container-size">
            <b-field label="Username">
                <!-- @vue-ignore -->
                <b-input
                    v-model="username"
                    placeholder="Alice"
                    maxlength="20" 
                    required
                ></b-input>
            </b-field>
            <b-field label="Password">
                <!-- @vue-ignore -->
                <b-input
                    v-model="password"
                    maxlength="50"
                    type="password"
                    required
                ></b-input>
            </b-field>
            <b-button type="is-primary" @click="login">Login</b-button>
    </div>
</template>

<style scoped>
.container-size{
        flex: none;
        gap:0;
        width: 20rem;
        height: 20rem ;
    }
</style>