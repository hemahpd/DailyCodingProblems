#Given an array of integers, return a new array such that each element at index i 
#of the new array is the product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 
#60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].



l=list(map(int,input().split(',')))
n=len(l)
res=[]
for i in range(n):
    pro=1
    for j in range(n):
        pro=pro*l[j]
    ans=pro/l[i]
    res.append(int(ans))
print(res)