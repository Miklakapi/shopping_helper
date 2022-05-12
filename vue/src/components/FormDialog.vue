<template>
    <section>
        <div class="overlay" @click="back"></div>
        <div class="box" :class="{ showUp: showUp, hide: hide }" @animationend="endAnimation">
            <div class="headerContainer">
                <slot name='head'></slot>
            </div>
            <div class="formContainer">
                <form @submit.prevent="">
                    <slot></slot>
                    <div v-if="success" class="text-success">Form successfully sent.</div>
                    <div v-if="error" class="text-danger">Error while submitting the form.</div>
                    <div>
                        <button type="button" @click="back" class="btn btn-danger">Cancel</button>
                        <button type="button" @click="add" class="btn btn-success float-end"><slot name="add">Add</slot></button>
                    </div>
                </form>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    data() {
        return {
            showUp: true,
            hide: false,
        };
    },
    emits: ['back', 'add'],
    props: ['success', 'error'],
    methods: {
        back() {
            this.hide = true;
        },
        add() {
            this.$emit('add');
        },
        endAnimation() {
            if (this.hide === true) {
                this.$emit('back');
            }
            this.showUp = false;
            this.hide = false;
        }
    }
}
</script>

<style scoped lang="scss">
@keyframes showUpAnimation {
    from {
        opacity: 0;
        transform: translateY(-100px) scale(0.8);
    }

    to {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

.showUp {
    animation: showUpAnimation 0.3s ease-out;
}

.hide {
    animation: showUpAnimation 0.3s ease-in reverse;
}

.overlay {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    opacity: 0.5;
    background-color: black;
    z-index: 100;
}

section {

    .box {
        z-index: 200;
        background-color: #353c42;
        border-radius: 1.5rem;
        overflow: hidden;
        position: fixed;
        top: 20%;
        left: calc(50% - (450px / 2));

        .headerContainer {
            background-color: #272c30;
            padding: 20px;
            text-align: center;
            font-weight: bold;
        }

        .formContainer {
            width: 450px;
            padding: 20px;

            .text-success,
            .text-danger {
                font-weight: bold;
                margin: 10px 0px;
                text-align: center;
            }

            button {
                width: 80px;
            }
        }
    }
}
</style>
