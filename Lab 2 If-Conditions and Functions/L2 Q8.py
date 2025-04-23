#Valid triangle or not

def validtriangle(x,y,z):
    if x+y+z==180: print("This is a valid triangle")
    else: print("This is not a valis triangle")

a=int(input("Enter first angle: "))
b=int(input("Enter second angle: "))
c=int(input("Enter third angle: "))
validtriangle(a,b,c)
