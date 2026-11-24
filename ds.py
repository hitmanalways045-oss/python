n=int(input("Enter n:"))
temp=n
rev=0
for i in range(len(str(n))):
    d=temp%10
    rev=rev*10+d
    temp=temp//10
if rev==n:
    print("Palin")
else:
    print("NP")
