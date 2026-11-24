x=int(input('Enter the number'))
n=int(input('Enter the number'))
s=1
for i in range(1,n+1):
    s+=1/i**3
print("Sum of Series",s)
