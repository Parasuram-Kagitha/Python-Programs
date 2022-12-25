#Sum Of Natural Numbers
s=0
n=int(input("Enter a number : "))
print('0',end="")
for i in range (1,n+1):
    s+=i
    print("+",i,end=" ")
    
print(" = ",s)


#Sample Output
'''
Enter a number : 20
0+ 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20  =  210
'''
