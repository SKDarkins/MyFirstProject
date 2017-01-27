"""
Sasha's first class.

Run as:
python MyFirstClass.py
"""

import sashas_animals
		
class Customer():

	def __init__(self, name):

		self.name = name
		self.amountowed = 0
		
customer_names_from_website = ["Bob", "Fred", "Ben"]
my_customers = []

for eachCumsterName in customer_names_from_website:
	my_customers.append(Customer(eachCumsterName))

# Our price is 5 dolla per week

for eachWeek in range(12):

	for eachCustomer in my_customers:
		eachCustomer.amountowed += 5
		
# Make a report

for eachCumstor in my_customers:
	print "Name: ", eachCumstor.name, " Owes Us: ", eachCumstor.amountowed
