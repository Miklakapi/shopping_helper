import { createStore } from 'vuex';

import user from './user/index.js';

const store = createStore({
    modules: {
        user: user
    }
});

export default store;
