lst = ['madam', 'Python', 'malayalam', 12321]
palindromes = filter(lambda x: isinstance(x, str) and x == x[::-1], lst)

print(list(palindromes))
