# A cupcake costs A dollars and B cents. Determine, how many dollars and cents should one pay for N cupcakes.
# A program gets three numbers: A, B, N. It should print two numbers: total cost in dollars and cents.

a= float(input())
b= int(input())
n= int(input())
a=a+(b*(10**-2))
print(a*n)

# Or


a= int(input())
b= int(input())
n= int(input())
print(a*n+b*n//100,b*n%100)

# Or

a = int(input())
b = int(input())
n = int(input())
cost = n * (100 * a + b)
print(cost // 100, cost % 100)