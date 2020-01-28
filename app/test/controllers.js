const assert = require('assert');
const controllers = require('../src/controllers')

const HOME_API_EXPECTED_MSG = 'Hello, first pipeline build 14!';

describe('Controllers', function() {
  describe('hello', function() {
    it('should return Hello World!', function() {
      const helloFromSomeEnv = controllers.hello();
      assert.equal(helloFromSomeEnv.msg, HOME_API_EXPECTED_MSG);
    });
  });
});
