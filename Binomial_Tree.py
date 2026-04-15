from Option_Contract import OptionContract
import numpy as np


def crr_price(option, n):
    dt = option.maturity/ n
    u = np.exp(option.sigma*np.sqrt(dt))
    d = np.exp(-option.sigma*np.sqrt(dt))
    p = (np.exp((option.risk_free-option.div)*dt)-d)/(u-d)
    
    i = np.arange(0,n+1)
    ST = option.spot*(u**i)*(d**(n-i))
    if option.opt_type == "call":
        payoff = np.maximum(ST-option.strike, 0)
    else :
        payoff = np.maximum(option.strike-ST,0)
    V = payoff
    for i in range (n):
        V = np.exp(-option.risk_free*dt)*(p*V[1:]+(1-p)*V[:-1])
        if option.obs_type == "american" :
            j = n - i - 1
            Si = option.spot*(u**(np.arange(j+1)))*(d**(j-np.arange(j+1)))
            if option.opt_type == "call":
                V = np.maximum(V,Si-option.strike)
            else : 
                V = np.maximum(V,option.strike-Si)
    return V[0]