#!/usr/bin/env python3

def main():
	""" Run-time Code """
	
	# Create a small string
	lilstring = "Alta3 Research offers classes on pythong coding"
	newlist = lilstring.split(" ") # this returns a list
	print(newlist)

	# create a list of strings
	myiplist = ["192", "168", "0", "12"]
	# set singleip as the result of joining the list myiplist around the "."
	singleip = ".".join(myiplist)
	# display single ip
	print(singleip)

# Call out main function
main()

