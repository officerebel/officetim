<template>
  <div>
    <q-breadcrumbs class="q-mb-md">
      <q-breadcrumbs-el label="Home" to="/" />
      <q-breadcrumbs-el label="Blog" to="/blog" />
      <q-breadcrumbs-el :label="post?.title || '...'" />
    </q-breadcrumbs>

    <q-card v-if="post">
      <q-img v-if="post.image" :src="normalizedImage(post.image)" :ratio="16/9" class="q-img__cover"/>
      <q-card-section>
        <div class="text-subtitle2 green">{{ post.date }}</div>
        <div class="text-h5 green q-mt-xs">{{ post.title }}</div>
      </q-card-section>
      <q-separator />
      <q-card-section class="green" style="white-space: pre-line;">{{ post.body }}</q-card-section>
    </q-card>

    <q-skeleton v-else type="text" :width="'60%'" class="q-mb-sm" />
    <q-skeleton v-else type="text" :width="'90%'" />
  </div>
  </template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import { useRoute } from 'vue-router'
import { tryExceptAwait } from '@/utils'
import postApi from '@/api/posts.js'

const route = useRoute()
const post = ref(null)
const normalizedImage = (url) => (url ? url.replace(/^http:\/\//, 'https://') : '')

const load = async (id) => {
  const { status, data } = await tryExceptAwait(() => postApi.getPostById(id))
  if (status === 200) {
    post.value = data
  }
}

onMounted(() => load(route.params.id))
watch(() => route.params.id, (id) => id && load(id))
</script>

<style scoped>
</style>
