#Count vewels in a string

a=input("Enter a string: ")
cv=0
for i in a:
    if i=='A' or i=='E' or i=='I' or i=='O' or i=='U' or i=='a' or i=='e' or i=='i' or i=='o' or i=='u' :
        cv+=1
print(cv)
