#Menu Driven Program for Prime Number,Armstrong Number,Factorial,Finding Factors of a number.


while True:
    print("\n\n1.Prime Number\n2.Armstrong Number\n3.Factorial\n4.Factors = ")
    ch=int(input("Enter a your choice = "))
    if ch==1:
        def isPrimeNumber(n):
            count=1
            for i in range(2,n):
                if n%i==0:
                    count=2
            if count==1:
                print(n," is a prime number")
            else:
                print(n,"is not a prime number")

        n=int(input("Enter a number = "))
        isPrimeNumber(n)
        continue
    elif ch==2:
        def isArmstrongNumber(n):
            count=0
            temp=n
            while n>0:
                count=count+1
                n=n//10
            n=temp
            temp=n
            s=0
            while n>0:
                s=s+((n%10)**count)
                n=n//10
            if s==temp:
                print(s,"is Armstrong number ")
            else:
                print(temp," is not an Armstrong number..")

        n=int(input("Enter a number = "))
        isArmstrongNumber(n)
        continue
    elif ch==3:
        def factorial(n):
            fact=1
            for i in range(1,n+1):
                fact=fact*i
            print(n," factorial = ",fact)
    
        n=int(input("Enter a number = "))
        factorial(n)
        continue
    elif ch==4:
        def factors(n):
            for i in range(1,n+1):
                if n%i==0:
                    print(i,end=",")
            print(" are factors of ",n)

        n=int(input("Enter a number = "))
        factors(n)
        continue
    else:
        print("Wrong choice\nEnter your choice again")
        continue
 
 
 
 
#Sample Output

1.Prime Number
2.Armstrong Number
3.Factorial
4.Factors 

Enter a your choice = 1
Enter a number = 13
13  is a prime number


1.Prime Number
2.Armstrong Number
3.Factorial
4.Factors 

Enter a your choice = 2
Enter a number = 153
153 is Armstrong number 


1.Prime Number
2.Armstrong Number
3.Factorial
4.Factors 

Enter a your choice = 3
Enter a number = 5
5  factorial =  120


1.Prime Number
2.Armstrong Number
3.Factorial
4.Factors 

Enter a your choice = 4
Enter a number = 100
1,2,4,5,10,20,25,50,100, are factors of  100


1.Prime Number
2.Armstrong Number
3.Factorial
4.Factors

Enter a your choice = t
