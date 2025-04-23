def ls():
    n= int(input('enter the number'))
    return([(x,x**2,x**3) for x in range(1,n+1)])
print(ls())
        
