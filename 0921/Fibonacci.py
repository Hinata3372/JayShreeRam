def fibonacci_iterative(n):
    if n < 0 :
        return -1,1
    if n == 0 or n == 1:
        return n,1
    steps = 0
    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b 
        b = c
        steps = steps + 1

    return c, steps+1

def fibonacci_recursive(n):
    if n < 0 :
        return -1,1
    if n == 0 or n == 1:
        return n,1
    
    fib1, steps1 = fibonacci_recursive(n-1)
    fib2, steps2 = fibonacci_recursive(n-2)

    return (fib1 + fib2), (steps1 + steps2 + 1)

if __name__ == '__main__':
    n = int(input("Enter number : "))
    print("Iterative : " , fibonacci_iterative(n)[0])
    print("Steps : " , fibonacci_iterative(n)[1])
    print("Recursive : " , fibonacci_recursive(n)[0])
    print("Steps : " , fibonacci_recursive(n)[1])