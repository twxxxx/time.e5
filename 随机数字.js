// 引入随机数生成函数
const random = require('random-js');

// 创建一个随机数生成器
const rng = random.generator();

// 生成一个介于0和10之间的随机整数
const randomNumber = rng.integer(0, 10);

// 打印随机生成的数字
console.log(`随机生成的数字是： ${randomNumber}`);
