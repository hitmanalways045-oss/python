n=5
for i in range(n,0,-1):
    s=(n-i)*" "
    print(s,end="")
    for j in range(1,i+1):
        print(j,end="")
    print()
