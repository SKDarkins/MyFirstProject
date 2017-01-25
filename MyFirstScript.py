"""
Sasha's first script.

Run as:
python MyFirstScript.py
"""

my_words = ["Doug", "the", "Pug"]
check_word = "Doug"

for eachWord in my_words:

	# Check for our special word
	if check_word in eachWord:
		print "We found Doug!"
	else:
		print "We found something else"
		print eachWord
	