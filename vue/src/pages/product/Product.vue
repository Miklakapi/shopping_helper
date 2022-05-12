<template>
    <section>
        <product-form 
            v-if="form.form" 
            :success="form.success" 
            :error="form.error" 
            :data="categoryNames" 
            :type="form.edit" 
            :editData="editData" 
            @close="closeAndResetForm" 
            @reset="resetForm" 
            @edit="editElement" 
            @add="addElement">
        </product-form>
        <error-dialog v-if="error.dialog" @close="error.dialog=false"><template v-slot:default>{{ error.message }}</template></error-dialog> 
        <h1>Products</h1>
        <box>
            <spinner v-if="isLoading"></spinner>
            <span v-else>
                <error-data v-if="error.status"></error-data>
                <product-table 
                    v-else 
                    :data="data" 
                    :categoryNames="categoryNames" 
                    @add="add"
                    @edit="edit">
                </product-table>
            </span>
        </box>
    </section>
</template>

<script>
import ProductTable from './ProductTable.vue';
import ProductForm from './ProductForm.vue';

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
                dialog: false,
                message: null,
                status: false
            },
            isLoading: true,
            data: [],
            categoryNames: [],
            editData: null
        };
    },
    components: {
        'productTable': ProductTable,
        'productForm': ProductForm
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
        loadProducts() {
            fetch('http://server.local:5000/getProducts')
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
        loadCategoryNames() {
            fetch('http://server.local:5000/getCategoryNames')
            .then(async response => {
                const responseData = await response.json();

                if (!response.ok) {
                    const error = (responseData && responseData.message) || response.statusText;
                    return Promise.reject(error);
                }

                this.isLoading = false;
                this.categoryNames = responseData.data;
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
                category_id: data.category,
            }

            fetch(`http://server.local:5000//addProduct`, {
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
                name: data.product,
                category_id: data.category,
            }

            fetch('http://server.local:5000/editProduct', {
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
                found.name = element.name; 
                found.category_id = element.category_id; 
                this.closeAndResetForm();
            })
            .catch(error => {
                this.form.error = true;
            });
        }
    },
    created() {
        this.loadProducts();
        this.loadCategoryNames();
    }
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
