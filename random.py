num = int(input("Enter a number between 1 and 5: "))
if num > 5 or num < 1:
    print("Error: incompatible number")
else:
    if num % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")
    if num != 4:
        print("The number is prime")
    else:
        print("The number is not prime")
