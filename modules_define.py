# we are defining the functions here so that this can be reuse 

def addition(add1,add2):
    return add1 + add2

def subtraction(sub1,sub2):
    return sub2 - sub1

def multiply(mul1, mul2):
    return mul1 * mul2

def division(div1,div2):
    if div2 != 0:
        return div1/div2
    else:
        return "Error: cannot divide with 0"