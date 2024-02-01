import numpy as np

#return price as a function of time
def GBM(numSteps, mean, stDev, initial, t):
    pStep = [(mean - (np.square(stDev))/2) + np.random.randn()*stDev for s in range(numSteps)]
    p = initial*np.exp(np.cumsum(pStep))
    t = []
    for i in range(numSteps):
        time = t * i
        t.append(time)
    return t,p