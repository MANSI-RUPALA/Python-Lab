#Absolute value

def absolute(n):
    if n==0: print("The absolute value of 0 is 0")
    elif n<0: print("The absolute value of",n ," is", -n)
    elif n>0: print("The absolute value of", n," is", n)
    else: print("ERROR!")

a=int(input("Enter any value: "))
absolute(a)
