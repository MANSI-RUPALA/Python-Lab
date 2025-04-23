#Perimeter  of rectangle is greater than area or not

def perimeterarea(x,y):
    p=2*(x+y)
    ar=x*y
    if p>ar: print("The perimeter of this rectangle is greater than it's area")
    elif ar>p: print("The area of this rectangle is greater than it's perimeter")
    else: print("The perimeter and area of this reactangle are same")

a=int(input("Enter the length of rectange: "))
b=int(input("Enter the breadth of the reactangle: "))
perimeterarea(a,b)
