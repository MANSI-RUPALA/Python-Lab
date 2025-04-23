def fibonacci(n):
    fib= []
    a, b = 0, 1
    for _ in range(n):
        fib.append(a)
        a, b = b, a + b
    return fib
n = int(input("Enter the number of Fibonacci terms to generate: "))
fibo = fibonacci(n)
print("Fibonacci series: ", fibo)
