<template>
<q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-brown">

            <q-toolbar class="bg-brown">
                <q-btn flat @click="drawer = !drawer" round dense icon="menu" />

                <q-toolbar-title >

                    <div class="nav">
                        <router-link to="/">
                        <img src="@/assets/OfficeTim.png" alt="OfficeTim logo">
                            </router-link>
                    </div>
                </q-toolbar-title>

        <q-drawer
                v-model="drawer"
                behavior = "mobile"
                show-if-above
                :width="200"
                :breakpoint="500"
                class="bg-brown"
        >
            <q-scroll-area class="fit">
                <q-list padding class="menu-list">


                    <q-item clickable v-ripple>
                        <q-item-section>
                            <RouterLink class="nav" to="/">Home </RouterLink>
                        </q-item-section>
                    </q-item>

                    <q-item active clickable v-ripple>
                        <RouterLink class="nav" to="/about">
                           About </RouterLink>
                    </q-item>

                    <q-item clickable v-ripple>
                        <q-item-section>
                            <RouterLink class="nav" to="/blog">Blog </RouterLink>
                        </q-item-section>
                    </q-item>

                    <q-item clickable v-ripple>
                        <q-item-section>
                            <RouterLink class="nav" to="/contact">Contact </RouterLink>
                        </q-item-section>
                    </q-item>
                </q-list>
            </q-scroll-area>
        </q-drawer>
            </q-toolbar>
    </q-header>
    <q-page-container>
        <q-page>
            <router-view />
        </q-page>

    </q-page-container>


    <q-footer elevated class="bg-grey-8 text-white">
        <q-toolbar>
            <q-toolbar-title>
                <q-avatar>
                </q-avatar>
                <div>OfficeTim</div>
            </q-toolbar-title>
        </q-toolbar>
    </q-footer>
</q-layout>

</template>


<style lang="sass" scoped>
.my-card
  width: 100%
  max-width: 250px

</style>

<style>
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
}

.logo img {
  width: 100px;
}

nav ul {
  display: flex;
  list-style: none;
}

nav li {
  margin-left: 1rem;
}

nav a {
  text-decoration: none;
  color: #333;
  font-weight: bold;
}

nav a:hover {
  color: #666;
}

p { font-size:20px;
}
</style



>
<script setup>
</script>


<script>
import { ref } from 'vue'

export default {
    setup () {
        return {
            drawer: ref(false)
        }
    }
}
</script>