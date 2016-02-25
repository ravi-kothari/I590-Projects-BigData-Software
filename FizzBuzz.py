#import sys

n=int(raw_input("Enter an integer: "))
print "Fizz buzz counting up to " + str(n)

def fizzbuzz(n):
    for num in n:
        if (num%2 == 0) and (num%3 == 0):
            print("fizzbuzz")
        elif num%2 == 0:
            print("fizz")
        elif num%3 == 0:
            print("buzz")
        else:
            print(num)

fizzbuzz(range (1,n+1))