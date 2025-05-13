<template>
  <main class="centered-main">
    <LanguageSelector v-model="language" :languages="SUPPORTED_LANGUAGES" />
    <div class="main-row">
      <div class="input-wrapper">
        <TextInput v-model="text" />
      </div>
      <div class="response-wrapper">
        <ResponseDisplay :output="output" :error="error" />
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import TextInput from '@/components/TextInput.vue'
import ResponseDisplay from '@/components/ResponseDisplay.vue'
import LanguageSelector from '@/components/LanguageSelector.vue'
import { SUPPORTED_LANGUAGES } from '@/constants/languages'
import { fetchTranslation } from '@/services/api'

const text = ref('')
const language = ref(SUPPORTED_LANGUAGES[0].value)
const output = ref('')
const error = ref('')

let debounceTimeout: ReturnType<typeof setTimeout> | null = null

// Fetch translation when text changes after a debounce period
watch(text, () => {
  if (debounceTimeout) clearTimeout(debounceTimeout)

  debounceTimeout = setTimeout(() => {
    if (!text.value.trim()) {
      output.value = ''
      error.value = ''
      return
    }
    triggerFetch()
  }, 1000)
})

// Immediately fetch when language changes
watch(language, () => {
  if (text.value.trim()) {
    triggerFetch()
  }
})

async function triggerFetch() {
  try {
    const result = await fetchTranslation(text.value, language.value)
    output.value = result
    error.value = ''
  } catch (err) {
    output.value = ''
    error.value = (err as Error).message
  }
}
</script>

<style>
.centered-main {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  box-sizing: border-box;
  padding: 0 2rem;
  margin: 0 auto;
}
.main-row {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: flex-start;
  gap: 2rem;
}


</style>
