#

x=10
y=5
print("arithmetic operators.......................................")

print("sum :", x+y)
print("difference :", x-y)
print("product :", x*y)
print("quotient :", x/y)
print("remainder :", x%y)
print("power :", x**y)


# comparison operators

print("comparison operators.......................................")

print("Is x equal to y ? ", x==y)
print("Is x not equal to y ? ", x!=y)
print("Is x greater than y ? ", x>y)
print("Is x less than y ? ", x<y)
print("Is x greater than or equal to y ? ", x>=y)
print("Is x less than or equal to y ? ", x<=y)

# logical operators

x=10
y=5

print("logical operators.......................................")

print("Is x greater than y and less than x ? ", x>y and x<x)
print("Is x greater than y or less than x ? ", x>y or x<x)
print("Is x not greater than y ? ", not(x>y))


#assignment operators
print("assignment operators.......................................")
a= 2 
b=3

a=a+6
a+=6
print("a after addition assignment operator :", a)

a=a-2
a-=2
print("a after subtraction assignment operator :", a)

a=a*3
a*=3
print("a after multiplication assignment operator :", a)

a=a/2
a/=2
print("a after division assignment operator :", a)