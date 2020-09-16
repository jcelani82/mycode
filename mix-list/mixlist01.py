#!/usr/local/bin/python3

# Create a list and insert values into that list
my_list = [ "192.168.0.5", 5060, "UP"]

#Print the First item 
print("The first item in the list (IP): " + my_list[0] )

#Print the Second item as a string
print("The Second item in the list (port): " + str(my_list[1]) )

#Print the Thrid item
print("The Thrid item in the list (state): " + my_list[2] ) 

#Printing Multiple Values

#Create a new list and add the variables into it
new_list = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh"]

#Creating the sentence
print("When I " + new_list[5] + " into IP Addresses " + new_list[3] + " or " + new_list[4] + " I am unale to ping ports " + str(new_list[0]) + ", " + new_list[1] + ", " + str(new_list[2]) + ".")
