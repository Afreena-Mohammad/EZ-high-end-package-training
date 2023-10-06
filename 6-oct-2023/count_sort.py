arr=[2,1,1,0,2,5,4,0,2,8,7,7,9,2,0,1,9]
x=[]
for i in range(len(arr)):
    print(arr.count(i))
    x.append(arr.count(i))
print(x)
t=0
updated_arr=[]
for n in range(0,len(x)):
    t=t+x[n]
    updated_arr.append(t)
print(updated_arr)

for j in range(0,len(updated_arr)):
    a=arr[j]
    arr[j]=updated_arr[a]
    