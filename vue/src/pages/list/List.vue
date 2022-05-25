<template>
    <section>
        <list-form 
            v-if="form.form" 
            :success="form.success" 
            :error="form.error" 
            @close="closeAndResetForm" 
            @reset="resetForm" 
            @add="addElement">
        </list-form>
        <error-dialog v-if="error.dialog" @close="error.dialog=false"><template v-slot:default>{{ error.message }}</template></error-dialog>
        <h1>Shopping List</h1>
        <box>
            <spinner v-if="isLoading"></spinner>
            <span v-else>
                <error-data v-if="error.status"></error-data>
                <section v-else>
                    <list-table :data="data" @add="add" @delete="deleteElement"></list-table>
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
import ListTable from './ListTable.vue';
import ListForm from './ListForm.vue';

export default {
    data() {
        return {
            form: {
                form: false,
                error: false,
                success: false
            },
            error: {
                message: null,
                dialog: false,
                status: false
            },
            isLoading: true,
            data: [],
            nextPage: null,
            thisPage: null,
            previousPage: null
        };
    },
    components: {
        'listForm': ListForm,
        'listTable': ListTable
    },
    methods: {
        add() {
            this.form.form = true;
        },
        closeAndResetForm() {
            this.form.form = false;
            this.resetForm();
        },
        resetForm() {
            this.form.error = false;
            this.form.success = false;
        },
        toPreviousPage() {
            if (this.previousPage) {
                this.loadList(this.previousPage);
            }
        },
        toNextPage() {
            if (this.nextPage) {
                this.loadList(this.nextPage);
            }
        },
        loadList(link = 'http://localhost:8080/shopping-list/') {
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

                this.isLoading = false;
                this.data = responseData["results"];
                this.nextPage = responseData["next"];
                this.previousPage = responseData["previous"];
            })
            .catch(error => {
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        },
        addElement(data) {
            const element = {
                name: data.product,
                quantity: data.quantity,
            }

            fetch(`http://localhost:8080/shopping-list/`, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json',
                    'Authorization': `Token ${this.$store.getters['user/token']}`
                },
                body: JSON.stringify(element)
            })
            .then(async response => {

                if (!response.ok) {
                    const error = response.statusText;
                    return Promise.reject(error);
                }

                const responseData = await response.json();

                element['id'] = responseData['id'];
                element['date'] = responseData['date'];
                element['owner_name'] = responseData['owner_name'];
                if (!this.previousPage) {
                    this.data.unshift(element);
                }
                if (this.data.length > 15) {
                    this.data.pop();
                    if (!this.nextPage) {
                        this.loadList(this.thisPage);
                    }
                }
                this.form.success = true;
            })
            .catch(error => {
                this.form.error = true;
            });
        },
        deleteElement(id) {
            fetch('http://localhost:8080/shopping-list/id/' + id, {
                    method: 'DELETE',
                    headers: {
                        'Authorization': `Token ${this.$store.getters['user/token']}`
                    }
                })
                .then(async response => {
                    
                    if (!response.ok) {
                        let status = response.status;

                        if (status == 403) status = "Access denied.";
                        else if (status >= 500) status = "An error occurred on the server side. Please contact the administrator.";
                        else status = "An error occurred while removing the product."

                        return Promise.reject(status);
                    }

                    this.data.splice(this.data.findIndex(function(i){
                        return i.id === id;
                    }), 1);

                    if (this.data.length == 14) {
                        this.loadList(this.thisPage);
                    }
                    else if (!this.data.length && this.previousPage) {
                        this.loadList(this.previousPage);
                    }
                })
                .catch(error => {
                    this.error.message = error;
                    this.error.dialog = true;
                });
        }
    },
    created() {
        this.loadList();
    },
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
