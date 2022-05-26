<template>
    <bar
        :chart-data="data"
        :chart-options="options"
        :height="300"
    ></bar>
</template>

<script>
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
    components: {
        'bar': Bar
    },
    props: ['data'],
    data() {
        return {
            options: {
                responsive: true,
                maintainAspectRatio: false,
            }
        };
    }
}
</script>

<style scoped lang="scss">

</style>