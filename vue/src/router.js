import { createRouter, createWebHistory } from "vue-router";

import NotFound from'./pages/NotFound.vue';
import Login from'./pages/login/Login.vue';
import Dashboard from'./pages/dashboard/Dashboard.vue';
import History from'./pages/history/History.vue';
import List from'./pages/list/List.vue';
import Product from'./pages/product/Product.vue';
import Category from'./pages/category/Category.vue';

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: Login },
        { path: '/logout', component: null },
        { path: '/dashboard', component: Dashboard },
        { path: '/list', component: List },
        { path: '/history', component: History },
        { path: '/product', component: Product },
        { path: '/category', component: Category },
        { path: '/:notFound(.*)', component: NotFound }
    ],
});

export default router;
