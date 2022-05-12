<template>
    <section>
        <history-form 
            v-if="form.form" 
            :success="form.success" 
            :error="form.error" 
            :data="productNames"
            :type="form.edit"
            :editData="editData"
            @close="closeAndResetForm" 
            @reset="resetForm" 
            @edit="editElement"
            @add="addElement">
        </history-form>
        <error-dialog v-if="error.dialog" @close="error.dialog=false"><template v-slot:default>{{ error.message }}</template></error-dialog>
        <h1>Product History</h1>
        <box>
            <spinner v-if="isLoading"></spinner>
            <span v-else>
                <error-data v-if="error.status"></error-data>
                <history-table 
                    v-else 
                    :data="data" 
                    :productNames="productNames" 
                    @add="add" 
                    @edit="edit">
                </history-table>
            </span>
        </box>
    </section>
</template>

<script>
import HistoryTable from './HistoryTable.vue';
import HistoryForm from './HistoryForm.vue';

export default {
    data() {
        return {
            form: {
                form: false,
                edit: false,
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
            productNames: [],
            editData: null
        };
    },
    components: {
        'historyForm': HistoryForm,
        'historyTable': HistoryTable
    },
    methods: {
        add() {
            this.form.edit = false;
            this.form.form = true;
        },
        edit(id) {
            this.form.edit = true;
            this.form.form = true;
            this.editData = this.data.find(element => element.id === id);
        },
        closeAndResetForm() {
            this.form.form = false;
            this.resetForm();
        },
        resetForm() {
            this.form.error = false;
            this.form.success = false;
        },
        loadHistory() {
            fetch('http://server.local:5000/getHistory')
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }

                this.isLoading = false;
                this.data = responseData.data;
            })
            .catch(error => {
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        },
        loadProductNames() {
            fetch('http://server.local:5000/getProductNames')
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }

                this.isLoading = false;
                this.productNames = responseData.data;
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
                quantity: data.quantity,
                price: data.price,
                date: data.date,
                owner: data.owner,
                product_id: data.product
            }

            fetch('http://server.local:5000/addHistory', {
                method: 'POST',
                body: JSON.stringify(element)
            })
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }

                element['id'] = responseData.data;
                this.data.push(element);
                this.form.success = true;
            })
            .catch(error => {
                this.form.error = true;
            });
        },
        editElement(data) {
            const element = {
                id: data.id,
                quantity: data.quantity,
                price: data.price,
                date: data.date,
                owner: data.owner,
                product_id: data.product
            }

            fetch('http://server.local:5000/editHistory', {
                method: 'POST',
                body: JSON.stringify(element)
            })
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }
                this.form.success = true;
                const found = this.data.find(el => el.id === element.id);
                found.quantity = element.quantity; 
                found.price = element.price; 
                found.date = element.date; 
                found.owner = element.owner; 
                found.product_id = element.product_id; 
                this.closeAndResetForm();
            })
            .catch(error => {
                this.form.error = true;
            });
        }
    },
    created() {
        this.loadHistory();
        this.loadProductNames();
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
