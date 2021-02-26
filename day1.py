print("Enter list elements space separated")
l=list(map(int,input().split()))
k=int(input("enter k value:"))
n=len(l)
s=False
for i in range(n):
    for j in range(i+1,n):
        if l[i]+l[j]==k:
                s=True
                break
print(s)
            
