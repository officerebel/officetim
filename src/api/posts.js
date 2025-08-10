import { placeholderApi } from '@/api/index.js'

const basePath = 'posts/'

export default {
    async getPosts() {
        return await placeholderApi.get(basePath)
    },
    async getPostById(id) {
        return await placeholderApi.get(`${basePath}${id}/`)
    }
}

