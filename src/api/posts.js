import { placeholderApi } from '@/api/index.js'

const basePath = 'posts/posts/'

export default {
    async getPosts() {
        return await placeholderApi.get(basePath)
    }
}

