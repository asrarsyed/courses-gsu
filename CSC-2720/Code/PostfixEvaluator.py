from utils import ArrayStack


def postfixEval(postfixExpr):
    stack = ArrayStack()
    tokens = postfixExpr.split()

    for token in tokens:
        if token.isnumeric():
            stack.push(int(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = doMath(token, operand1, operand2)
            stack.push(result)
    return stack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


print(postfixEval("1 2 + 3 4 + *"))
