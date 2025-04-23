n=int(input("enter the number n: "))
r=int(input("enter the number r: "))
def fact(x):
    fac=1
    for i in range(1,x+1):
          fac=fac*i
    return fac
print("nCr= ",fact(n)/(fact(r)*fact(n-r)))
print("nPr= ",fact(n)/fact(n-r))
