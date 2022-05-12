<template>
    <section>
        <category-form 
            v-if="form.form" 
            :success="form.success" 
            :error="form.error" 
            :type="form.edit"
            :editData="editData"
            @close="closeAndResetForm" 
            @reset="resetForm" 
            @edit="editElement"
            @add="addElement">
        </category-form>
        <error-dialog v-if="error.dialog" @close="error.dialog=false"><template v-slot:default>{{ error.message }}</template></error-dialog> 
        <h1>Categories</h1>
        <box>
            <spinner v-if="isLoading"></spinner>
            <span v-else>
                <error-data v-if="error.status"></error-data>
                <category-table 
                    v-else 
                    :data="data" 
                    @add="add"
                    @edit="edit">
                </category-table>
            </span>
        </box> 
    </section>
</template>

<script>
import CategoryTable from './CategoryTable.vue';
import CategoryForm from './CategoryForm.vue';

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
            editData: null
        };
    },
    components: {
        'categoryTable': CategoryTable,
        'categoryForm': CategoryForm,
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
        loadCategory() {
            fetch('http://server.local:5000/getCategories')
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
        addElement(data) {
            const element = {
                id: null,
                name: data.category,
            }

            fetch('http://server.local:5000/addCategory', {
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
                name: data.category,
            }

            fetch('http://server.local:5000/editCategory', {
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
                this.closeAndResetForm();
            })
            .catch(error => {
                this.form.error = true;
            });
        }
    },
    created() {
        this.loadCategory();
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
