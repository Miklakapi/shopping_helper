<template>
    <section>
        <div class="overlay" @click="close"></div>
        <div class="box" :class="{ showUp: showUp, hide: hide }" @animationend="endAnimation">
            <div class="headerContainer">
                <slot name='head'>Error</slot>
            </div>
            <div class="formContainer">
                <form @submit.prevent="">
                    <slot></slot>
                    <div>
                        <button type="button" @click="close" class="btn btn-danger float-end">Close</button>
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
    emits: ['close'],
    methods: {
        close() {
            this.hide = true;
        },
        endAnimation() {
            if (this.hide === true) {
                this.$emit('close');
            }
            this.showUp = false;
            this.hide = false;
        }
    }
}
</script>

<style scoped lang="scss">
@keyframes show-up {
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
    animation: show-up 0.3s ease-out;
}

.hide {
    animation: show-up 0.3s ease-in reverse;
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

            button {
                margin: 20px;
                margin-right: 0;
                width: 80px;
            }
        }
    }
}
</style>
