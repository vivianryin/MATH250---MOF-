"""
Sample file for homework 1

please implement the given functions

TODO: rename this file to `homework.py` before submitting to gradescope.
"""

def hello(name):
	""" A simple function that returns a greeting """
	
	return "Hello, {}!".format(name)
	pass


def future_value(amount, rate, years, periods_per_year=1):
	"""
	Use compound interest to compute what a present amount will be worth in
	the future.

	Args:
		amount (float): the present amount of money
		rate (float): the interest rate in decimal form
		years (int): the number of years
	
	Kwargs:
		periods_per_year (int): how many times a year to compound [default: 1]

	Returns:
		future (float).  Amount after compound interest has been applied.
	"""
	future = amount*(1+(rate/periods_per_year))**(years*periods_per_year) 
	#This function takes the present value and compute the future value according to the rate and compunding frequency 
	return future
	pass



def present_value(amount, rate, years, periods_per_year=1):
	"""
	Suppose you have access to an instrument with an interest rate of `rate`,
	compounded `periods_per_year` times a year.  What is the present value
	to you of a payment of `amount` paid `years` years in the future?

	Args:
		amount (float): the amount of the future payment
		rate (float): the interest rate in decimal form
		years (int): the number of years
	
	Kwargs:
		periods_per_year (int): how many times a year to compound [default: 1]

	Returns:
		future (float).  Present value of the future payment
	"""
	future = amount*(1+(rate/periods_per_year))**(-1*(periods_per_year*years)) #the equation to compute the present value of the payment
	return future
	pass
