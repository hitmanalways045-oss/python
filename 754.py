def armstrong(n):
    temp=n
    s=0
    digits=len(str(n))
    for i in range(digits):
        d=temp%10
        s=s++d**digits
        temp=temp//10
    if s==n:
        print("Armstrong")
    else:
        print("Non Armstorng")
n=int(input("Enter n"))
armstrong(n)

