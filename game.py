a=int(input("Enter a"))
b=int(input("Enter b"))
c=int(input("Enter c"))
d=int(input("Enter d"))
e=int(input("Enter e"))
if a > b and a > c and a > d and a > e:
    print("The greatest number is", a)
elif b > c and b > d and b > e:
    print("The greatest number is", b)
elif c > d and c > e:
    print("The greatest number is", c)
elif d > e:
    print("The greatest number is", d)
else:
    print("The greatest number is", e)
