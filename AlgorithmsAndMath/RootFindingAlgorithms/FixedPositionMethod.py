import math

def f(x):
    return math.sin(math.sqrt(x))

def fixedPositionMethod(x,iteration=10):
    X=x
    i = 0
    while i<iteration:
        fX = f(X)
        print(f(X))
        X=fX
        i+=1
fixedPositionMethod(0.5)
    