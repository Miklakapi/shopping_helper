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
        { path: '/', component: Login, meta: { requireAuth: false } },
        { path: '/dashboard', component: Dashboard, meta: { requireAuth: true } },
        { path: '/list', component: List, meta: { requireAuth: true } },
        { path: '/history', component: History, meta: { requireAuth: true } },
        { path: '/product', component: Product, meta: { requireAuth: true } },
        { path: '/category', component: Category, meta: { requireAuth: true } },
        { path: '/:notFound(.*)', component: NotFound, meta: { requireAuth: true } }
    ],
});

router.beforeEach(function (to, from, next) {
    if (to.meta.requireAuth && !localStorage.getItem('token')) {
        next('/');
    } else if (!to.meta.requireAuth && localStorage.getItem('token')){
        next('/dashboard');
    } else {
        next();
    }
});

export default router;
