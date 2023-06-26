def recur_fib(n):
    if n<=1:
        return n
    else:
        return recur_fib(n-1)+recur_fib(n-2)
n=7
if n<0:
    print("can't perform")
else:
    print("fibonacci series of", n, "is",recur_fib(n))
