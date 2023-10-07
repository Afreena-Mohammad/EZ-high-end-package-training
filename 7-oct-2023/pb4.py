#reverse the given string and keeping its special character at the same place
#example:
#input:srin#ivas
#output:savi#nirs
#input:we@lcome
#output:em@oclem
#input:pyth#on
#output:noht#yp
'''s=input()
r=s[::-1]
print(r)
sp=["@","#","&","$"]
for i in range(len(s)):
   for sp in s:
       if s[i]==sp:'''
def demo(s):
    l=[]
    for i in s:
        if i.isalpha():
            l.append(i)
        else:
            spc=i
            idxspc=s.index(i)
    l.reverse()
    l.insert(idxspc,spc)
    return ''.join(l)
s=input()
print(demo(s))
           
      