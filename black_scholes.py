# black_scholes.py
import numpy as np
from scipy.stats import norm
from option_pricing_model import OptionPricingModel, OPTION_TYPE

class BlackScholesModel(OptionPricingModel):
    def __init__(self, S, K, T, r, sigma):
        self.S = S
        self.K = K
        self.T = T / 365.0
        self.r = r
        self.sigma = sigma

    def _calculate_call_option_price(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        call_price = self.S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        return call_price

    def _calculate_put_option_price(self):
        d1 = (np.log(self.S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        put_price = self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - self.S * norm.cdf(-d1)
        return put_price

