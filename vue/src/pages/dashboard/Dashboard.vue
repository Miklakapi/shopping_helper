<template>
    <section>
        <h1>Dashboard</h1>
        <section v-if="isLoading"><box><spinner></spinner></box></section>
        <section v-else>
            <section v-if="error.status"><box><error-data></error-data></box></section>
            <section v-else>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-3"><mini-box class="one"><template v-slot:head>Total spend</template>{{ headData['total'] }} $</mini-box></div>
                        <div class="col-3"><mini-box class="two"><template v-slot:head>Last 12 months</template>{{ headData['months'] }} $</mini-box></div>
                        <div class="col-3"><mini-box class="three"><template v-slot:head>Last 4 weeks</template>{{ headData['weeks'] }} $</mini-box></div>
                        <div class="col-3"><mini-box class="four"><template v-slot:head>Last 7 days</template>{{ headData['days'] }} $</mini-box></div>
                    </div>
                </div>
                <box-with-title @click="periodicExpenses">
                    <template v-slot:head>Monthly expenses for the last 12 months</template>
                    <chart :data="monthChartData"></chart>
                </box-with-title>
            </section>
        </section>
    </section>
</template>

<script>
import MiniBox from '../../components/MiniBox.vue';
import Chart from './Chart.vue';

export default {
    data() {
        return {
            isLoading: true,
            error: {
                status: false
            },
            headData: {
                total: 0,
                months: 0,
                weeks: 0,
                days: 0
            },
            monthChartData: {
                labels: [],
                datasets: [
                    { 
                        data: [],
                        backgroundColor: [
                            '#723e3c',
                            '#725f31',
                            '#5d628e',
                            '#5733cb',
                            '#7a1d1d',
                            '#b449bd',
                            '#b1483e',
                            '#32863d',
                            '#6772e4',
                            '#d1571a',
                            '#e36754',
                            '#d3c432',
                        ]
                    }
                ]
            }
        };
    },
    components: {
        'miniBox': MiniBox,
        'chart': Chart
    },
    methods: {
        periodicExpenses() {

        },
        loadHeaders() {
            fetch('http://localhost:8080/dashboard/spends', {
                headers: {
                    'Authorization': `Token ${this.$store.getters['user/token']}`
                }
            })
            .then(async response => {
                
                if (!response.ok) {
                    let status = response.status;

                    if (status == 403) status = "Access denied.";
                    else if (status >= 500) status = "An error occurred on the server side. Please contact the administrator.";
                    else status = "An error occurred while getting data from the server."

                    return Promise.reject(status);
                }
                
                const responseData = await response.json();

                this.headData = responseData;
            })
            .catch(error => {
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        },
        loadSpendsByMonthChart() {
            fetch('http://localhost:8080/dashboard/spends-by-month-chart', {
                headers: {
                    'Authorization': `Token ${this.$store.getters['user/token']}`
                }
            })
            .then(async response => {
                
                if (!response.ok) {
                    let status = response.status;

                    if (status == 403) status = "Access denied.";
                    else if (status >= 500) status = "An error occurred on the server side. Please contact the administrator.";
                    else status = "An error occurred while getting data from the server."

                    return Promise.reject(status);
                }
                
                const responseData = await response.json();

                responseData.forEach(element => {
                    this.monthChartData['labels'].push(element['month']);
                    this.monthChartData['datasets'][0]["data"].push(element['spends']);
                });

                this.isLoading = false;
            })
            .catch(error => {
                console.log(error);
                this.error.message = error;
                this.error.dialog = true;
                this.error.status = true;
                this.isLoading = false;
            });
        }
    },
    created() {
        this.loadHeaders();
        this.loadSpendsByMonthChart();
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
