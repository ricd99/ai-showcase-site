import axios from "axios"

// Create instance of axios with base URL
const api = axios.create({
    baseURL: "http://localhost:8000" // url of backend
});

// Export Axios instance
export default api;