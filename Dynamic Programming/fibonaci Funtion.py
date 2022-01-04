def fibonaci(x):
    if x==1 or x==2:
        return 1
    return fibonaci(x-1)+fibonaci(x-2)
n = int(input())
print(fibonaci(n))

#위와 같은 코드는 연산 횟수가 너무 많다.
#아래는 중복연산되는 부분을 줄여 다이나믹 프로그래밍으로 만들었다.
#매모이제이션을 활용하여 한 번 계산한 결과를 메모리 공간에 메모한다.

#임시 저장 장소
store = [0] * 100

def fibo(x):
    if x==1 or x==2:
        return 1
    #이미 계산이 되었다면
    if store[x] !=0:
        return store[x]
    #계산이 되지 않았다면
    store[x] = fibo(x-1)+fibo(x-2)
    return store[x]

n= int(input())
print(fibo(n))
