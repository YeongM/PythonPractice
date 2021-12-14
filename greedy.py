n=1260
count=0

#화폐단위
array=[500,100,50,10]

#최대 화폐금액이 500이고, 그 아래 화폐 단위의 배수가 500이므로 greedy 알고리즘을 사용해도 된다.
for coin in array:
    count += n//coin
    n= n%coin

#최소 동전 반환
print(count)

#현재의 코드의 시간 복잡도는 O(화폐의 개수)이다.