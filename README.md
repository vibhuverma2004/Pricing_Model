# Pricing Model  

This project implements multiple option pricing models and provides functionality to fetch and visualize stock data from Yahoo Finance. It serves as a comprehensive framework for analyzing and estimating option prices in financial markets.  

## Features  

- **Option Pricing Models:**  
  - **Black-Scholes Model:** Closed-form solution for European call and put options.  
  - **Binomial Tree Model:** Discrete-time method to approximate option prices using a binomial tree.  
  - **Monte Carlo Simulation:** Stochastic approach to simulate stock price paths and calculate option prices.  

- **Stock Data Fetching:**  
  - Fetch historical stock data using the `pandas-datareader` library.  
  - Retrieve specific stock information, including adjusted closing prices and the last recorded price.  
  - Visualize stock price trends over time using `matplotlib`.  

- **Testing Framework:**  
  - Comprehensive tests for all models.  
  - Demonstrates stock data fetching and option pricing calculations.  


## Functionality  

### Stock Data Fetching  

- Fetch historical stock data for analysis and modeling.  
- Visualize historical trends to better understand price movements.  

### Visualization  

- Generate plots of stock prices to gain insights into historical performance and trends.  

### Testing  

- Validate model implementations using the `test_script.py`.  
- Outputs option prices and visualizes stock data.  

## Conclusion  

This project demonstrates the application of three prominent option pricing models alongside stock data fetching and visualization. The tools provided here enable robust analysis and modeling of financial options in real-world scenarios.  
