def plus(a,b):
    return a+b
def multi(a,b):
    return a*b
def minus(a,b):
    return a-b
def div(a,b):
    return a/b

PLUS = "+"
MULTI = "*"
MINUS = "-"
DIV = "/"
tokens = ["18"]

def evalRPN(tokens):
    # Init stack
    stack = []
    # read token caracteres
    for item in tokens:
    # check if item is not a number
        if not item.lstrip("-").isdigit():
            b = int(stack.pop())
            a = int(stack.pop())
    
            if item == PLUS:
                result = plus(a,b)
                stack.append(result)
            if item == MULTI:
                result = multi(a,b)
                stack.append(result)
            if item == MINUS:
                result = minus(a,b)
                stack.append(result)
            if item == DIV:
                result = div(a,b)
                stack.append(result)
        else:
            stack.append(item)
    return stack[0]    


result = evalRPN(tokens)
print(result)