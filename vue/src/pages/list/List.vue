<template>
    <section>
        <list-form v-if="form" @close="closeForm" :success="formData.success" :error="formData.error" @reset="resetForm" @add="addElement"></list-form>
        <error-dialog v-if="error.dialog" @close="closeError">
            <template v-slot:default>{{ error.message }}</template>
        </error-dialog>
        <h1>Shopping List</h1>
        <box>
            <spinner v-if="isLoading"></spinner>
            <span v-else>
                <error-data v-if="error.status"></error-data>
                <list-table v-else :data="data" @add="add" @delete="deleteElement"></list-table>
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
            form: false,
            error: {
                message: null,
                dialog: false,
                status: false
            },
            formData: {
                error: false,
                success: false
            },
            isLoading: true,
            data: []
        };
    },
    components: {
        'listForm': ListForm,
        'listTable': ListTable
    },
    methods: {
        closeForm() {
            this.form = false;
        },
        closeError() {
            this.error.dialog = false;
        },
        add() {
            this.form = true;
        },
        resetForm() {
            this.formData.error = false;
            this.formData.success = false;
        },
        loadList() {
            fetch('http://localhost:8080/shopping-list/')
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }

                this.isLoading = false;
                this.data = responseData;
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
                id: null,
                name: data.product,
                quantity: data.quantity,
                owner: data.owner,
                date: null
            }

            fetch(`http://localhost:8080/shopping-list/`, {
                method: 'POST',
                headers: {
                    'Content-type': 'application/json'
                },
                body: JSON.stringify(element)
            })
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }

                element['id'] = responseData['id'];
                element['date'] = responseData['date'];
                this.data.unshift(element);
                this.formData.success = true;
            })
            .catch(error => {
                this.formData.error = true;
            });
        },
        deleteElement(id) {
            fetch('http://localhost:8080/shopping-list/id/' + id, {
                    method: 'DELETE'
                })
                .then(async response => {

                    if (!response.ok) {
                        const error = (responseData && responseData.message) || response.statusText;
                        return Promise.reject(error);
                    }

                    this.data.splice(this.data.findIndex(function(i){
                        return i.id === id;
                    }), 1);
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
}
</style>
