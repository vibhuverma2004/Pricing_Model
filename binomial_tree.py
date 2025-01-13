# binomial_tree.py
import numpy as np
from option_pricing_model import OptionPricingModel

class BinomialTreeModel(OptionPricingModel):
    def __init__(self, S, K, T, r, sigma, num_steps):
        self.S = S
        self.K = K
        self.T = T / 365.0
        self.r = r
        self.sigma = sigma
        self.num_steps = num_steps

    def _calculate_call_option_price(self):
        dt = self.T / self.num_steps
        u = np.exp(self.sigma * np.sqrt(dt))
        d = 1 / u
        p = (np.exp(self.r * dt) - d) / (u - d)
        disc = np.exp(-self.r * dt)

        prices = np.zeros((self.num_steps + 1, self.num_steps + 1))
        prices[0, 0] = self.S

        for i in range(1, self.num_steps + 1):
            for j in range(i + 1):
                prices[j, i] = self.S * (u ** (i - j)) * (d ** j)

        call_values = np.maximum(0, prices[:, self.num_steps] - self.K)

        for i in range(self.num_steps - 1, -1, -1):
            for j in range(i + 1):
                call_values[j] = disc * (p * call_values[j] + (1 - p) * call_values[j + 1])

        return call_values[0]

    def _calculate_put_option_price(self):
        dt = self.T / self.num_steps
        u = np.exp(self.sigma * np.sqrt(dt))
        d = 1 / u
        p = (np.exp(self.r * dt) - d) / (u - d)
        disc = np.exp(-self.r * dt)

        prices = np.zeros((self.num_steps + 1, self.num_steps + 1))
        prices[0, 0] = self.S

        for i in range(1, self.num_steps + 1):
            for j in range(i + 1):
                prices[j, i] = self.S * (u ** (i - j)) * (d ** j)

        put_values = np.maximum(0, self.K - prices[:, self.num_steps])

        for i in range(self.num_steps - 1, -1, -1):
            for j in range(i + 1):
                put_values[j] = disc * (p * put_values[j] + (1 - p) * put_values[j + 1])

        return put_values[0]
