from math import sqrt
number=int(input("Enter the number:"))
if number>1:
    for i in range (2,int(sqrt(number))+1):
        if(number%i)==0:
            print("The number isn't a prime number.")
            break
    else:
        print("the number is a prime number")
else:
    print("the number isn't a prime number.")