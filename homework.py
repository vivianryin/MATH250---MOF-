"""
Sample file for homework 3

please implement the given functions

TODO: rename this file to `homework.py` before submitting to gradescope.
"""
import numpy as np
from math import comb


def call_payoff(stock, strike):
    """
    Payoff for holding a call option with a given stock price and strike price
    """

    return max(stock-strike, 0)

def put_payoff(stock, strike):
    """
    Payoff for holding a put option with a given stock price and strike price
    """

    # IMPLEMENT THIS PAYOFF FUNCTION
    return max(strike-stock,0)
    pass
a = put_payoff(70,100)
print(a)


def option_pricer(stock, strike, U, D, R, N, payoff_func):
    """
    Give the price of a call or put using a version of Cox-Ross-Rubinstein.

    Args:
        stock (float): price of the asset right now
        strike (float): strike price of the option
        U (float): The up percentage, per step, as a decimal
        D (float): The down percentage, per step, as a decimal
        R (float): The risk-free interest in one step, as a decimal (D < R < U)
        N (int): Number of steps
        payoff_func (function): This is a function that will take a stock price
            and a strike price.
    """
    p = (R-D)/(U-D) #risk-neutral probability
    discount_factor = 1/((1+R)**N)
    option_price = 0
    for i in range (N+1):
        s_t= (((1+U)**i)*((1+D)**(N-i)))*stock # stock price at time T
        payoff = payoff_func(s_t,strike)
        option_price += ((comb(N,i))*((p**i)*((1-p)**(N-i)))*payoff)
    option_price = discount_factor*option_price
    return option_price
    pass