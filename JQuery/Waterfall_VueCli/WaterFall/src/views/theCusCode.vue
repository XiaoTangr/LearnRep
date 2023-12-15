<template>
  <div>
    <AddItem></AddItem>
    <button @click="AddMyvalue"> add</button>
    <WaterFall :Number="myvalue"></WaterFall>
  </div>
</template>
<script setup lang="ts">
import AddItem from "@/components/CusCode/theAddItem.vue";
import WaterFall from "@/components/CusCode/theWaterFall.vue";

import { ref } from "vue";

const myvalue = ref(100);

const AddMyvalue = () => {
  myvalue.value++;
};
</script>

<style lang="scss" scoped></style>
