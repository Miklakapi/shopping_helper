export default {
    async login(context, payload) {
        const response = await fetch('http://localhost:8080/login', {
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
            let error =  response.status;

            if (error >= 400 && error < 500) error = "Incorrect login details.";
            else if (error >= 500) error = "Server side error. Please contact the administrator.";
            else error = response.response.statusText;

            return Promise.reject(error);
        }

        const responseData = await response.json();
        
        localStorage.setItem('token', responseData.token);
        localStorage.setItem('expires', responseData.expires);
        localStorage.setItem('username', responseData.username);

        context.commit('setUser', {
            token: responseData.token,
            expires: responseData.expires,
            username: responseData.username
        })

        return true;
    },
    async tryLogin(context) {
        const token = localStorage.getItem('token');
        if (!token) return false;

        const response = await fetch('http://localhost:8080/isLogin', {
            method: 'POST',
            headers: {
                'Content-type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify({
                key: token
            })
        });

        if (!response.ok) {
            let error =  response.status;

            if (error >= 400 && error < 500) error = "Incorrect login details.";
            else if (error >= 500) error = "Server side error. Please contact the administrator.";
            else error = response.response.statusText;

            return Promise.reject(error);
        }

        const responseData = await response.json();

        localStorage.setItem('expires', responseData.expires);
        localStorage.setItem('username', responseData.username);

        context.commit('setUser', {
            token: responseData.token,
            username: responseData.username
        })

        return true;
    },
    logout(context) {
        localStorage.removeItem('token');
        localStorage.removeItem('expires');
        localStorage.removeItem('username');

        context.commit('setUser', {
            token: null,
            username: null
        });
    }
};
