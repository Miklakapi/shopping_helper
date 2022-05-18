export default {
    async login(context, payload) {
        const response = await fetch('http://localhost:8080/login/', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json'
            },
            body: JSON.stringify({
                username: payload.username,
                password: payload.password
            })
        });
        
        if (!response.ok) {
            const error =  response.statusText;
            return error;
        }

        const responseData = await response.json();
        console.log(responseData);
        context.commit('setUser', {
            token: responseData.token
        })

        return true;
    },
    logout(context) {
        context.commit('setUser', {
            token: null,
            username: null
        });
    },
    auth(context, payload) {

    }
};
