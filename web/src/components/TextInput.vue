<template>
  <div class="text-input-wrapper">
    <textarea
      v-model="internalText"
      @input="onInput"
      placeholder="Add your text to translate here"
      rows="5"
      cols="40"
    />
    <div class="helper-text">
      <p>{{ internalText.length }} / {{ maxLength }}</p>
      <p v-if="error" class="error-text">{{ error }}</p>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{ modelValue: string }>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const internalText = ref(props.modelValue)
const error = ref('')
const maxLength = 500

const VALID_TEXT_REGEX = /^[\w\d\s.,!?¿¡'"-]*$/

watch(
  () => props.modelValue,
  (newVal) => {
    internalText.value = newVal
  },
)

function onInput() {
  // Restore error value
  error.value = ''

  // Truncate if necessary. Prevent exceeding maxLength
  if (internalText.value.length > maxLength) {
    internalText.value = internalText.value.slice(0, maxLength)
  }

  let value = internalText.value

  if (!VALID_TEXT_REGEX.test(value)) {
    error.value = 'Text contains invalid characters'
    // Restore translation result value
    value = ''
  }

  emit('update:modelValue', value)
}
</script>

<style scoped>
.text-input-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

textarea {
  font-size: 1rem;
  padding: 0.5rem;
  box-sizing: border-box;
}

.helper-text {
  display: flex;
  width: 100%;
  flex-direction: row;
  justify-content: space-between;
  margin-top: 0.25rem;
  font-size: 0.9rem;
}

.error-text {
  color: red;
}
</style>
