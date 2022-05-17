<template>
    <header>
        <div class="icon" @click="expand">
            <icon-list :class="{animateIcon: animateIcon}" @animationend="animateIcon=false"></icon-list>
        </div>
        <div class="title">
            <router-link  to="/dashboard">Shopping Helper</router-link>
        </div>
        <div class="username">Username: 
            <code v-if="isLogin">{{ username }}</code>
            <code v-else>-</code>
        </div>
        <router-link class="logout" to="/logout">Logout</router-link>
    </header>
</template>

<script>
import { BIconList } from 'bootstrap-icons-vue';

export default {
    data() {
        return {
            animateIcon: false
        };
    },
    emits: ['toogleSidebar'],
    components: {
        'IconList': BIconList,
    },
    computed: {
        isLogin() {
            return this.$store.getters['user/isLogin'];
        },
        username() {
            return this.$store.getters['user/name'];
        },
    },
    methods: {
        expand() {
            this.animateIcon = !this.animateIcon;
            this.$emit('toogleSidebar');
        }
    }
}
</script>

<style scoped lang="scss">
@keyframes rotateIcon {
    0% {
        transform: rotate(0deg) scale(1);
    }

    50% {
        transform: rotate(180deg) scale(2);
    }

    100% {
        transform: rotate(360deg) scale(1);
    }
}

header {
    width: 100%;
    background-color: #272c30;
    display: flex;
    align-items: center;
    height: 55px;

    .icon {
        height: 100%;
        min-width: 55px;
        display: flex;
        align-items: center;
        justify-content: center;

        &:hover {
            background-color: #3c8dbc;
        }

        svg {
            width: 23px;
            height: 23px;
        }
    } 

    .animateIcon {
        animation: rotateIcon 0.3s ease-out forwards;
    }

    a {
        text-decoration: none;

        &:hover {
            color: #3c8dbc;
        }
    }

    .title {
        font-weight: bold;
        width: 70%;
        padding-left: 20px;
        font-size: 1.2rem;
    }

    .username {
        width: 30%;
        display: flex;
        align-items: center;
        justify-content: center;

        code {
            margin-left: 5px;
            font-size: 1rem;
            background-color: lighten(#272c30, 5%);
            border-radius: 0.5rem;
            padding-left: 10px;
            padding-right: 10px;
            line-height: normal;
        }
    }

    .logout {
        padding: 15px;

        &:hover {
            background-color: darken(#272c30, 2%);
        }
    }
}
</style>
