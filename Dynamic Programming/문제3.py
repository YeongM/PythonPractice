#최소화 화폐만들기
#화폐단위와 돈을 입력값으로 받기

#내 풀이
#점화식 ai는 최소 화폐 갯수, ki는 금액
#ai = min(a(ki-3),a(ki-2))+1

#화폐 갯수와 금액 적기
n, m = map(int,input().split())
array = [0]*n
for i in range(n):
    array[i]=int(input())
#INF 는 10001
store = [10001]*(m+1)

store[0]=0
for i in range(n):
    for j in range(array[i], m+1):
        if store[j-array[i]] != 10001:
            store[j] = min(store[j],store[j-array[i]]+1)

if store[m] == 10001:
    print(-1)
else:
     print(store[m])