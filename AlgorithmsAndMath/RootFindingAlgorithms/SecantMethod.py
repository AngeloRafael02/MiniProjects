import math

def f(x):
    """Adjust your equation after the return keyword"""
    return (math.e**-x)-x
def SecantMethod(x1,x2,iteration=10):
    X1=x1
    X2=x2
    i=0
    while i<iteration:
        fx1 = round(f(X1),5)
        fx2 = round(f(X2),5)
        X1=X2  
        X2=X2-((fx2*(X1-X2)/fx1-fx2))
        print(fx1,fx2,X2)
        i+=1
SecantMethod(0,1)

