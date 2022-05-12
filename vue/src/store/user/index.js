import actions from './actions.js';
import getters from './getters.js';
import mutations from './mutations.js';

export default {
    namespaced: true,
    state() {
        return {
            user: {
                id: '1',
                username: 'Kacper',
            },
        };
    },
    mutations,
    actions,
    getters
}