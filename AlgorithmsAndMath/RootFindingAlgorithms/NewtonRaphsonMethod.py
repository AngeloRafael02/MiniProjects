import sympy 

def f(x):
    return (-0.9*(x**2))+(1.7*x)+(2.5)
def dFString():
    x = sympy.Symbol('x')
    f = (-0.9*(x**2))+(1.7*x)+(2.5)
    df = f.diff(x)
    return str(df)
def dF(x):
    Df = dFString()
    return eval(Df.replace('x',str(x)))
def NewtonRaphsonMethod(x,iteration=10):
    X=x
    i=0
    while i<iteration:
        xi = X-(f(X)/dF(X))
        print(xi)
        X=xi
        i+=1
print(f(5))
print(dF(5))
NewtonRaphsonMethod(5)