<template>
    <section>
        <error-dialog v-if="error.dialog" @close="error.dialog=false"><template v-slot:default>{{ error.message }}</template></error-dialog>
        <h1>Category spends</h1>
        <box>
            <spinner v-if="isLoading"></spinner>
            <span v-else>
                <error-data v-if="error.status"></error-data>
                <section v-else>
                    <data-table>
                        <template v-slot:add><div></div></template>
                        <template v-slot:head>
                            <th>Category</th>
                            <th>Spends</th>
                        </template>
                        <tr v-for="element in data" :key="element.product_name">
                            <td scope="row">{{ element.product_name }}</td>
                            <td>{{ element.spends }} $</td>
                        </tr>
                    </data-table>
                    <div class="arrows">
                        <previous-arrow class="arrow-left" @click="toPreviousPage"></previous-arrow>
                        <next-arrow class="arrow-right" @click="toNextPage"></next-arrow>
                    </div>
                </section>
            </span>
        </box>
    </section>
</template>

<script>
export default {
    data() {
        return {
            isLoading: true,
            error: {
                message: null,
                dialog: false,
                status: false
            },
            data: [],
            nextPage: null,
            thisPage: null,
            previousPage: null
        };
    },
    methods: {
        toPreviousPage() {
            if (this.previousPage) {
                this.loadData(this.previousPage);
            }
        },
        toNextPage() {
            if (this.nextPage) {
                this.loadData(this.nextPage);
            }
        },
        loadData(link = 'http://localhost:8080/dashboard/spends-by-product-table') {
            this.thisPage = link;
            fetch(link, {
                headers: {
                    'Authorization': `Token ${this.$store.getters['user/token']}`
                }
            })
            .then(async response => {
                
                if (!response.ok) {
                    let status = response.status;

                    if (status == 403) status = "Access denied.";
                    else if (status >= 500) status = "An error occurred on the server side. Please contact the administrator.";
                    else status = "An error occurred while getting data from the server."

                    return Promise.reject(status);
                }

                const responseData = await response.json();

                this.data = responseData["results"];
                this.nextPage = responseData["next"];
                this.previousPage = responseData["previous"];
                this.isLoading = false;
            })
            .catch(error => {
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        },
    },
    created() {
        this.loadData();
    }
}
</script>

<style scoped lang="scss">
section {
    h1 {
        text-align: center;
        margin-bottom: 15px;
    }

    .arrows {
        font-size: 1.5rem;
        display: flex;
        justify-content: center;

        .arrow-left {
            margin-right: 30px;
            
            &:hover {
                color: #3c8dbc;
            }
        }

        .arrow-right {
            margin-left: 30px;

            &:hover {
                color: #3c8dbc;
            }
        }
    }
}
</style>
