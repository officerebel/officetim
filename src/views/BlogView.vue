
<template>
     <h1 class="green">Blog</h1>
    <p class="green">Here I will post my snippets blogs articles and inspiration</p>
    <br>
      <div v-for="post in posts.slice(0, 100)">
          <q-card>
          <q-card-section>
              <div class="text-subtitle2 green ">  {{ post.date}}</div>
              <div class="text-subtitle2 green ">  {{ post.date}}</div>
              <div class="text-h6 green ">{{ post.title }}</div>
          </q-card-section>
          <q-card-section class="green">
              {{ post.body}}
<!--              <q-btn label="read more" ></q-btn>-->
              <router-view></router-view>
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
