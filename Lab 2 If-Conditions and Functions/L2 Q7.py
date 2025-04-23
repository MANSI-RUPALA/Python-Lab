#Leap year or not

def leapyear(n):
    if n%4==0: print("This is a leap year")
    else: print("This in not a leap year")

a=int(input("Enter the year: "))
leapyear(a)
