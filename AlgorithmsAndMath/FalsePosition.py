import math
def f(x):
    """Change your Equations Here"""
    return (math.e**-x)-x
def FalsePositionMethod(XL,XU):
    xL = XL
    xU = XU
    xR  = xU-(f(xU)*(xL-xU))/(1-f(xU))
    print("xL:"+str(xL) + " xU:"+str(xU)+" f(xL):"+str(f(xL))+" f(xU):"+str(f(xU))+" xR:"+str(xR)+" f(xR):"+str(f(xR))+" f(xL)*f(xR):"+str(f(xL)*f(xR)))



    


FalsePositionMethod(0,0.5722) #for now, loop function with changing arguments
