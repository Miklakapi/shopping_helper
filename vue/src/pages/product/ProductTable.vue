<template>
    <data-table @add="add">
        <template v-slot:head>
            <th>Id</th>
            <th>Product</th>
            <th>Parent Category</th>
            <th>Edit</th>
        </template>
        <template v-slot:default>
            <tr v-for="product in data" :key="product.id">
                <td scope="row">{{ product.id }}</td>
                <td>{{ product.name }}</td>
                <td>{{ nameFromId(product.category_id) }}</td>
                <td class="col-1">
                    <div class="confirm" @click="edit(product.id)">
                        <pen></pen>
                    </div>
                </td>
            </tr>
        </template>
    </data-table>
</template>

<script>
import { BIconPenFill } from 'bootstrap-icons-vue';

export default {
    props: ['data', 'categoryNames'],
    emits: ['add', 'edit'],
    components: {
        'pen': BIconPenFill
    },
    methods: {
        add() {
            this.$emit('add');
        },
        edit(id) {
            this.$emit('edit', id);
        },
        nameFromId(id) {
            const found = this.categoryNames.find(element => element.id === id);
            if (found === undefined) {
                return id
            }
            return found.name;
        }
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
</style>
