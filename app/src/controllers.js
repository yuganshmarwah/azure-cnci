const config = require('./../config')

function hello() { 
    return  { 
        msg: 'Hello, first pipeline build 3!', 
        environment: config.ENV_NAME
    }
};

module.exports = {
    hello: hello
}
