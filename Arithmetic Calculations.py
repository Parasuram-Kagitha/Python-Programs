#Simple Arithmetic Operations using Operators(+,-,/,%,*)
a=int(input("Enter a number="))
b=int(input("Enter a number="))
op=input("Enter a operator(+,-,*,%,/)")
if op=="+":
    print("Sum=",a+b)
elif op=="-":
    print("Difference=",a-b)
elif op=="*":
    print("Product=",a*b)
elif op=="%":
    print("Remainder=",a%b)
elif op=="/":
    print("Division=",a/b)
else:
    print("invalid operator")

#Sample Output-1
Enter a number=10
Enter a number=5
Enter a operator(+,-,*,%,/)+
Sum= 15

#Sample Output-2
Enter a number=40
Enter a number=30
Enter a operator(+,-,*,%,/)-
Difference= 10

#Sample Output-3
Enter a number=500
Enter a number=50
Enter a operator(+,-,*,%,/)/
Division= 10.0

#Sample Output-4
Enter a number=100
Enter a number=90
Enter a operator(+,-,*,%,/)0
invalid operator
