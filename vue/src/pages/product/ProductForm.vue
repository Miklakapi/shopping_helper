<template>
    <form-dialog @back="back" @add="add" :error="error" :success="success" v-on:keyup.enter="add">
        <template v-slot:head>
            Adding a product the database
        </template>
        <template v-slot:default>
            <div v-if="type" class="input-group">
                <span class="input-group-text">Id</span>
                <input type="number" disabled class="form-control" :placeholder="editData.id">
            </div>
            <div class="input-group">
                <span class="input-group-text">Product</span>
                <input type="text" class="form-control" placeholder="Product" v-model="product.val">
                <span class="invalid" v-if="!product.isValid">
                    Invalid product name.
                </span>
            </div>
            <div class="input-group">
                <span class="input-group-text">Parent</span>
                <select class="form-control" v-model="category.val">
                    <option v-for="categoryElement in data" :value="categoryElement.id" :key="categoryElement.id">{{ categoryElement.name }}</option>
                </select>
                <span class="invalid" v-if="!category.isValid">
                    Invalid category name.
                </span>
            </div>
        </template>
        <template v-if="type" v-slot:add>Edit</template>
    </form-dialog>
</template>

<script>
export default {
    data() {
        return {
            product: {
                val: '',
                isValid: true
            },
            category: {
                val: '',
                isValid: true
            },
        };
    },
    props: ['success', 'error', 'data', 'type', 'editData'],
    emits: ['close', 'reset', 'add', 'edit'],
    methods: {
        validateForm() {
            if (this.product.val === '') {
                this.product.isValid = false;
            } else {
                this.product.isValid = true;
            }

            if (this.category.val === '') {
                this.category.isValid = false;
            } else {
                this.category.isValid = true;
            }

            if (this.product.isValid === false || this.category.isValid === false) return false;
            return true;
        },
        add() {
            this.$emit('reset');
            
            if (this.validateForm() === false) return;

            if (this.type) {
                const formData = {
                    id: this.editData.id,
                    product: this.product.val,
                    category: this.category.val,
                }
                this.$emit('edit', formData);
            } else {
                const formData = {
                    product: this.product.val,
                    category: this.category.val,
                }
                this.$emit('add', formData);

                this.product.val = '';
                this.product.isValid = true;
                this.category.val = '';
                this.category.isValid = true;
            }
        },
        back() {
            this.$emit('close');
        }
    },
    created() {
        if (this.type) {
            this.product.val = this.editData.name;
            this.category.val = this.editData.category;
        }
    }
}
</script>

<style scoped lang="scss">
.input-group {
    margin-bottom: 1.0rem;

    .input-group-text {
        width: 90px;
    }

    .invalid {
        width: 100%;
        margin-top: 0.25rem;
        font-size: 0.875em;
        color: #dc3545;
        font-weight: bold;
    }
}
</style>
