def fibonacciImperative(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1 
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b
    
def fibonacciFunctional(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciFunctional(n - 1) + fibonacciFunctional(n - 2)
    
print(fibonacciFunctional(10))

print(fibonacciImperative(10))