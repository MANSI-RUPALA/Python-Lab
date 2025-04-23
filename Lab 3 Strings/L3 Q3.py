#if one string is in another

a=input("Enter a string: ")
b=input("Enter another string: ")
if a in b:
    print("The first string is a part of the second string")
elif b in a:
    print("The second string is present in the first string")
else:
    print("Both strings are unique")
