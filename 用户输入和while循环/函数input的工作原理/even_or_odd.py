number = input("Enter a number,and I'll tell you if it't even or odd:")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nnumber " + str(number) + " is odd.")
