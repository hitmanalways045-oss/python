n=int(input("Enter no"))
temp=n
s=0
digits=len(str(n))
while temp>0:
    d=temp%10
    s=s+d**digits
    temp//=10
if n==s:
    print("Armstrong")
else:
    print("N-armstrong")
