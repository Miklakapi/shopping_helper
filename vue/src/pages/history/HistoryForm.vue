<template>
    <form-dialog @back="back" @add="add" :error="error" :success="success">
        <template v-slot:head>
            Adding a product to your history
        </template>
        <template v-slot:default>
            <div v-if="type" class="input-group">
                <span class="input-group-text">Id</span>
                <input type="number" disabled class="form-control" :placeholder="editData.id">
            </div>
            <div class="input-group">
                <span class="input-group-text">Product</span>
                <select class="form-control" v-model.trim="product.val">
                    <option v-for="productElement in data" :value="productElement.id" :key="productElement.id">{{ productElement.name }}</option>
                </select>
                <span class="invalid" v-if="!product.isValid">
                    Invalid product name.
                </span>
            </div>
            <div class="input-group">
                <span class="input-group-text">Quantity</span>
                <input type="number" class="form-control" placeholder="Quantity" v-model.number="quantity.val" min="1">
                <span class="invalid" v-if="!quantity.isValid">
                    Invalid quantity.
                </span>
            </div>
            <div class="input-group">
                <span class="input-group-text">Price</span>
                <input type="number" step="0.01" class="form-control" placeholder="Price" v-model.number="price.val" min="0.01">
                <span class="invalid" v-if="!price.isValid">
                    Invalid price.
                </span>
            </div>
            <div class="input-group">
                <span class="input-group-text">Date</span>
                <input type="date" class="form-control" v-model="date.val">
                <span class="invalid" v-if="!date.isValid">
                    Invalid date.
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
            quantity: {
                val: '',
                isValid: true
            },
            price: {
                val: '',
                isValid: true
            },
            date: {
                val: '',
                isValid: true
            }
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

            if (this.quantity.val === '') {
                this.quantity.isValid = false;
            } else {
                this.quantity.val = parseInt(this.quantity.val);
                if (this.quantity.val <= 0) {
                    if (this.quantity.val <= -1) {
                        this.quantity.val = -this.quantity.val;
                        this.quantity.isValid = true;
                    } else {
                        this.quantity.isValid = false;
                    }
                } else {
                    this.quantity.isValid = true;
                }
            }

            if (this.price.val === '') {
                this.price.isValid = false;
            } else {
                this.price.val = parseFloat(this.price.val);
                if (this.price.val <= 0) {
                    if (this.price.val !== 0) {
                        this.price.val = -this.price.val;
                        this.price.isValid = true;
                    } else {
                        this.price.isValid = false;
                    }
                } else {
                    this.price.isValid = true;
                }
            }

            if (this.date.val === '') {
                this.date.isValid = false;
            } else {
                this.date.isValid = true;
            }

            if (this.quantity.isValid === false || this.product.isValid === false || this.price.isValid === false || this.date.isValid === false) return false;
            return true;
        },
        add() {
            this.$emit('reset');
            
            if (this.validateForm() === false) return;

            if (this.type) {
                const formData = {
                    id: this.editData.id,
                    product: this.product.val,
                    quantity: this.quantity.val,
                    price: this.price.val,
                    date: this.date.val,
                    owner: this.editData.owner
                };
                this.$emit('edit', formData);
            } else {
                const formData = {
                    product: this.product.val,
                    quantity: this.quantity.val,
                    price: this.price.val,
                    date: this.date.val,
                    owner: this.$store.getters['user/username']
                };
                this.$emit('add', formData);
                
                this.product.val = '';
                this.product.isValid = true;
                this.quantity.val = '';
                this.quantity.isValid = true;
                this.price.val = '';
                this.price.isValid = true;
                this.date.isValid = true;
            }
        },
        back() {
            this.$emit('close');
        },
    },
    created() {
        if (this.type) {
            this.product.val = this.editData.product;
            this.quantity.val = this.editData.quantity;
            this.price.val = this.editData.price;
            this.date.val = this.editData.date;
        } else {
            const date = new Date();
            this.date.val = date.toISOString().split('T')[0];
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
