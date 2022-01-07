#특정한 전투력을 갖고있는 병사를 내림차순으로 정렬한다.
#배치과정에서 특정한 위치에 있는 병사를 열외시키는 방법을 이용한다. 그러면서도 남아 있는 병사의 수가 최대가 되도록 하는 알고리즘을 만들어라

#이 문제는 가장 긴 증가하는 부분 수열을 사용한다.
#가장 긴 증가하는 부분 수열이란 array = {4,2,5,8,4,11,15}가 있을 경우
#이 수열의 가장 긴 증가하는 부분 수열은 {4,5,8,11,15}이다.
#본 문제는 가장 긴 감소하는 부분 수열을 찾으면 된다.

n = int(input())
array = list(map(int,input().split()))
#array 함수를 뒤집는다.
array.reverse()

#다이나믹 프로그램밍을 위한 store배열 1로 모두 초기화
store = [1]*n

#가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1,n):
    for j in range(i):
        if array[j] < array[i]:
            store[i]=max(store[i],store[j]+1)

#열외 병사 출력
print(n-max(store))