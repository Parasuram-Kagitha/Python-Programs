def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i,end=",")
    print(" are factors of ",n)

n=int(input("Enter a number = "))
factors(n)



#Sample Output-1
Enter a number = 100
1,2,4,5,10,20,25,50,100, are factors of  100.

#Sample Output-2
Enter a number = 123
1,3,41,123, are factors of  123

#Sample Output-3
Enter a number = 999
1,3,9,27,37,111,333,999, are factors of  999
