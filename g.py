n=int(input("Enter n"))
s=0
for i in range(len(str(n))):
    d=n%10
    s=s+d
    n=n//10
print("S",s)
