<template>
  <div>
    <RouterTemplate></RouterTemplate>
    <RouterView></RouterView>
  </div>
</template>
<script setup lang="ts">
import { RouterLink, RouterView } from "vue-router";
import RouterTemplate from "@/components/Public/Router.vue";
</script>
<style scoped>
@media (min-width: 1024px) {
}
</style>
