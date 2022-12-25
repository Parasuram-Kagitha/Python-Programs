n=input("Enter number = ")
l=list(n)
i=len(l)-1

def reverse(i,n):
      if i>=0:
            print(l[i],end="")
            reverse(i-1,n)

print("Reverse number of ",n," = ")
reverse(i,n)
      
#Sample Output
'''
Enter number = 123456
Reverse number of  123456  = 
654321

'''

