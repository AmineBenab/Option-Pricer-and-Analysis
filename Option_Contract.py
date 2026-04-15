from dataclasses import dataclass

@dataclass
class OptionContract: 
    opt_type : str
    obs_type : str
    spot : float
    strike : float
    sigma : float
    maturity : float
    risk_free : float
    div : float = 0
    repo : float = 0 

    def __post_init__(self): 
        self.opt_type = self.opt_type.lower()
        self.obs_type = self.obs_type.lower()
        assert self.opt_type in ["call", "put"]
        assert self.obs_type in ["european", "american"]
    
    
    