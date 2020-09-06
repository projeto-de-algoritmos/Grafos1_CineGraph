
<template>
    <section>
        <v-container>
            <GraphSearch
                @selectedActor="changeCurrentActor"/>
            
            <GraphRender 
                :actor="selectedActor"/>
        </v-container>
    </section>
</template>

<script>
import GraphSearch from "./graph/GraphSearch"
import GraphRender from "./graph/GraphRender"

export default {
    data: () => ({
        selectedActor: ""
    }), 
    components: {
        GraphSearch,
        GraphRender
    },
    methods: {
        changeCurrentActor(value) {
            this.selectedActor = value
        }
    }
}
</script>