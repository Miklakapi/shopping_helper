<template>
    <section>
        <div class="add" @click="add">
            <circle-add></circle-add>
        </div>
        <table class="table nowrap">
            <thead>
                <tr>
                    <slot name="head"></slot>
                </tr>
            </thead>
            <slot name="tbody">
                <tbody>
                    <slot></slot>
                </tbody>
            </slot>
        </table>
    </section>
</template>

<script>
import { BIconPlusCircle } from 'bootstrap-icons-vue';

export default {
    emits: ['add'],
    components: {
        'circleAdd': BIconPlusCircle
    },
    methods: {
        add() {
            this.$emit('add')
        }
    },
}
</script>

<style scoped lang="scss">
.add {
    float: right;

    svg {
        color: #198754;
        height: 30px;
        width: 30px;
        margin-bottom: 15px;

        &:hover {
            color: lighten(#198754, 7%);
        }
    }
}

table {
    color: #bec5cb;;
    border: lighten(#272c30, 10%) 1px solid;

    tr:nth-child(even) {
        background-color: lighten(#272c30, 5%);
    }
}
</style>
