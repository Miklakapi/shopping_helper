<template>
    <data-table @add="add">
        <template v-slot:head>
            <th>Product</th>
            <th>Quantity</th>
            <th>Date</th>
            <th>Owner</th>
            <th>Complete</th>
        </template>
        <template v-slot:tbody>
            <transition-group tag="tbody" name="table-list">
                <tr v-for="element in data" :key="element.id">
                    <td scope="row">{{ element.name }}</td>
                    <td>{{ element.quantity }}</td>
                    <td>{{ element.date }}</td>
                    <td>{{ element.owner_name }}</td>
                    <td class="col-1">
                        <div class="confirm" @click="deleteElement(element.id)">
                            <check-sign></check-sign>
                        </div>
                    </td>
                </tr>
            </transition-group>
        </template>
    </data-table>
</template>

<script>
import { BIconCheckLg } from 'bootstrap-icons-vue';

export default {
    props: ['data'],
    emits: ['add', 'delete'],
    components: {
        'checkSign': BIconCheckLg
    },
    methods: {
        add() {
            this.$emit('add');
        },
        deleteElement(id) {
            this.$emit('delete', id);
        },
    }
}
</script>

<style scoped lang="scss">
.confirm {
    background-color: #198754;
    display: flex;
    width: 35px;
    border-radius: 0.7rem;
    height: 24px;
    align-items: center;
    justify-content: center;
    color: white;

    &:hover {
        background-color: darken(#198754, 5%);
    }
}

@keyframes table-list-animation {
    0% {
        opacity: 1;
        transform: translateX(0);
    }

    100% {
        opacity: 0;
        transform: translateX(30px);
    }
}

.table-list-leave-active {
    animation: table-list-animation 0.6s ease-in;
}
</style>
