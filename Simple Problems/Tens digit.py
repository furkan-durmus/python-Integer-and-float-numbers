#Given an integer. Print its tens digit.

a = int(input("Input an integer: "))
print(int(a % 100/10))

# Or

n = int(input("Input an integer: "))
print(n // 10 % 10)