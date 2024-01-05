<template>
    <div>
        <h1 class="green">Detailed</h1>
        <br>
  
    <p>I am a skilled developer with broad experience.</p>
    <p>On personal level I have interest in art, photography, architecture, cooking and snowboarding and skateboarding .</p>
    <br>
    <p></p>
    <div class="q-pa-md">
    <q-carousel
      animated
      v-model="slide"
      arrows
      navigation
      infinite
    >
      <q-carousel-slide :name="1" img-src="src/assets/Scherm­afbeelding 2024-01-05 om 14.42.31.png" />
      <q-carousel-slide :name="2" img-src="src/assets/arhc.png" />
      <q-carousel-slide :name="3" img-src="src/assets/tm.png" />
    </q-carousel>
  </div>
  <br>
  </div>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    setup () {
      return {
        slide: ref(1)
      }
    }
  }
  </script>