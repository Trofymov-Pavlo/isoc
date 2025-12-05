<template>
  <MainHeader />
  <SubHeader />
  <slot />
</template>

<script setup lang="ts">
import MainHeader from '@/components/header/mainHeader.vue'
import SubHeader from '@/components/header/sub_header.vue'
</script>


