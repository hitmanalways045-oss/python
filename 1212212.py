s=input("Enter Str:")
b=''
for i in s[::-1]:
    b=b+i
if s==b:
    print("p")
else:
    print("np")
