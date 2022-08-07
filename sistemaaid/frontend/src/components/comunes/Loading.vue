<template>
    <vue-element-loading :active="show" spinner="bar-fade-scale" />
</template>

<script>
import VueElementLoading from "vue-element-loading";
//import 'vue-loading-overlay/dist/vue-loading.css';

export default {
    data() {
    return {
    }
    },
    components: {
    VueElementLoading
    },
    props: {
        show: Boolean
    }
}
</script>