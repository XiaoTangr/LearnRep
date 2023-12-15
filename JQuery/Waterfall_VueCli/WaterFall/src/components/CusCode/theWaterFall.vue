<template>
  <div>{{ Number }}</div>
</template>

<script setup lang="ts">

import { reactive, ref } from "vue";
defineProps({
    Number:{
        type:Number,
        default:1
    }
})
</script>

<style scoped></style>
