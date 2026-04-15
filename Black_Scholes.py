import numpy as np
from scipy.stats import norm
from Option_Contract import OptionContract
import pandas as pd 

# faudrait créer des var plus courtes v = option.var
def d1_d2(option):
    d1 = (np.log(option.spot/option.strike)+(option.risk_free-option.div+(option.sigma**2)/2)*option.maturity)/(option.sigma*np.sqrt(option.maturity))
    d2 = d1 - option.sigma*np.sqrt(option.maturity)
    return d1,d2 
def bs_price(option):
    div_disc = np.exp(-option.div*option.maturity)
    rf_disc = np.exp(-option.risk_free*option.maturity)
    d1,d2 = d1_d2(option)
    price = 0 
    if option.opt_type == "call":
        price = option.spot * div_disc*norm.cdf(d1) - option.strike *rf_disc *norm.cdf(d2)
    elif option.opt_type =="put":
         price = -option.spot * div_disc*norm.cdf(-d1) + option.strike * rf_disc *norm.cdf(-d2)
    else : 
        print("Is it a call or a put ?")
    return price 
    
def greeks_bs(option):
    d1,d2 = d1_d2(option)
    div_disc = np.exp(-option.div*option.maturity)
    rf_disc = np.exp(-option.risk_free*option.maturity)
    gamma = (div_disc*norm.pdf(d1))/(option.spot*option.sigma*np.sqrt(option.maturity)) 
    vega = option.spot * div_disc *norm.pdf(d1)*np.sqrt(option.maturity)
    theta = - (option.spot *  div_disc * norm.pdf(d1)*option.sigma)/(2*np.sqrt(option.maturity)) \
    - option.risk_free * option.strike * rf_disc * norm.cdf(d2) \
    + option.div * option.spot * div_disc * norm.cdf(d1)
    if option.opt_type == "call" : 
        delta = div_disc*norm.cdf(d1)
        rho = option.strike*option.maturity*rf_disc*norm.cdf(d2)
    elif option.opt_type == "put":
        delta = - div_disc * norm.cdf(-d1)
        rho = -option.strike*option.maturity*rf_disc*norm.cdf(-d2)
    df_greeks = pd.DataFrame({"Value":[delta, gamma, vega, theta, rho]},index = ["Delta", "Gamma", "Vega", "Theta", "Rho"])
    return df_greeks
    
    