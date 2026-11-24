n=int(input("Enter a number"))
temp=n
s=0
digits=len(str(n))
while temp>0:
    d=temp%10
    s+=d**digits
    temp=temp//10
if n==s:
    print("Armstrong")
else:
    print("Non armstrong")
