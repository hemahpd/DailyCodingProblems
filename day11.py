#This problem was asked by Twitter.

#Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

#For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].



str=list(input("Enter string list").split())
pre=input("Enter prefix:")
l=len(pre)
a=[]
for i in str:
    if i[:l]==pre:
        a.append(i)
print(a)