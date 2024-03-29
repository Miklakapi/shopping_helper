<template>
    <section>
        <error-dialog v-if="error.dialog" @close="error.dialog=false"><template v-slot:default>{{ error.message }}</template></error-dialog>
        <h1>Dashboard</h1>
        <section>
            <section v-if="error.count==4"><box><error-data></error-data></box></section>
            <section v-else>
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-3">
                            <mini-box class="one mini-box">
                                <section v-if="errorPlace.spends"><error-data></error-data></section>
                                <template v-if="!isLoadingHeaders" v-slot:head>Total spend</template>
                                <spinner v-if="isLoadingHeaders && !errorPlace.spends"></spinner>
                                <section v-else-if="!errorPlace.spends" class="box-data">{{ headData['total'] }} $</section>
                            </mini-box>
                        </div>
                        <div class="col-3">
                            <mini-box class="two mini-box">
                                <section v-if="errorPlace.spends"><error-data></error-data></section>
                                <template v-if="!isLoadingHeaders" v-slot:head>Last 12 months</template>
                                <spinner v-if="isLoadingHeaders && !errorPlace.spends"></spinner>
                                <section v-else-if="!errorPlace.spends" class="box-data">{{ headData['months'] }} $</section>
                            </mini-box>
                        </div>
                        <div class="col-3">
                            <mini-box class="three mini-box">
                                <section v-if="errorPlace.spends"><error-data></error-data></section>
                                <template v-if="!isLoadingHeaders" v-slot:head>Last 4 weeks</template>
                                <spinner v-if="isLoadingHeaders && !errorPlace.spends"></spinner>
                                <section v-else-if="!errorPlace.spends" class="box-data">{{ headData['weeks'] }} $</section>
                            </mini-box>
                        </div>
                        <div class="col-3">
                            <mini-box class="four mini-box">
                                <section v-if="errorPlace.spends"><error-data></error-data></section>
                                <template v-if="!isLoadingHeaders" v-slot:head>Last 7 days</template>
                                <spinner v-if="isLoadingHeaders && !errorPlace.spends"></spinner>
                                <section v-else-if="!errorPlace.spends" class="box-data">{{ headData['days'] }} $</section>
                            </mini-box>
                        </div>
                    </div>
                </div>
                <box-with-title @click="monthSpends" class="pointer">
                    <template v-slot:head>Monthly expenses</template>
                    <section v-if="errorPlace.monthlyChart"><box><error-data></error-data></box></section>
                    <section v-else>
                        <spinner v-if="isLoadingMonthChart"></spinner>
                        <chart v-else :data="monthChartData"></chart>
                    </section>
                </box-with-title>
                <box-with-title @click="categorySpends" class="pointer">
                    <template v-slot:head>Annual expenses by category</template>
                    <section v-if="errorPlace.categoryChart"><box><error-data></error-data></box></section>
                    <section v-else>
                        <spinner v-if="isLoadingCategoryChart"></spinner>
                        <chart v-else :data="categoryChartData"></chart>
                    </section>
                </box-with-title>
                <box-with-title @click="productSpends" class="pointer">
                    <template v-slot:head>Annual expenses by product</template>
                    <section v-if="errorPlace.productChart"><box><error-data></error-data></box></section>
                    <section v-else>
                        <spinner v-if="isLoadingProductChart"></spinner>
                        <chart v-else :data="productChartData"></chart>
                    </section>
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
            isLoadingHeaders: true,
            isLoadingMonthChart: true,
            isLoadingCategoryChart: true,
            isLoadingProductChart: true,
            error: {
                count: 0,
                dialog: null,
                message: null
            },
            errorPlace: {
                spends: false,
                monthlyChart: false,
                categoryChart: false,
                productChart: false
            },
            headData: null,
            monthChartData: {
                labels: [],
                datasets: [
                    { data: [], backgroundColor: ['#723e3c', '#725f31', '#5d628e', '#5733cb', '#7a1d1d', '#b449bd', '#b1483e', '#32863d', '#6772e4', '#d1571a', '#e36754', '#d3c432'], }
                ]
            },
            productChartData: {
                labels: [],
                datasets: [
                    { data: [], backgroundColor: ['#723e3c', '#725f31', '#5d628e', '#5733cb', '#7a1d1d', '#b449bd', '#b1483e', '#32863d', '#6772e4', '#d1571a', '#e36754', '#d3c432'], }
                ]
            },
            categoryChartData: {
                labels: [],
                datasets: [
                    { data: [], backgroundColor: ['#723e3c', '#725f31', '#5d628e', '#5733cb', '#7a1d1d', '#b449bd', '#b1483e', '#32863d', '#6772e4', '#d1571a', '#e36754', '#d3c432'], }
                ]
            }
        };
    },
    components: {
        'miniBox': MiniBox,
        'chart': Chart
    },
    methods: {
        newError(error) {
            this.error.count++;
            if (!this.error.dialog) {
                this.error.message = error;
                this.error.dialog = true;
            }
        },
        monthSpends() {
            this.$router.push({ name: 'monthSpends' });
        },
        productSpends() {
            this.$router.push({ name: 'productSpends' });
        },
        categorySpends() {
            this.$router.push({ name: 'categorySpends' });
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

                this.isLoadingHeaders = false;
            })
            .catch(error => {
                this.newError(error);
                this.isLoadingHeaders = true;
                this.errorPlace.spends = true;
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

                this.isLoadingMonthChart = false;
            })
            .catch(error => {
                this.newError(error);
                this.isLoadingMonthChart = true;
                this.errorPlace.monthlyChart = true;
            });
        },
        loadCategorySpends() {
            fetch('http://localhost:8080/dashboard/spends-by-category-chart', {
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
                    this.categoryChartData['labels'].unshift(element['category_name']);
                    this.categoryChartData['datasets'][0]["data"].unshift(element['spends']);
                });

                this.isLoadingCategoryChart = false;
            })
            .catch(error => {
                this.newError(error);
                this.isLoadingCategoryChart = true;
                this.errorPlace.categoryChart = true;
            });
        },
        loadProductSpends() {
            fetch('http://localhost:8080/dashboard/spends-by-product-chart', {
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
                    this.productChartData['labels'].unshift(element['product_name']);
                    this.productChartData['datasets'][0]["data"].unshift(element['spends']);
                });

                this.isLoadingProductChart = false;
            })
            .catch(error => {
                this.newError(error);
                this.isLoadingProductChart = true;
                this.errorPlace.productChart = true;
            });
        },
    },
    created() {
        this.loadHeaders();
        this.loadSpendsByMonthChart();
        this.loadCategorySpends();
        this.loadProductSpends();
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

    .mini-box {
        height: 120px;

        .box-data {
            margin-top: 17px;
        }
    }
}

.pointer {
    cursor: pointer;
}
</style>
