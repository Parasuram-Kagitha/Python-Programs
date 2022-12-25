#Fibonacci Series

n=int(input("Enter a number : "))
print("Fibonacci Series = ")
first=0
second=1
print(first,second,end=" ")
for a in range (0,n):
  third=first+second
  print(third,end=" ")
  first,second=second,third


#Sample Output
'''

Enter a number : 13
Fibonacci Series = 
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377

'''
