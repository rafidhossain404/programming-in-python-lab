# Print Fibonacci numbers below a given user input N.
x=int(input("Enter the number: "))
a=0
b=1
for i in range(0,x):
  c=a+b
  a=b
  b=c
  print(a)
