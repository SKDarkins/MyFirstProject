"""
Sasha's first script.

Run as:
python MyFirstScript.py
"""

def find_doug(list_of_words): # Function

	""" Check if Doug is in the list
	"""

	check_word = "Doug" #string

	for eachWord in list_of_words: # for loop

		# Check for our special word
		if check_word in eachWord: # if statement
			print "We found Doug!" # print statement
		else:
			print "We found something else"
			print eachWord
			
def number_fun(an_integer, a_float):

	"""Perform some numerical operations on the input
	"""
	
	a = an_integer + 5 # addition
	b = a_float + 5.0

	c = an_integer - 5 # subtraction
	d = a_float - 5.0

	e = an_integer * 5 # mult
	f = a_float * 5.0

	print a, b, c, d, e, f
	
an_integer = 9
a_float = 5.2
number_fun(an_integer, a_float)

an_integer = 39
a_float = 53333.25757573463636
number_fun(an_integer, a_float)


#my_words = ["Doug", "the", "Pug", "is", "cooler", "than", "you"] #List of strings			
#find_doug(my_words)