<template>
<div>
    {{ message }}
</div>

</template> 

<script setup lang="ts">
import { compileString } from 'sass';

const props = defineProps({
    message: String
})

</script>