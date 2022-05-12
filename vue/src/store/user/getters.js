export default {
    username(state) {
        return state.user.username;
    },
    isLogin(state) {
        if (state.user.username && state.user.username.length > 0) {
            return true;
        } else {
            return false;
        }
    }
};