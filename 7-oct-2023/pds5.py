#input:A string of comma separated numbers are given such that the numbers 4 and 7 are alaready available
#in the list.Assumption:7 always comes after 4 in the given string.number1=Add all numbers which do not lie b/w
#4 and 7(excluding 4 and 7)in the given input.
#numbers2:numbers formed by cancatinating all numbers from 4 to 7(including 4 n 7)
#o/p:sum of number1 and number2
#example:2,5,1,32,7,8
#number1:2+5+1+8=16
#number2:'4'+'3'+'2'+'7'='4327'
#o/p:16+4327
def demo(s):
    los=s.split(',')
    idxpof=los.index('4')
    idxpos=los.index('7')
    n1,n2=0,''
    for i in los[:idxpof]:
        n1+=int(i)
    for i in los[idxpof:idxpof+1]:
        n2+=i
        return (n1+int(n2))
    
    
s=input()
if __name__=='__main__':
    print(demo(s))