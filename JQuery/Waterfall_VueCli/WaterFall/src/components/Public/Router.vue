<template>
  <div>
    <RouterView>
      <RouterLink to="/">代码实现</RouterLink>
      <RouterLink to="/PluginsCode">插件实现</RouterLink>
    </RouterView>
  </div>
</template>

<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
</script>

<style scoped></style>