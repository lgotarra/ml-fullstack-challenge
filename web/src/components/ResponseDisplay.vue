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
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  box-sizing: border-box;
  height: 7rem;
  width: 20rem;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.error,
.placeholder {
  margin: 0;
  padding: 0;
}

.placeholder {
  color: #888;
}

.error {
  color: red;
}
</style>
