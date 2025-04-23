#Check odd even

def OddEven(n):
    if n==0: print("Zero is neither Even nor Odd")
    elif n%2==0: print("The number is Even")
    else: print("The number is Odd")

a=int(input("Enter the number: "))
print(OddEven(a))
