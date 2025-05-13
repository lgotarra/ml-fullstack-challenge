<template>
  <textarea
    v-model="internalText"
    @input="onInput"
    placeholder="Add your text to translate here"
    rows="5"
    cols="40"
  />
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{ modelValue: string }>()
const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const internalText = ref(props.modelValue)

watch(
  () => props.modelValue,
  (newVal) => {
    internalText.value = newVal
  },
)

function onInput() {
  emit('update:modelValue', internalText.value)
}
</script>

<style scoped>
textarea {
  width: 100%;
  font-size: 1rem;
  padding: 0.5rem;
}
</style>
