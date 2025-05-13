<template>
  <div class="response">
    <p v-if="error" class="error">⚠️ {{ error }}</p>
    <p v-else-if="output">✅ {{ output }}</p>
    <p v-else class="placeholder">The translation result will appear here.</p>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  output: string
  error: string
}>()
</script>

<style scoped>
.response {
  margin-top: 1rem;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
}
.error {
  color: red;
}
.placeholder {
  color: #888;
}
</style>
