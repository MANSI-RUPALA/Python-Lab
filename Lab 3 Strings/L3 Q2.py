x=input("enter the string: ")
def lower(x):
    ret=""
    for i in x:
        if 'A'<= i <= 'Z':
            ret+=chr(ord(i)+32)
        else :
            ret+=i
    return ret
def upper(x):
    ret=""    
    for i in x:
        if 'a'<= i<= 'z':
            ret+=chr(ord(i)-32)
        else :
            ret+=i
    return ret

print(upper(x))
print(lower(x))
