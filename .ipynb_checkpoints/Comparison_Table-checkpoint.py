import numpy as np
import pandas as pd
from Option_Contract import OptionContract
from Black_Scholes import bs_price
from Binomial_Tree import crr_price
from Monte_Carlo_Options import mc_price 

s=float(input("Spot : "))
k=float(input("Strike : "))
sig=float(input("Volatility : "))
mat=float(input("Maturity : "))
rf=float(input("Risk Free Rate : "))
dvd = float(input("Dividends : "))


call_eu = OptionContract(
    opt_type="call",
    obs_type="european",
    spot=s,
    strike=k,
    sigma=sig,
    maturity=mat,
    risk_free=rf,
    div = dvd)

put_eu = OptionContract(
    opt_type="put",
    obs_type="european",
    spot=s,
    strike=k,
    sigma=sig,
    maturity=mat,
    risk_free=rf,
    div = dvd)

call_us = OptionContract(
    opt_type="call",
    obs_type="american",
    spot=s,
    strike=k,
    sigma=sig,
    maturity=mat,
    risk_free=rf,
    div = dvd)

put_us = OptionContract(
    opt_type="put",
    obs_type="american",
    spot=s,
    strike=k,
    sigma=sig,
    maturity=mat,
    risk_free=rf,
    div = dvd)

data = {
    "Black Scholes":[bs_price(call_eu),bs_price(put_eu),bs_price(call_us),bs_price(put_us)],
    "CRR":[crr_price(call_eu,100),crr_price(put_eu,100), crr_price(call_us,100), crr_price(put_us,100)],
    "Monte Carlo":[mc_price(call_eu,10000), mc_price(put_eu,10000), mc_price(call_us,10000), mc_price(put_us,10000)]
}
df = pd.DataFrame(data, index = ["Call EU", "Put EU", "Call US", "Put US"])

df