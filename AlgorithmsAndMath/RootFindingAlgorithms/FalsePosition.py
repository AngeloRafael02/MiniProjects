import math
def f(x):
    """Change your Equations Here"""
    return (math.e**-x)-x
def FalsePositionMethod(XL,XU,iteration=10,error=10):
    xL = XL
    xU = XU
    i=0
    while i < iteration:
        fxL = f(xL)
        fxU = f(xU)
        xR  = xU-(fxU*(xL-xU))/(1-fxU)
        fxR = f(xR)
        Ea = abs((xU-xL)/(xU+xL))*100
        if fxL*fxR <0:
            xU = xR
            print("xL:"+str(xL)+" xU:"+str(xU)+" f(xL):"+str(fxL)+" f(xU):"+str(fxU)+" xR:"+str(xR)+" f(xR):"+str(fxR)+" Ea:"+str(Ea))
            i+=1
        elif fxL*fxR  > 0:
            xL=xR
            print("xL:"+str(xL)+" xU:"+str(xU)+" f(xL):"+str(fxL)+" f(xU):"+str(fxU)+" xR:"+str(xR)+" f(xR):"+str(fxR)+" Ea:"+str(Ea))
            i+=1
        elif fxL*fxR  == 0 or error > Ea:
            print("xL:"+str(xL)+" xU:"+str(xU)+" f(xL):"+str(fxL)+" f(xU):"+str(fxU)+" xR:"+str(xR)+" f(xR):"+str(fxR)+" Ea:"+str(Ea))
            break




    


FalsePositionMethod(0.5,1)