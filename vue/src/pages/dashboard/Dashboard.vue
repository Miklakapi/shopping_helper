<template>
    <section>
        <h1>Dashboard</h1>
        <box-with-title>
            <template v-slot:head>Month Categories</template>
            <template v-slot:default>
                <spinner v-if="isLoading"></spinner>
                <span v-else>
                    <error-data v-if="error.status"></error-data>
                </span>
            </template>
        </box-with-title>
        <box-with-title>
            <template v-slot:head>Month Products</template>
            <template v-slot:default>
                <spinner v-if="isLoading"></spinner>
                <span v-else>
                    <error-data v-if="error.status"></error-data>
                </span>
            </template>
        </box-with-title>
        <box-with-title>
            <template v-slot:head>Year Categories</template>
            <template v-slot:default>
                <spinner v-if="isLoading"></spinner>
                <span v-else>
                    <error-data v-if="error.status"></error-data>
                </span>
            </template>
        </box-with-title>
        <box-with-title>
            <template v-slot:head>Year Products</template>
            <template v-slot:default>
                <spinner v-if="isLoading"></spinner>
                <span v-else>
                    <error-data v-if="error.status"></error-data>
                </span>
            </template>
        </box-with-title>
    </section>
</template>

<script>
export default {
    data() {
        return {
            isLoading: true,
        };
    }
}
</script>

<style scoped>
h1 {
    text-align: center;
}
</style>
