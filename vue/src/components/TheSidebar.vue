<template>
    <nav>
        <ul :class="{expand: expanded, collapseDelay: collapseDelay}">
            <li>
                <router-link to="/dashboard">
                    <div class="square"><dashboard></dashboard></div>
                    <div class="info" v-if="text">Dashboard</div>
                </router-link>
            </li>
            <li>
                <router-link to="/list">
                    <div class="square"><checklist></checklist></div>
                    <div class="info" v-if="text">List</div>
                </router-link>
            </li>
            <li>
                <router-link to="/history">
                    <div class="square"><history></history></div>
                    <div class="info" v-if="text">History</div>
                </router-link>
            </li>
            <li>
                <router-link to="/product">
                    <div class="square"><basket></basket></div>
                    <div class="info" v-if="text">Products</div>
                </router-link>
            </li>
            <li>
                <router-link to="/category">
                    <div class="square"><tags></tags></div>
                    <div class="info" v-if="text">Categories</div>
                </router-link>
            </li>
        </ul>
    </nav>
</template>

<script>
import { BIconBasket2Fill, BIconClockHistory, BIconSpeedometer, BIconCardChecklist, BIconTagsFill } from 'bootstrap-icons-vue';

export default {
    props: ['expanded'],
    data() {
        return {
            collapseDelay: false,
            text: false,
        };
    },
    components: {
        'dashboard': BIconSpeedometer,
        'checklist': BIconCardChecklist,
        'history': BIconClockHistory,
        'basket': BIconBasket2Fill,
        'tags': BIconTagsFill,
    },
    watch: {
        expanded(newValue) {
            if (newValue === true) {
                this.collapseDelay = false;
                setTimeout(() => {
                    this.text = true;
                }, 250); 
            } else {
                this.text = false;
                this.collapseDelay = true;
            }
        }
    }
}
</script>

<style lang="scss">
@keyframes expandAnimation {
    from {
        min-width: 55px;
    }

    to {
        min-width: 147px;
    }
}

.expand {
    animation: expandAnimation 0.3s ease-out forwards;
}

@keyframes collapseAnimation {
    from {
        min-width: 147px;
    }

    to {
        min-width: 55px;
    }
}

.collapseDelay {
    animation: collapseAnimation 0.5s ease-out forwards;
}

nav {
    background-color: #272c30;

    ul {
        list-style: none;
        padding: 0;

        li {
            
            a {
                text-decoration: none;
                color: white;
                display: flex;
                align-items: center;

                &:hover {
                    color: white;
                }

                .info {
                    margin-right: 15px;
                }
            }

            .square {
                min-width: 55px;
                max-width: 55px;
                height: 55px;
                display: flex;
                align-items: center;
                justify-content: center;
            }

            &:hover {
                background-color: darken(#272c30, 5%);
            }
        }
    }
}
</style>
