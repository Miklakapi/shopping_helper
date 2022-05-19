<template>
    <div class="container p-0">
        <the-header @toogleSidebar="toogleExpand"></the-header>
        <div class="content">
            <the-sidebar :expanded="expanded"></the-sidebar>
            <the-content-wrapper>
                <router-view v-slot="slotProps">
                    <transition name="route" mode="out-in">
                        <component :is="slotProps.Component"></component>
                    </transition>
                </router-view>
            </the-content-wrapper>
        </div>
    </div>
</template>

<script>
import TheHeader from './components/TheHeader.vue';
import TheSidebar from './components/TheSidebar.vue';
import TheContentWrapper from './components/TheContentWrapper.vue';

export default {
    data() {
        return {
            expanded: false
        };
    },
    components: {
        TheHeader,
        TheSidebar,
        TheContentWrapper
    },
    methods: {
        toogleExpand() {
            this.expanded = !this.expanded;
        }
    },
    async created() {
        try {
            await this.$store.dispatch('user/tryLogin');
        } catch(error) {
            this.$store.dispatch('user/logout');
            this.$router.replace('/');
        }
    }
}
</script>

<style>
body {
    background-image: url("./black-1920.jpg");
    margin: 0;
    color: #bec5cb;
}

a {
    color: #bec5cb;
}

.container {
    background-color: #353c42;
    box-shadow: 0 0 10px rgb(0 0 0 / 50%);
}

.content {
    display: flex;
}

@keyframes leave {
    0% {
        transform: scale(1);
    }

    100% {
        transform: scale(0);
    }
}

@keyframes enter {
    0% {
        transform: scale(0);
    }

    100% {
        transform: scale(1);
    }
}

.route-enter-active {
    animation: enter .3s ease-in;
}

.route-leave-active {
    animation: leave .3s ease-out;
}
</style>
