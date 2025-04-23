#Three points lie on a straight line or not

def straightline(x1,y1,x2,y2,x3,y3):
    m1=(y2-y1)/(x2-x1)
    m2=(y3-y2)/(x3-x2)
    if m1==m2: print("These points lie on a straight line")
    else: print("These points does not lie on a straight line")

a1=int(input("Enter x coordinate of the first point: "))
b1=int(input("Enter y coordinate of the first point: "))
a2=int(input("Enter x coordinate of the second point: "))
b2=int(input("Enter y coordinate of the second point: "))
a3=int(input("Enter x coordinate of the third point: "))
b3=int(input("Enter y coordinate of the third point: "))
straightline(a1,b1,a2,b2,a3,b3)
    
