r=int(input("enter the number r: "))
def fact(x):
    fac=1
    for i in range(1,x+1):
          fac=fac*i
    print(fac)
check=fact(r)
