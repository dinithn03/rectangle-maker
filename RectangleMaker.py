#Name: Dinith Nawaratne
#Purpose: Ask the user for the length and height of a rectangle, and then prints it on the screen using asterisks
#Date: November 6th, 2018

#Printing the title
print("Rectangle Maker")
print("---------------")

again = "y"

#Creating the while and for loops
#The first for loop is to print the full rectangle with the middle filled in
#The second for loop prints the asterisks across (*******) if it's the first or last number, otherwise, prints asterisks twice (*     *)
while again == "y" or again == "Y":
    L = int(input("\nEnter the length: "))
    w = int(input("Enter the width: "))
    print()
    for i in range(1, w+1):
        print("*" * L)

    again = input("\nWould you like to run the program again? (Y/N): ")
    
    
    
     
