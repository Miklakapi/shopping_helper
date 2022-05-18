export default {
    name(state) {
        return state.username;
    },
    isLogin(state) {
        if (state.username && state.username.length > 0) {
            return true;
        } else {
            return false;
        }
    },
    token(state) {
        return state.token;
    }
};