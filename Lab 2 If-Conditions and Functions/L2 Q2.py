#Print largest and smallest out of three

def largest_and_smallest(x,y,z):
    if x>y and x>z: print(x,"is Largest")
    elif y>x and y>z: print(y,"is Largest")
    elif z>x and z>y: print(z,"is Largest")
    if x<y and x<z: print(x,"is Smallest")
    elif y<x and y<z: print(y,"is Smalles")
    elif z<x and z<y: print(z,"is Smallest")
    else: print("All values are equal")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
print(largest_and_smallest(a,b,c))
        
