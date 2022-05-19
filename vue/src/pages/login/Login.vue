<template>
    <section>
        <error-dialog v-if="error.dialog" @close="closeError">
            <template v-slot:default>{{ error.message }}</template>
        </error-dialog>
        <box-with-title>
            <template v-slot:head>Login</template>
            <template v-slot:default>
                <form @submit.prevent="">
                    <div class="input-group">
                        <input type="text" class="form-control" placeholder="Username" v-model.trim="username.val">
                        <span class="invalid" v-if="!username.isValid">
                            Invalid username.
                        </span>
                    </div>
                    <div class="input-group">
                        <input type="password" class="form-control" placeholder="Password" v-model.trim="password.val">
                        <span class="invalid" v-if="!password.isValid">
                            Invalid password.
                        </span>
                    </div>
                    <button type="button" class="btn btn-primary center-block" @click="login">Login</button>
                </form>
            </template>
        </box-with-title>
    </section>
</template>

<script>
export default {
    data() {
        return {
            username: {
                val: '',
                isValid: true
            },
            password: {
                val: '',
                isValid: true
            },
            error: {
                message: null,
                dialog: false
            }
        }
    },
    methods: {
        closeError() {
            this.error.message = null,
            this.error.dialog = false
        },
        validateForm() {
            if (this.username.val === '') {
                this.username.isValid = false;
            } else {
                this.username.isValid = true;
            }

            if (this.password.val === '') {
                this.password.isValid = false;
            } else {
                this.password.isValid = true;
            }

            if (this.username.isValid === false || this.password.isValid === false) return false;
            return true;
        },
        async login() {
            if (this.validateForm() === false) return;

            const formData = {
                username: this.username.val,
                password: this.password.val,
            }

            try {
                const response = await this.$store.dispatch('user/login', formData);
            } catch(error) {
                this.error.message = error;
                this.error.dialog = true;
                return;
            }

            this.$router.replace('/dashboard');
        },
    }
}
</script>

<style scoped lang="scss">
form {
    width: 50%;
    margin: auto;
    text-align: center;

    .input-group {
        margin-bottom: 1.0rem;

        .invalid {
            width: 100%;
            margin-top: 0.25rem;
            font-size: 0.875em;
            color: #dc3545;
            font-weight: bold;
        }
    }

    button {
        width: 10rem;
        margin-bottom: 15px;
    }

}
</style>
