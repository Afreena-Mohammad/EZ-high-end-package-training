# take the input from the user in the given format (consist of name and code)find the max digit from the code
#which is less or equal to the length to the length of the string and put that place char
#in final string if there is no any digit found which not satisfy the condition and simply put 'x'.
#input :Abhishek:43848,mayur:3749,friend:3939,yeah:7878
#output:kuex
s=input()
los=s.split(',')
op=''
for i in los:
    nc=i.split(':')
    name=nc[0]
    code=nc[1]
    print(name,code)
    max=0
    for i in code:
        if int(i)>max and int(i)<=len(name):
            max=int(i)
    if max==0:
        op+='x'
    else:
        op+=name[max-1]
print(op)
        
            