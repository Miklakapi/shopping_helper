<template>
    <form-dialog @back="back" @add="add" :error="error" :success="success">
        <template v-slot:head>
            Adding a product to shopping list
        </template>
        <template v-slot:default>
            <div class="input-group">
                <span class="input-group-text">Product</span>
                <input type="text" class="form-control" placeholder="Product" v-model.trim="product.val">
                <span class="invalid" v-if="!product.isValid">
                    Invalid product name.
                </span>
            </div>
            <div class="input-group">
                <span class="input-group-text">Quantity</span>
                <input type="number" class="form-control" placeholder="Quantity" min="1" v-model.number="quantity.val">
                <span class="invalid" v-if="!quantity.isValid">
                    Invalid quantity.
                </span>
            </div>
        </template>
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
            }
        };
    },
    props: ['success', 'error'],
    emits: ['close', 'reset', 'add'],
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

            if (this.quantity.isValid === false || this.product.isValid === false) return false;
            return true;
        },
        add() {
            this.$emit('reset');
            
            if (this.validateForm() === false) return;

            const formData = {
                product: this.product.val,
                quantity: this.quantity.val,
                date: new Date().toISOString().slice(0, 10)
            }

            this.$emit('add', formData);

            this.product.val = '';
            this.product.isValid = true;
            this.quantity.val = '';
            this.quantity.isValid = true;
        },
        back() {
            this.$emit('close');
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
