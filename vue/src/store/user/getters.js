export default {
    name(state) {
        return state.username;
    },
    isLogin(state) {
        if (state.token && state.token.length > 0) {
            return true;
        } else {
            return false;
        }
    }
};