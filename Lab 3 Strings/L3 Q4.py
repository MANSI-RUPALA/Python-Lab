#Remove one string from another

a=input("Enter a string: ")
b=input("Enter the string to be removed from this string: ")
c=a.replace(b, "",1)
if b in a:
    print("New string: ",c)
else:
    print("Secong string is not present in the first  string")
    
