#!/usr/bin/env python3

# create the list called vendors
vendors = ["cisco", "juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]

# loop across the list vendors
for x in vendors:
    print("\nThe Vendor is: " + x, end=" ") # newline, print current vendor, and end without Newline
    if x not in approved_vendors: # if x does not appear within the list approved_vendors
        print(" -NOT AN APPROVED VENDOR!", end="")
print("\nOur loop has ended!!") # when the loop ends print this

