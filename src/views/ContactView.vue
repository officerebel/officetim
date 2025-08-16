<template>
  <div class="q-pa-md" style="max-width: 720px">
    <h1 class="green q-mb-md">Contact</h1>
    <p class="q-mb-lg">You can also reach me on <a href="https://twitter.com/timvogt" target="_blank" rel="noopener noreferrer"><u>Twitter</u></a>.</p>

    <q-form @submit.prevent="onSubmit" @reset.prevent="onReset" ref="formRef" class="q-gutter-md">
      <q-input v-model="form.name" label="Name" :rules="[v => !!v || 'Name is required']" dense outlined />
      <q-input v-model="form.email" label="Email" type="email" :rules="emailRules" dense outlined />
      <q-input v-model="form.subject" label="Subject" :rules="[v => !!v || 'Subject is required']" dense outlined />
      <q-input v-model="form.message" label="Message" type="textarea" autogrow :rules="[v => !!v || 'Message is required']" outlined />

      <div class="row q-col-gutter-sm items-center">
        <div class="col-auto">
          <q-btn color="primary" label="Send" type="submit" :loading="submitting" />
        </div>
        <div class="col-auto">
          <q-btn flat color="secondary" label="Reset" type="reset" :disable="submitting" />
        </div>
      </div>
    </q-form>

    <q-banner v-if="success" class="bg-positive text-white q-mt-md" rounded>
      Thank you! Your message has been sent.
    </q-banner>
    <q-banner v-if="error" class="bg-negative text-white q-mt-md" rounded>
      {{ error }}
    </q-banner>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import contactApi from '@/api/contact.js'

const formRef = ref(null)
const submitting = ref(false)
const success = ref(false)
const error = ref('')

const form = ref({
  name: '',
  email: '',
  subject: '',
  message: ''
})

const emailRules = [
  v => !!v || 'Email is required',
  v => /.+@.+\..+/.test(v) || 'Enter a valid email'
]

const onSubmit = async () => {
  error.value = ''
  success.value = false
  const ok = await formRef.value?.validate()
  if (!ok) return
  submitting.value = true
  try {
    const payload = { ...form.value }
    const { status } = await contactApi.send(payload)
    if (status === 200 || status === 201) {
      success.value = true
      form.value = { name: '', email: '', subject: '', message: '' }
      formRef.value?.resetValidation()
      // Redirect to thank you page
      window.location.assign('/contact/thank-you')
    } else {
      error.value = 'Failed to send. Please try again later.'
    }
  } catch (e) {
    error.value = e?.data?.detail || e?.statusText || 'Failed to send. Please try again later.'
  } finally {
    submitting.value = false
  }
}

const onReset = () => {
  form.value = { name: '', email: '', subject: '', message: '' }
  error.value = ''
  success.value = false
  formRef.value?.resetValidation()
}
</script>

<style scoped>
/* Keep it readable and aligned with other pages */
</style>