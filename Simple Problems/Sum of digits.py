# Given a three-digit number. Find the sum of its digits.

a= int(input("Input an integer: "))

print(a//100+a//10%10+a%10)