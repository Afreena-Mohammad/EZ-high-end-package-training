#you are given an array of n integers and another integer k.how many numbers appear in the arry atleast k times?
#standard input
#the first line contains two integers n and k
#the second line contains n integers,representing the elements of the array.
#standard output:print the answer on the first line.
#example: input:3 1
#1 1 1 output:1 
n,k=map(int,input().split())
lst=[]
for i in range(n):
    lst.append(int(input()))
s,c=set(lst),0
for i in s:
    if lst.count(i)>=k:
        c+=1
print(c) 