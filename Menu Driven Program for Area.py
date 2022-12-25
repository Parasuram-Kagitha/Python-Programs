#Menu Driven Program for Calculating Area
print('''Menu : 
            1.Square
            2.Rectangle
            3.Circle''')
ch=int(input("enter your choice:"))
if ch==1:
    s=int(input("enter side:"))
    area=s*s
    print("Area of circle is:",area)
if ch==2:
    l=int(input("enter length:"))
    b=int(input("enter breadth:"))
    area=l*b
    print("Area of rectangle is:",area)
if ch==3:
    r=int(input("enter radius:"))
    area=3.14*r*r 
    print("Area of circle is:",area)


#Sample Output-1
'''
Menu : 
            1.Square
            2.Rectangle
            3.Circle
enter your choice:1
enter side:20
Area of circle is: 400
'''

#Sample Output-2
'''
Menu : 
            1.Square
            2.Rectangle
            3.Circle
enter your choice:2
enter length:10
enter breadth:100
Area of rectangle is: 1000
'''

#Sample Output-3
'''
Menu : 
            1.Square
            2.Rectangle
            3.Circle
enter your choice:3
enter radius:10
Area of circle is: 314.0
'''
