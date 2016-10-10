var binary = require('node-pre-gyp');
var path = require('path')
var binding_path = binary.find(path.resolve(path.join(__dirname,'./package.json')));

module.export = require(binding_path);

//require('assert').equal(binding.hello(),"hello");
