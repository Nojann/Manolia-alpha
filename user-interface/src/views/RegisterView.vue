<script setup lang="ts">
    import router from '@/router/index' 
    import { BField, BInput, BButton, useToast } from "buefy";
    import { ref } from "vue"
    import { authAPI } from '@/services/api'
    
    const username = ref<string>("")
    const password = ref<string>("")

    const Toast = useToast()

    async function register() {
        try {
            const responseRegister = await authAPI.register(username.value, password.value)
            if(responseRegister.status != 200)
                throw new Error("Registred failed")
            const responseLogin = await authAPI.login(username.value, password.value)
            const { access_token, refresh_token } = responseLogin.data

            localStorage.setItem('access_token', access_token)
            localStorage.setItem('refresh_token', refresh_token)
            
            router.push({ path: '/experiment' })
        } catch (err){
            console.log(err)
            Toast.open({message: "Registred failed", type: "is-danger"})
        }
    }
    
</script>

<template>
    <div class="container">
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
            <b-button type="is-primary" @click="register">Register</b-button>
    </div>
</template>

<style scoped>
.container{
        width: 20%;
        background-color: #ffffff;
        border-radius: 16px;
        padding: 34px;
    }
</style>