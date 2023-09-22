#This code appends the user's text file and writes two separate files (squared and cubed) from it. 
#The first file will contain all numbers from the user's file multiplied to two while the second file contains the user's file multiplied to three.
#The user should have a text (.tx) file named "numbers" containing integers in order for the code to be read.

with open("numbers.txt") as a:
    integers = [int(x) for x in a.read().split()]

with open("squared.txt", "w") as a:
    for num in integers:
        if num % 2 == 0:
            a.write((str(num ** 2)+ "\n"))

with open("cubed.txt", "w") as a:
    for num in integers:
        if num % 2 == 1:
            a.write((str(num ** 3)+ "\n"))
