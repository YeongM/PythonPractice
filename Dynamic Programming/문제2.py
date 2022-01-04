# 1로 만들기
#규칙 : 5로 나누기, 3으로 나누기, 2로 나누기, 1 빼기
#최소 연산 횟수 출력

n = int(input())

store = [0]*30001

for i in range(2, n+1):
    #1 빼기
    store[i] = store[i-1]+1
    #2로 나누기
    if i%2==0:
        store[i] = min(store[i], store[i // 2] + 1)
    #3으로 나누기
    if i%3==0:
        store[i] = min(store[i], store[i // 3] + 1)
    #5로 나누기
    if i%5==0:
        store[i] = min(store[i], store[i // 5] + 1)
print(store[n])