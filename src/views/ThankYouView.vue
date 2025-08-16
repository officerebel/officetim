<template>
  <div class="q-pa-md" style="max-width: 720px">
    <q-breadcrumbs class="q-mb-md">
      <q-breadcrumbs-el label="Home" to="/" />
      <q-breadcrumbs-el label="Contact" to="/contact" />
      <q-breadcrumbs-el label="Thank you" />
    </q-breadcrumbs>

    <q-card flat bordered>
      <q-card-section>
        <div class="text-h5 green">Thank you! Your message has been sent.</div>
        <div class="q-mt-sm">I'll get back to you soon.</div>
      </q-card-section>
      <q-separator />
      <q-card-actions>
        <q-btn color="primary" label="Back to Home" to="/" />
        <q-btn flat color="secondary" label="Contact again" to="/contact" />
      </q-card-actions>
    </q-card>
  </div>
</template>

<script setup>
</script>

<style scoped>
</style>
