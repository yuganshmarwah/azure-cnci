const config = require('./../config')

function hello() { 
    return  { 
        msg: 'Hello, first pipeline build!', 
        environment: config.ENV_NAME
    }
};

module.exports = {
    hello: hello
}
