def fibonaci(x):
    if x==1 or x==2:
        return 1
    return fibonaci(x-1)+fibonaci(x-2)
n = int(input())
print(fibonaci(n))