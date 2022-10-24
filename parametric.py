import numpy as np
n=80
theta = np.linspace(0,2*np.pi,n+1)
def get_x(e,me,l,v,d,w2,phase,sinusoidal,v2):
    if sinusoidal:
        b2 =(np.sin(w2*(theta+phase)))
        x = (e/me)*((l*b2)/((v**2)*d))
        return x
    else:
        x = (e/me)*((l*v2)/((v**2)*d))
        return x

def get_y(e,me,l,v,d,w,sinusoidal,v2):
    if sinusoidal:
        b1 =(np.sin(w*theta))
        y = (e/me)*((l*b1)/((v**2)*d))
        return y
    else:
        y = (e/me)*((l*v2)/((v**2)*d))
        return y


def createIndexes(cants):
    size = len(cants)
    result=[]
    cont =0
    for i in range(0,size):
        result.append(cont)
        cont+=1
    return result