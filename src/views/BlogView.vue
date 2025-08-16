
<template>
     <h1 class="green">Blog</h1>
    <p class="green">Here I will post my snippets blogs articles and inspiration</p>
    <br>
        <q-banner v-if="error" class="bg-negative text-white q-mb-md" rounded>
            {{ error }}
            <q-btn flat color="white" class="q-ml-sm" label="Retry" @click="load" :loading="loading" />
        </q-banner>
        <q-skeleton v-if="loading" type="rect" height="180px" class="q-mb-md" />
        <!-- Tag filter bar -->
        <div v-if="allTags.length" class="q-mb-md">
            <q-chip
                clickable
                :outline="!!selectedTag"
                color="primary"
                text-color="primary"
                class="q-mr-xs q-mb-xs"
                @click="clearFilter"
            >All</q-chip>
            <q-chip
                v-for="tag in allTags"
                :key="`filter-${tag}`"
                clickable
                :color="selectedTag === tag ? 'primary' : undefined"
                :text-color="selectedTag === tag ? 'white' : 'primary'"
                :outline="selectedTag !== tag"
                class="q-mr-xs q-mb-xs"
                @click="selectTag(tag)"
            >{{ tag }}</q-chip>
        </div>

                                                <div v-if="!loading && !error && !filteredPosts.length" class="q-mb-md">
                                                        <q-banner class="bg-grey-8 text-white" rounded>
                                                                No posts to show.
                                                                <template v-if="selectedTag">
                                                                    <q-btn flat color="white" class="q-ml-sm" label="Clear filter" @click="clearFilter" />
                                                                </template>
                                                        </q-banner>
                                                </div>
                                                <div v-for="post in filteredPosts" :key="post.id">
              <q-card>
              <q-img v-if="post.image"
                  :src="normalizedImage(post.image)"
                  :ratio="16/9"
                  class="q-img__cover"/>
          <q-card-section>
              <div class="text-subtitle2 green ">  {{ post.date}}</div>
                            <router-link class="text-h6 green" :to="{ name: 'blog-detail', params: { id: post.id } }">
                                {{ post.title }}
                            </router-link>
                        <div class="q-mt-sm" v-if="getTags(post).length">
                            <q-chip
                                v-for="tag in getTags(post)"
                                :key="`${post.id}-tag-${tag}`"
                                dense
                                outline
                                color="primary"
                                text-color="primary"
                                class="q-mr-xs q-mb-xs"
                                clickable
                                @click="selectTag(tag)"
                            >
                                {{ tag }}
                            </q-chip>
                        </div>
          </q-card-section>
          
          <q-separator light />
          </q-card>
          <br>
      </div>
</template>

<script setup>
import {ref,onMounted,computed,watch} from 'vue'
import { useRoute, useRouter } from 'vue-router'
import {tryExceptAwait} from '@/utils'
import postApi from '@/api/posts.js'

const posts = ref([])
const loading = ref(false)
const error = ref('')
const selectedTag = ref('')
const route = useRoute()
const router = useRouter()
const normalizedImage = (url) => {
    if (!url) return ''
    return url.replace(/^http:\/\//, 'https://')
}
const getTags = (post) => {
    const t = post?.tags
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
}
const allTags = computed(() => {
    const set = new Set()
    posts.value.forEach(p => getTags(p).forEach(t => set.add(t)))
    return Array.from(set).sort()
})
const filteredPosts = computed(() => {
    const tag = selectedTag.value?.trim()
    const list = posts.value.slice(0, 100)
    if (!tag) return list
    return list.filter(p => getTags(p).includes(tag))
})
const selectTag = (tag) => {
    selectedTag.value = tag
}
const clearFilter = () => {
    selectedTag.value = ''
}
onMounted(async ()=> {
        // initialize from URL
        if (typeof route.query.tag === 'string') {
            selectedTag.value = route.query.tag
        }
        await load()
})

// sync URL with selection
watch(selectedTag, (t) => {
    const q = { ...route.query }
    if (t) q.tag = t
    else delete q.tag
    router.replace({ query: q })
})

    async function load() {
        loading.value = true
        error.value = ''
        const {status, data} = await tryExceptAwait(
            postApi.getPosts
        )
        if (status === 200) {
            posts.value = data
        } else {
            posts.value = []
            error.value = `Could not load posts (status ${status || 'unknown'}).`
        }
        loading.value = false
    }

</script>
