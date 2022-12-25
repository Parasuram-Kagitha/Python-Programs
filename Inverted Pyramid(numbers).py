#Inverted Pyramid

n=int(input("Enter a number : "))
for i in range(n):
    for j in range(n,i,-1):
        print(j,end= " ")
    print()
      
#Sample Output
'''
Enter a number : 10
10 9 8 7 6 5 4 3 2 1 
10 9 8 7 6 5 4 3 2 
10 9 8 7 6 5 4 3 
10 9 8 7 6 5 4 
10 9 8 7 6 5 
10 9 8 7 6 
10 9 8 7 
10 9 8 
10 9 
10
'''
