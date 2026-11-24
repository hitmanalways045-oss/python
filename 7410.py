n=int(input("Enter no"))
n1,n2=0,1
print("Fibonacci series",n1,n2,end=" ")
i=2
while i<n:
    n3=n1+n2
    n1=n2
    n2=n3
    i+=1
    print(n3,end=" ")
print()
