const config = require('./../config')

function hello() { 
    return  { 
        msg: 'Hello, C-Devs!', 
        environment: config.ENV_NAME
    }
};

module.exports = {
    hello: hello
}
