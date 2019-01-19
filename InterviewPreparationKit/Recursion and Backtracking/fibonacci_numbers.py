def fibonacci(n):
    if (n <= 1):
        return(n)
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
        return(res)
        

    # Write your code here.

n = int(input())
print(fibonacci(n))
