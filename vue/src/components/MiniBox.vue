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
        padding-bottom: 0;
        font-size: 0.8rem;
        text-align: center;
        color: white;
    }

    .body {
        padding: 20px;
        padding-top: 10px;
        font-size: 1.3rem;
        text-align: center;
        color: white;
    }
}
</style>
