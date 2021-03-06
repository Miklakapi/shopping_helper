import { createApp } from 'vue';
import 'bootstrap/dist/css/bootstrap.css';

import router from './router.js';
import store from './store/index.js';
import App from './App.vue';
import Box from './components/Box.vue';
import BoxWithTitle from './components/BoxWithTitle.vue';
import FormDialog from './components/FormDialog.vue';
import Spinner from './components/Spinner.vue';
import ErrorDialog from './components/ErrorDialog.vue';
import ErrorData from './components/ErrorData.vue';
import DataTable from './components/DataTable.vue';
import { BIconChevronRight, BIconChevronLeft } from 'bootstrap-icons-vue';

const app = createApp(App);

app.use(store);
try {
    store.dispatch('user/tryLogin').then(function () {
        app.use(router);
    });
} catch(error) {
    store.dispatch('user/logout').then(function () {
        app.use(router);
    });
}


app.component('box', Box);
app.component('boxWithTitle', BoxWithTitle);
app.component('formDialog', FormDialog);
app.component('spinner', Spinner);
app.component('errorDialog', ErrorDialog);
app.component('errorData', ErrorData);
app.component('dataTable', DataTable);
app.component('nextArrow', BIconChevronRight);
app.component('previousArrow', BIconChevronLeft);

router.isReady().then(function() {
    app.mount('#app');
})
