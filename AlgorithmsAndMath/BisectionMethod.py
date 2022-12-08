import math
def f(x):
    """Change your Equations Here"""
    return (math.e**-x)-x
def BisectionMethod(XL,XU,iteration = 10):
    xL = XL
    xU = XU
    fxL = f(xL)
    fxU = f(xU)
    xR  = (xL+xU)/2
    fxR = f(xR)
    Ea = abs((xU-xL)/(xU+xL))*100
    print(xL, xU, fxL, fxU,xR,fxR,Ea)
    #Condition for changing values still needed


BisectionMethod(0,1)