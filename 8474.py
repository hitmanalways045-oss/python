d={}
n=int(input("Enter How many"))
for i in range(n):
    name=input("Enter name")
    p=input("Enter no.")
    d[name]=p
while True:
    print("1.Display")
    print("2.Add")
    print("3.Delete")
    print("4.Modify")
    print("5.Check")
    print("6.Sort")
    print("7.Exit")
    ch=int(input("Enter Choice"))
    if ch==1:
        print(d)
    if ch==2:
        n=input("Enter name")
        p=int(input("Enter Ph.no"))
        d[n]=p
        print(d)
    if ch==3:
        n=input("Enter name")
        if n in d:
            del[n]
        else:
            print("Not Found")
    if ch==4:
        n=input("Enter Name")
        if n in d:
            p=int(input("Enter ph.no"))
            d[n]=p
    if ch==5:
        n=input("Enter Name")
        if n in d:
            print("Found")
        else:
            print("Not Found")
    if ch==6:
        for k in sorted(d.keys()):
            print(k,":",d[k])
    if ch==7:
        print("Exit")
        break
