export default {
    setUser(state, payload) {
        state.id = payload.id;
        state.username = payload.username;
        state.token = payload.token;
    }
};