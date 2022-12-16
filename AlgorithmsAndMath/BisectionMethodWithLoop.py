import math



def f(x):
    """Adjust your equation after the return keyword"""
    return (math.e**-x)-x
def bisectionMethod(xl,xr,iteration=10,error=10):
    xL = xl
    xU = xr
    i=0
    while i < iteration:
        fxL = f(xL)
        fxU = f(xU)
        xR = (xL + xU)/2
        fxR = f(xR)
        Ea = abs((xU-xL)/(xU+xL))*100
    #print(f(xL)*f(xR))
        if f(xL)*f(xR) < 0:
            xU=xR
            print("xL:"+str(xL)+" xU:"+str(xU)+" f(xL):"+str(fxL)+" f(xU):"+str(fxU)+" xR:"+str(xR)+" f(xR):"+str(fxR)+" Ea:"+str(Ea))
            i+=1
        elif f(xL)*f(xR) > 0:
            xL=xR
            print("xL:"+str(xL)+" xU:"+str(xU)+" f(xL):"+str(fxL)+" f(xU):"+str(fxU)+" xR:"+str(xR)+" f(xR):"+str(fxR)+" Ea:"+str(Ea))
            i+=1
        elif f(xL)*f(xR) == 0 or error > Ea:
            print("xL:"+str(xL)+" xU:"+str(xU)+" f(xL):"+str(fxL)+" f(xU):"+str(fxU)+" xR:"+str(xR)+" f(xR):"+str(fxR)+" Ea:"+str(Ea))
            break
bisectionMethod(0.5,1)
        




