export default {
    username(state) {
        return state.username;
    },
    isLogin(state) {
        if (state.token && state.token.length > 0) {
            return true;
        } else {
            return false;
        }
    },
    token(state) {
        if (state.token === null) {
            state.token = localStorage.getItem('token'); 
        } 
        return state.token;
    }
};