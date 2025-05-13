<template>
  <select v-model="internalValue" @change="emit('update:modelValue', internalValue)">
    <option v-for="lang in languages" :key="lang.value" :value="lang.value">
      {{ lang.label }}
    </option>
  </select>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'

const props = defineProps<{
  modelValue: string
  languages: { label: string; value: string }[]
}>()

const emit = defineEmits<{
  (e: 'update:modelValue', value: string): void
}>()

const internalValue = ref(props.modelValue)

watch(
  () => props.modelValue,
  (val) => {
    internalValue.value = val
  },
)
</script>

<style scoped>
select {
  padding: 0.5rem;
  font-size: 1rem;
}
</style>
