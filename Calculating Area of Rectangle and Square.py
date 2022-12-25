def Area_of_circle(radius):
    area=3.14*radius*radius
    return area
def Area_of_rectangle(length,breadth):
    area=length*breadth
    return area

radius=float(input("Enter Radius value = "))
area=Area_of_circle(radius)
print("Area of Circle = ",area)
length=int(input("Enter length value = "))
breadth=int(input("Enter breadth value = "))
if length==breadth:
    s=Area_of_rectangle(length,breadth)
    print("It is a Square !!!!!")
    print("Area of Square = ",s)
else:
    a=Area_of_rectangle(length,breadth)
    print("Area of Rectangle = ",a)

#Sample Output-1
Enter Radius value = 10
Area of Circle =  314.0
Enter length value = 10
Enter breadth value = 20
Area of Rectangle =  200

#sample Output-2
Enter Radius value = 1
Area of Circle =  3.14
Enter length value = 10
Enter breadth value = 10
It is a Square !!!!!
Area of Square =  100
