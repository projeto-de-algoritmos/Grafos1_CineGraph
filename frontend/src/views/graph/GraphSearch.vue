
<template>
    <section>
        <v-autocomplete
            v-model="search"/>
    </section>
</template>

<script>
export default {
    data: () => ({
        search: []
    })
}
</script>