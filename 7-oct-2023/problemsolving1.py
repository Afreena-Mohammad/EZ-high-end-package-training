#input:7564168
#example:separate odd place integers:5,4,6 you have to return a 4 digit OTP by squaring the digits.
#digits from above ex:5,4,6
#squares:25,16,36
#so OTP to be returned is first four digits:2516
'''n=input()
n=list(n)
m=[]
for i in range(0,len(n)):
    if i%2!=0:
        n[i]=(int(n[i])**2)
        m.append((n[i]))
res=''.join(map(str,m))
result=int(str(res)[:4])
print(result)'''



n=input()
odd=n[1::2]
s=""
for i in odd:
    s=s+str(int(i)**2)
print(s[:4])



              