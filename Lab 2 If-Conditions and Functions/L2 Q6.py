#Number of digits

def numberofdigits(n):
    count=0
    for i in n:
        count +=1
    print(count)

a=int(input("Enter a number: "))
b=str(a)                           #IMP STEP
print(numberofdigits(b))
