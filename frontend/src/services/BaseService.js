import axios from 'axios'

class BaseService {
    constructor() {
        this.client = axios.create({
            baseURL: process.env.VUE_APP_API_URL
        })
    }
}

export default BaseService