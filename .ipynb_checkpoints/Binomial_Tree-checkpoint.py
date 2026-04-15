{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "ed895a3c-840f-4309-b562-9cea70a45b46",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Option_Contract import OptionContract\n",
    "import numpy as np\n",
    "\n",
    "\n",
    "def crr_price(option, n):\n",
    "    dt = option.maturity/ n\n",
    "    u = np.exp(option.sigma*np.sqrt(dt))\n",
    "    d = np.exp(-option.sigma*np.sqrt(dt))\n",
    "    p = (np.exp((option.risk_free-option.div)*dt)-d)/(u-d)\n",
    "    \n",
    "    i = np.arange(0,n+1)\n",
    "    ST = option.spot*(u**i)*(d**(n-i))\n",
    "    if option.opt_type == \"call\":\n",
    "        payoff = np.maximum(ST-option.strike, 0)\n",
    "    else :\n",
    "        payoff = np.maximum(option.strike-ST,0)\n",
    "    V = payoff\n",
    "    for i in range (n):\n",
    "        V = np.exp(-option.risk_free*dt)*(p*V[1:]+(1-p)*V[:-1])\n",
    "        if option.obs_type == \"american\" :\n",
    "            j = n - i - 1\n",
    "            Si = option.spot*(u**(np.arange(j+1)))*(d**(j-np.arange(j+1)))\n",
    "            if option.opt_type == \"call\":\n",
    "                V = np.maximum(V,Si-option.strike)\n",
    "            else : \n",
    "                V = np.maximum(V,option.strike-Si)\n",
    "    return V[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1972ecbb-b937-457b-99b6-f6522aa16841",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Put européen  : 5.5536\n",
      "Put américain : 6.0824\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e45958f0-3e02-4dcc-b52f-ade30e9423e0",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
