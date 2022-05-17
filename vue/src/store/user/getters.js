export default {
    name(state) {
        return state.user.name;
    },
    isLogin(state) {
        if (state.user.username && state.user.username.length > 0) {
            return true;
        } else {
            return false;
        }
    }
};