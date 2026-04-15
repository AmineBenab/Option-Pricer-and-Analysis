import numpy as np
from Option_Contract import OptionContract
from Black_Scholes import bs_price
from Binomial_Tree import crr_price


def mc_price(option, nb_simulations):
    Z = np.random.standard_normal(nb_simulations)
    ST = option.spot * np.exp((option.risk_free - option.div - ((option.sigma)**2)/2)*option.maturity \
                        + option.sigma*np.sqrt(option.maturity)*Z)
    if option.opt_type == "call":
        payoff = np.maximum(ST-option.strike,0)
    else : 
        payoff = np.maximum(option.strike-ST,0)
    moy_mc = np.mean(payoff)
    return np.exp(-option.risk_free*option.maturity)*moy_mc 