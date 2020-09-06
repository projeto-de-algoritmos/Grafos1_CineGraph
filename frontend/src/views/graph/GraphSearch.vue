
<template>
    <section>
        <v-autocomplete
            v-model="model"
            :items="entries"
            :loading="isLoading"
            :search-input.sync="search"
            hide-no-data
            hide-selected
            @change="getActor"
            item-text="name"
            item-value="id"
            label="Ator/Atriz"
            placeholder="Digite para inicar a busca"
            prepend-icon="mdi-database-search">
            <template v-slot:item="data">
                <template v-if="data.item">
                    <v-list-item-avatar>
                        <img :src="data.item.headshot" style="object-fit: cover;">
                    </v-list-item-avatar>
                    <v-list-item-content>
                        <v-list-item-title v-html="data.item.name"></v-list-item-title>
                    </v-list-item-content>
                </template>
            </template>
        </v-autocomplete>
    </section>
</template>

<script>
import ActorService from "../../services/ActorService"

const actorService = new ActorService()

export default {
    data: () => ({
        entries: [],
        isLoading: false,
        model: "",
        search: null,
    }),
    methods: {
        getActor(value) {
            this.$emit('selectedActor', value)
        }
    },
    watch: {
        search (val) {
            if (val && val.length >= 3) {
                this.isLoading = true
    
                // Lazily load input items
                actorService.getActorListByName(val)
                    .then(res => res.data)
                    .then(data => {
                        this.entries = data
                    })
                    .catch(err => {
                        console.log(err)
                    })
                    .finally(() => (this.isLoading = false))
            }
            else {
                this.entries = []
                this.model = ""
            }
      },
    }
}
</script>