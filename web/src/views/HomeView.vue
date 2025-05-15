<template>
  <main class="centered-main">
    <LanguageSelector v-model="language" :languages="SUPPORTED_LANGUAGES" />
    <div class="main-row">
      <div class="input-wrapper">
        <TextInput v-model="input" @validation-error="inputError = $event" />
      </div>
      <div class="response-wrapper">
        <ResponseDisplay :output="output" :error="error" />
      </div>
    </div>
  </main>
</template>

<script setup lang="ts">
import { ref, watch, watchEffect } from 'vue'
import TextInput from '@/components/TextInput.vue'
import ResponseDisplay from '@/components/ResponseDisplay.vue'
import LanguageSelector from '@/components/LanguageSelector.vue'
import { SUPPORTED_LANGUAGES } from '@/constants/languages'
import { fetchTranslation } from '@/services/api'

const input = ref('')
const inputError = ref('')
const language = ref(SUPPORTED_LANGUAGES[0].value)
const output = ref('')
const error = ref('')

let debounceTimeout: ReturnType<typeof setTimeout> | null = null

// Fetch translation when text changes after a debounce period
watchEffect(() => {
  if (debounceTimeout) clearTimeout(debounceTimeout)

  if (!input.value.trim() || inputError.value) {
    output.value = ''
    error.value = ''
    return
  }

  debounceTimeout = setTimeout(() => {
    triggerFetch()
  }, 1000)
})

// Immediately fetch when language changes
watch(language, () => {
  if (input.value.trim() && !inputError.value) {
    triggerFetch()
  }
})

async function triggerFetch() {
  if (inputError.value) return // Don't fetch if there is an input validation error
  try {
    const result = await fetchTranslation(input.value, language.value)
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
