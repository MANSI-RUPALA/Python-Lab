r=float(input("enter the radius: "))
x=float(input("enter the centre x point: "))
y=float(input("enter the centre y point: "))
def ch(x,y):
    if  (((x-x1)**2 +(y-y1)**2 ) ==r**2):
        print("it is on the circle")
    elif(((x-x1)**2 +(y-y1)**2) < r**2):
        print("it is inside the circle")
    else:
        print("it is outside the circle")

x1=float(input("enter the x point"))
y1=float(input("enter the y point"))
check=ch(x1,y1)            
