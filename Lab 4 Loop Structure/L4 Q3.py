x=input("enter the string: ")
digit=0
alp=0
for i in x :
    if (i.isdigit()):
        digit=digit+1
    elif(i.isalpha()):
        alp=alp+1
print( "total no of digits is: ",digit)
print("total no of alphabet is: ",alp)
        
