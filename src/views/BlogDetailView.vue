<template>
  <div class="post-container">
    <q-breadcrumbs class="q-mb-md breadcrumbs-left">
      <q-breadcrumbs-el label="Home" to="/" />
      <q-breadcrumbs-el label="Blog" to="/blog" />
      <q-breadcrumbs-el :label="post?.title || '...'" />
    </q-breadcrumbs>

  <q-card v-if="post" class="post-card full-width" :style="{ width: '100%' }">
      <q-img
        v-if="post.image"
        :src="normalizedImage(post.image)"
        :ratio="16/9"
    class="q-img__cover cursor-pointer header-image full-width"
    :style="{ width: '100%' }"
        @click="showImageDialog = true"
      />
      <q-card-section>
        <div class="text-subtitle2 green">{{ post.date }}</div>
        <div class="text-h5 green q-mt-xs">{{ post.title }}</div>
        <div class="q-mt-sm" v-if="tags.length">
          <q-chip
            v-for="tag in tags"
            :key="`tag-${tag}`"
            dense
            outline
            color="primary"
            text-color="primary"
            class="q-mr-xs q-mb-xs"
          >
            {{ tag }}
          </q-chip>
        </div>
      </q-card-section>
      <q-separator />
      <q-card-section class="green" style="white-space: pre-line;">{{ post.body }}</q-card-section>
    </q-card>

      <div v-else class="q-pa-md">
        <q-skeleton type="rect" height="200px" class="q-mb-md" />
        <q-skeleton type="text" :width="'60%'" class="q-mb-sm" />
        <q-skeleton type="text" :width="'90%'" />
      </div>

    <q-dialog v-model="showImageDialog" persistent maximized>
      <q-card class="bg-black">
        <div class="row items-center justify-end q-pa-sm">
          <q-btn dense round flat icon="close" color="white" @click="showImageDialog = false" />
        </div>
        <q-card-section class="q-pa-none">
          <q-img :src="normalizedImage(post?.image)" fit="contain" class="full-height-img" />
        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
  </template>

<script setup>
import { onMounted, ref, watch, computed } from 'vue'
import { useRoute } from 'vue-router'
import { tryExceptAwait } from '@/utils'
import postApi from '@/api/posts.js'

const route = useRoute()
const post = ref(null)
const showImageDialog = ref(false)
const normalizedImage = (url) => (url ? url.replace(/^http:\/\//, 'https://') : '')
const tags = computed(() => {
  const t = post.value?.tags
  if (!t) return []
  if (Array.isArray(t)) {
    if (t.length && typeof t[0] === 'object') {
      return t.map(x => x?.name || x?.title || x?.slug).filter(Boolean)
    }
    return t.map(x => (typeof x === 'string' ? x : String(x))).filter(Boolean)
  }
  if (typeof t === 'string') {
    return t.split(',').map(s => s.trim()).filter(Boolean)
  }
  return []
})

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
.full-height-img { height: calc(100vh - 56px); }
.breadcrumbs-left { display: flex; justify-content: flex-start; }
.post-container { width: 100%; padding: 0 16px; }
.post-card { width: 100% !important; max-width: 100% !important; display: block; }
.q-card.post-card { width: 100% !important; }
.header-image { width: 100% !important; display: block; }
</style>
