
<template>
     <h1 class="green">Blog</h1>
    <p class="green">Here I will post my snippets blogs articles and inspiration</p>
    <br>
            <div v-for="post in posts.slice(0, 100)" :key="post.id">
              <q-card>
              <q-img v-if="post.image"
                  :src="normalizedImage(post.image)"
                  :ratio="16/9"
                  class="q-img__cover"/>
          <q-card-section>
              <div class="text-subtitle2 green ">  {{ post.date}}</div>
                            <div class="text-subtitle2 green ">  {{ post.date}}</div>
                            <router-link class="text-h6 green" :to="{ name: 'blog-detail', params: { id: post.id } }">
                                {{ post.title }}
                            </router-link>
          </q-card-section>
          
          <q-separator light />
          </q-card>
          <br>
      </div>
</template>

<script setup>
import {ref,onMounted} from 'vue'
import {tryExceptAwait} from '@/utils'
import postApi from '@/api/posts.js'

const posts = ref([])
const normalizedImage = (url) => {
    if (!url) return ''
    return url.replace(/^http:\/\//, 'https://')
}
onMounted(async ()=> {
    const {status,data} = await tryExceptAwait(
        postApi.getPosts
    )
    if (status === 200) {
        posts.value = data

    }
    console.log(status,data,'status','data')
})

</script>
