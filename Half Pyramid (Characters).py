#Half Pyramid of Characters

n=int(input("Enter a number : "))
for i in range(1,n):
    for j in range(65,65+i):
        a=chr(j)
        print(a,end='')
    print()      

#Sample Output
'''

Enter a number : 7
A
AB
ABC
ABCD
ABCDE
ABCDEF

'''
