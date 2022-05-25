<template>
    <section>
        <product-form 
            v-if="form.form" 
            :success="form.success" 
            :error="form.error" 
            :data="categories" 
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
                <section v-else>
                    <product-table :data="data" @add="add" @edit="edit"></product-table>
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
            categories: [],
            editData: null,
            nextPage: null,
            previousPage: null
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
        toPreviousPage() {
            if (this.previousPage) {
                this.loadProducts(this.previousPage);
            }
        },
        toNextPage() {
            if (this.nextPage) {
                this.loadProducts(this.nextPage);
            }
        },
        loadProducts(link = 'http://localhost:8080/product/') {
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
        loadCategories() {
            fetch('http://localhost:8080/category/no-pagination', {
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
                this.categories = responseData;
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
                name: data.product,
                category: data.category,
            }

            fetch(`http://localhost:8080/product/`, {
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
                element['category'] = responseData['category'];
                element['category_name'] = responseData['category_name'];
                this.data.push(element);
                this.form.success = true;
            })
            .catch(error => {
                this.form.error = true;
            });
        },
        editElement(data) {
            const id = data.id;
            const element = {
                name: data.product,
                category: data.category,
            }

            fetch('http://localhost:8080/product/id/' + id, {
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
                found.name = responseData['name'];
                found.category = responseData['category'];
                found.category_name = responseData['category_name'];
                this.closeAndResetForm();
            })
            .catch(error => {
                this.form.error = true;
            });
        }
    },
    created() {
        this.loadProducts();
        this.loadCategories();
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
