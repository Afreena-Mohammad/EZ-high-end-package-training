# print number of pairs of inversions 
def inversion(n):
    count=0
    a=len(n)
    for i in range(a-1):
        for j in range(i+1,a):
            if n[i] >n[j]:
                count+=1
    return count
n=list(map(int,input().split()))
k=inversion(n)
print(k)