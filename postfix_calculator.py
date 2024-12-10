from Operators_dict import Operators
from math_operations import Calculator
def post_calc(expression):
    """Calculate the postfix expression and returns the result"""
    result=[]
    while len(expression)!=0:
        char=expression[0]
        if char in Operators:
        #if char in operators pop two last number and check which operator is char
            num2=result.pop()
            num1=result.pop()
            if char=="+":
                result.append(Calculator.add(num1,num2))
            elif char=="-":
                result.append(Calculator.subtract(num1, num2))
            elif char=="*":
                result.append(Calculator.mul(num1, num2))
            elif char=="/":
                result.append(Calculator.div(num1, num2))
            elif char=="%":
                result.append(Calculator.modulus(num1, num2))
            elif char=="^":
                result.append(Calculator.pow(num1, num2))
            elif char=="@":
                result.append(Calculator.average(num1, num2))
            elif char=="$":
                result.append(Calculator.max(num1, num2))
            elif char=="&":
                result.append(Calculator.min(num1, num2))
            expression.pop(0)
        else:
        #if char is number push the number into result
            result.append(expression.pop(0))
    return result