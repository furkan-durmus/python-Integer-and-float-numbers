# Given a positive real number, print its first digit to the right of the decimal point.
a=float(input("Input a number: "))
print(int((a-int(a))*10))

# Or

x = float(input())
print(int(x * 10) % 10)