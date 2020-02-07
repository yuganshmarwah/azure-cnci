const config = require('./../config')

function hello() { 
    return  { 
        msg: 'Hello, folks!', 
        environment: config.ENV_NAME
    }
};

module.exports = {
    hello: hello
}
