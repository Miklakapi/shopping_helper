<template>
    <section>
        <h1>Dashboard</h1>
        <section v-if="!isLoading"><box><spinner></spinner></box></section>
        <section v-else>
            <section v-if="error.status"><box><error-data></error-data></box></section>
            <section v-else>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-3"><mini-box class="one"><template v-slot:head>Total spend</template>2256.34 $</mini-box></div>
                        <div class="col-3"><mini-box class="two"><template v-slot:head>Last 12 months</template>1656.34 $</mini-box></div>
                        <div class="col-3"><mini-box class="three"><template v-slot:head>Last 4 weeks</template>300.21 $</mini-box></div>
                        <div class="col-3"><mini-box class="four"><template v-slot:head>Last 7 days</template>78.27 $</mini-box></div>
                    </div>
                </div>
                <box-with-title @click="periodicExpenses">
                    <template v-slot:head>Monthly expenses for the last 12 months</template>
                    TO DO
                </box-with-title>
                <box-with-title @click="periodicExpenses">
                    <template v-slot:head>Weekly expenses for the last 12 weeks</template>
                    TO DO
                </box-with-title>
            </section>
        </section>
    </section>
</template>

<script>
import MiniBox from '../../components/MiniBox.vue';

export default {
    data() {
        return {
            isLoading: true,
            error: {
                status: false
            },
        };
    },
    components: {
        'miniBox': MiniBox
    },
    methods: {
        periodicExpenses() {
            console.log(1);
        },
        loadHeaders() {

        },
        loadMonthlyExpenses() {

        },
        loadWeeklyExpenses() {

        }
    },
    create() {
        loadHeaders();
        loadMonthlyExpenses();
        loadWeeklyExpenses();
    }
}
</script>

<style scoped lang="scss">
h1 {
    text-align: center;
}

.row {
    .one {
        background-color: #09708a;
    }

    .two {
        background-color: #9866d1;
    }

    .three {
        background-color: #0ab1a0;
    }

    .four {
        background-color: #474996;
    }
}
</style>
