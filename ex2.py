try: 
    a = int(input('-> '))
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
    print("Factorial of", a, "is",
    factorial(a))
except Exception as ex:
    print(f'Error [{ex.__class__.__name__}]: {ex}')
