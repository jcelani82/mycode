#!/usr/bin/env python3

ipchk = input("Apply an IP Address: ")

# a provided string will test true
if ipchk:
	print("Looks like the IP Address was set: " + ipchk) 
else:	# if data was not provided
	print("You did not provide input.")
