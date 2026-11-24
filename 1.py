d={}
n=int(input("Enter How many Friends: "))
for i in range(n):
    n1=input("Enter name: ")
    p=int(input("Enter Ph.no: "))
    d[n1]=p
while True:
    print("1.Display")
    print("2.Add")
    print("3.Delete")
    print("4.Modify")
    print("5.Check")
    print("6.Sort")
    print("7.Exit")
    ch=int(input("Enter Choice: "))
    if ch==1:
        print(d)
    if ch==2:
        name=input("Enter Name")
        p=int(input("Enter ph.no"))
        d[name]=p
        print(d)
    if ch==3:
        name=input("Enter Name")
        if name in d:
            del d[name]
        else:
            print("Not Found")
    if ch==4:
        name=input("Enter Name")
        if name in d:
            p=int(input("Enter no"))
            d[name]=p
    if ch==5:
        name=input("Enter Name")
        if name in d:
            print("Found")
        else:
            print("Not Found")
    if ch==6:
        for k in sorted(d.keys()):
            print(k,":",d[k])
    if ch==7:
        print("Exit")
        break
