import axios from "axios"
import type { AxiosResponse } from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_API_URL
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('access_token')
    if (token){
        config.headers.Authorization = `Bearer ${token}`
    }
    return config
})

export const authAPI = {
    register: (username: string, password: string)  => 
        api.post(
            '/api/v1/auth/register', 
            { "username":username, "plain_password":password }
        ),
    login: (username: string, password: string) => 
        api.post(
            '/api/v1/auth/login',
            new URLSearchParams({ username, password }),
            { headers: { 'Content-Type': 'application/x-www-form-urlencoded' }}
        ),
    getMe: () => api.get('/api/v1/auth/me')
}

export const isAuthenticated = async () => {
    try {
        const response: AxiosResponse = await authAPI.getMe()
    if (response.status==200)
        return true
    else 
        return false
    }
    catch{
        return false
    }
    
}

export default api;