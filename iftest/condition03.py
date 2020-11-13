#!/usr/bin/env python3

hostname = input("What value should we set for the hostname? : ")

## Notice how the next line has changed
## here we use the str.lower() method to reutrn a lowercase string
if hostname.lower() == "mtg":
	print("The hostname was found to be mtg")
	print("The hostname matches expected config")

## Exiting the script
print("Exiting the script now")

