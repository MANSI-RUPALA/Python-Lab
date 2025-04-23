def ispalindrome():
    str1=input('enter the string')
    str1=str1.lower()
    lst=list(str1)
    lst1=reversed(lst)
    if(lst==lst1):
        print('it is a palindrome')
ispalindrome()    
