#Hour hand turned by α degrees since the midnight. Determine the angle by which minute hand turned since the start of the current hour.
# Input and output in this problems are floating-point numbers.

a=float(input())
print(a%60*12%360)