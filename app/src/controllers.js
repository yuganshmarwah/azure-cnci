const config = require('./../config')

function hello() { 
    return  {
        msg: 'Hello, PR tesing!',
        environment: config.ENV_NAME
    }
};

module.exports = {
    hello: hello
}
