#Print largest and smalles values out of two

def largest_smallest(x,y):
    if x>y:
        print(x,"is Greater")
    elif x==y:
        print("Both values are equal")
    else:
        print(y,"is Greater")

a=int(input("Enter first value: "))
b=int(input("Enter second value: "))
print(largest_smallest(a,b))
