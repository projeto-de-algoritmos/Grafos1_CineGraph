
<template>
    <section 
        class="px-3"
        id="search-graph">
        <v-text-field
            v-model="actorLimit"
            label="Número limite de atores por filme"
            placeholder="Evite colocar um número muito alto."
            min="5"
            max="50">

        </v-text-field>

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

        <GraphItemDetails 
            :type="type"
            :item-id="itemId" />

    </section>
</template>

<script>
import ActorService from "../../services/ActorService"
import GraphItemDetails from "./GraphItemDetails"

const actorService = new ActorService()

export default {
    props: {
        itemId: {
            type: String,
            required: false,
            default: ""
        },
        type: {
            type: String,
            required: false,
            default: ""
        }
    },
    components: {
        GraphItemDetails
    },
    data: () => ({
        actorLimit: 8,
        entries: [],
        isLoading: false,
        model: "",
        search: null,
    }),
    methods: {
        getActor(value) {
            this.$emit('selectedActor', {
                actor: value,
                actorLimit: this.actorLimit
            })
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

<style lang="scss">
#search-graph {
    width: 380px;
}
</style>