# main.py
from ticker import Ticker
from base import OPTION_TYPE    
from black_scholes import BlackScholesModel
from monte_carlo import MonteCarloPricing
from binomial_tree import BinomialTreeModel

def main():
    # User inputs
    ticker_symbol = 'AAPL'
    start_date = '2023-05-01'
    end_date = '2023-12-31'
    option_type = OPTION_TYPE.CALL_OPTION.value
    S = 152  # Current stock price
    K = 155  # Strike price
    T = 30  # Time to maturity in days
    r = 0.01  # Risk-free rate
    sigma = 0.2  # Volatility

    # Fetch historical data
    data = Ticker.get_historical_data(ticker_symbol, start_date, end_date)
    if data is not None:
        last_price = Ticker.get_last_price(data, 'Close')
        print(f"Last price of {ticker_symbol}: {last_price}")

    # Black-Scholes Model
    bs_model = BlackScholesModel(S, K, T, r, sigma)
    bs_option_price = bs_model.calculate_option_price(option_type)
    print(f"Black-Scholes {option_type} price: {bs_option_price}")
    # Monte Carlo Simulation
    num_simulations = 10000
    mc_model = MonteCarloPricing(S, K, T, r, sigma, num_simulations)
    mc_model.simulate_prices()
    mc_option_price = mc_model.calculate_option_price(option_type)
    print(f"Monte Carlo {option_type} price: {mc_option_price}")

    # Binomial Tree Model
    num_steps = 100
    bt_model = BinomialTreeModel(S, K, T, r, sigma, num_steps)
    bt_option_price = bt_model.calculate_option_price(option_type)
    print(f"Binomial Tree {option_type} price: {bt_option_price}")

if __name__ == "__main__":
    main()
