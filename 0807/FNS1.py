memo = {}
def fibonacci_iter(n):
    if n<=0:
        return -1, 1
    if n==0 or n==1:
        return n, 1
    steps=0
    a= 0 
    b= 1
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        steps+=1
        return c, steps+1

def fibonacci_recur(n):
    def fib(n):
        if n<=0:
            return -1, 1
        if n in memo:
            return memo[n]
        if n==0 or n==1:
            return n, 1
        fib1, steps1 = fib(n-1)
        fib2, steps2 = fib(n-2)
        result = fib1 + fib2 , steps1+ steps2 +1
        return result
    return fib(n)

if __name__ =="__main__":
    n = int(input("Enter a number: "))
    print("Iterative:", fibonacci_iter(n)[0])
    print("Steps", fibonacci_iter(n)[1])
    print("Recursive:", fibonacci_recur(n)[0])
    print("Steps", fibonacci_recur(n)[1])