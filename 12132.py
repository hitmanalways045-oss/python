def s(student,n1):
    if n1 in student:
        return True
    else:
        return False
student=()
n=int(input('Enter how many:'))
for i in range(n):
    name=input("Enter name")
    student+=(name,)
n1=input("Enter name to search")
if (student,n1):
    print("Found")
else:
    print("Not found")
