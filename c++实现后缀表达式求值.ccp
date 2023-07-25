// 引入头文件
#include <iostream>
#include <stack>
#include <string>
using namespace std;

// 定义一个函数，判断一个字符是否是操作符
bool isOperator(char c) {
  return c == '+' || c == '-' || c == '*' || c == '/';
}

// 定义一个函数，根据操作符计算两个操作数的结果
int calculate(int a, int b, char op) {
  switch (op) {
    case '+': return a + b;
    case '-': return a - b;
    case '*': return a * b;
    case '/': return a / b;
    default: return 0;
  }
}

// 定义一个函数，求解后缀表达式的值
int evaluatePostfix(string expression) {
  // 创建一个栈，用来存放操作数
  stack<int> operands;
  // 遍历表达式中的每个字符
  for (char c : expression) {
    // 如果是空格，跳过
    if (c == ' ') continue;
    // 如果是操作符，从栈中弹出两个操作数，计算结果，并将结果压入栈中
    if (isOperator(c)) {
      int b = operands.top();
      operands.pop();
      int a = operands.top();
      operands.pop();
      int result = calculate(a, b, c);
      operands.push(result);
    } else {
      // 如果是操作数，将其转换为整数，并压入栈中
      int num = c - '0';
      operands.push(num);
    }
  }
  // 返回栈顶元素，即最终结果
  return operands.top();
}

// 主函数，测试一些示例
int main() {
  cout << evaluatePostfix("2 3 +") << endl; // 输出5
  cout << evaluatePostfix("4 2 /") << endl; // 输出2
  cout << evaluatePostfix("2 3 * 4 +") << endl; // 输出10
  cout << evaluatePostfix("2 3 + 4 *") << endl; // 输出20
  cout << evaluatePostfix("2 3 * 4 + 5 -") << endl; // 输出5
}
