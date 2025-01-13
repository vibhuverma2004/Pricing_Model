# monte_carlo.py
import numpy as np
import matplotlib.pyplot as plt
from option_pricing_model import OptionPricingModel

class MonteCarloPricing(OptionPricingModel):
    def __init__(self, S, K, T, r, sigma, num_simulations):
        self.S = S
        self.K = K
        self.T = T / 365.0
        self.r = r
        self.sigma = sigma
        self.num_simulations = num_simulations
        self.simulated_prices = []

    def simulate_prices(self):
        dt = self.T / self.num_simulations
        prices = np.zeros((self.num_simulations, 1))
        prices[0] = self.S
        for t in range(1, self.num_simulations):
            prices[t] = prices[t - 1] * np.exp((self.r - 0.5 * self.sigma**2) * dt + self.sigma * np.sqrt(dt) * np.random.normal())
        self.simulated_prices = prices

    def plot_simulation_results(self, num_movements):
        for i in range(num_movements):
            plt.plot(self.simulated_prices)
        plt.title('Monte Carlo Simulation of Stock Prices')
        plt.xlabel('Time Steps')
        plt.ylabel('Stock Price')
        plt.show()

    def _calculate_call_option_price(self):
        payoffs = np.maximum(self.simulated_prices[-1] - self.K, 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)

    def _calculate_put_option_price(self):
        payoffs = np.maximum(self.K - self.simulated_prices[-1], 0)
        return np.exp(-self.r * self.T) * np.mean(payoffs)
