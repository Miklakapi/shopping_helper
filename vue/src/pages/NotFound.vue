<template>
    <section>
        <h1>Page not found</h1>
        <box>
            This page could not be found. Try a different page or go to the <router-link to="/dashboard">home page</router-link>.
        </box>
    </section>
</template>

<style scoped lang="scss">
section {

    h1 {
        text-align: center;
    }

    section {
        text-align: center;
        font-weight: bold;

        a {
            color: #f39c12;
        }
    }
}
</style>
