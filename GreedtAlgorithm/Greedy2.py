# 어떠한 수 N이 1이 될 때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 한다. 단, 두번째 연산은 N이 K로 나누어 떨어 질때만 가능
# 1. N에서 1을 뺀다.
# 2. N에서 K를 나눈다.


N, K=map(int, input().split(' '))
count=0

#내가 적은 이유 : N에서 K를 나누는 행위를 많이 해야지 최소 연산이 된다.
while (N!=1):
    if(N%K==0):
        count+=1
        N=N//K
    else:
        count+=1
        N-=1

print(count)

#중요
#해답 : 주어진 N에 대하여 최대한 많이 나누기를 수행하면 된다.
n,k=map(int,input().split())
result=0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target=(n//k)*k             #반복해서 1감소하는 N값중 최대 K배수인 값을 찾는 코드
    result+=(n-target)          #result 값에 1을 뺀 횟수를 result에 저장
    n=target                    #최종 1 감소한 n 값을 저장
    #N이 K보다 작을 때 (더이상 나눌 수 없을 때) 반복문 탈출
    if(n<k):
        break;
    result +=1                  #나눈 연산을 했으므로 연산 횟수 1증가
    n//=k                       #나눠진 값을 n에 저장

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)                 #(n-1)을 하여 1이 감소한 횟수 result에 저장
print(result)