<template>
    <section>
        <history-form 
            v-if="form.form" 
            :success="form.success" 
            :error="form.error" 
            :data="products"
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
            products: [],
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
            fetch('http://localhost:8080/history/', {
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
                this.data = responseData;
            })
            .catch(error => {
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        },
        loadProducts() {
            fetch('http://localhost:8080/product/base/', {
                headers: {
                    'Authorization': `Token ${this.$store.getters['user/token']}`
                }
            })
            .then(async response => {
                
                if (!response.ok) {
                    let status = response.status;

                    if (status == 403) status = "Access denied to category.";
                    else if (status >= 500) status = "An error occurred on the server side. Please contact the administrator.";
                    else status = "An error occurred while getting data from the server."

                    return Promise.reject(status);
                }

                const responseData = await response.json();

                this.isLoading = false;
                this.products = responseData;
            })
            .catch(error => {
                this.data = [];
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        },
        addElement(data) {
            const element = {
                quantity: data.quantity,
                price: data.price,
                date: data.date,
                owner: data.owner,
                product: data.product
            }

            fetch(`http://localhost:8080/history/`, {
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
                element['product'] = responseData['product'];
                element['product_name'] = responseData['product_name'];
                this.data.unshift(element);
                this.form.success = true;
            })
            .catch(error => {
                this.form.error = true;
            });
        },
        editElement(data) {
            const id = data.id;
            const element = {
                quantity: data.quantity,
                price: data.price,
                date: data.date,
                owner: data.owner,
                product: data.product
            }

            fetch('http://localhost:8080/history/id/' + id, {
                method: 'PUT',
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
                
                this.form.success = true;
                const found = this.data.find(el => el.id === id);
                found.quantity = responseData['quantity']; 
                found.price = responseData['price'];
                found.date = responseData['date'];
                found.owner = responseData['owner'];
                found.product = responseData['product']; 
                found.product_name = responseData['product_name']; 
                this.closeAndResetForm();
            })
            .catch(error => {
                this.form.error = true;
            });
        }
    },
    created() {
        this.loadHistory();
        this.loadProducts();
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
