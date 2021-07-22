#if else statement
x = int(input("Enter a number:"))
if x == 0:
    print("Number is 0 and is nor odd neither even")
else:
    if x > 0:
        print("Number is Positive")
        if (x%2) == 0:
            print("Number is even")
        else:
            print("Number is odd")
    else:
        print("Number is Negative")
        if (x%2) == 0:
            print("Number is even")
        else:
            print("Number is odd") 