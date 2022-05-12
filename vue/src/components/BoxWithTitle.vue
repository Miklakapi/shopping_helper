<template>
    <section>
        <div class="title">
            <slot name="head"></slot>
        </div>
        <div class="body">
            <slot></slot>
        </div>
    </section>
</template>

<style scoped lang="scss">
section {
    background-color: #272c30;
    border-radius: 10px;
    margin-bottom: 25px;

    .title {
        padding: 10px;
        border-bottom: 1px solid #353c42;
        font-size: 1.2rem;
    }

    .body {
        padding: 20px;
    }
}
</style>
