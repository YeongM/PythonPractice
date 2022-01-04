#식량 털기 문제
#점화식은 ai = max(ai-1, ai-2 + ki)
#ki = i 번째 식량 창고에 있는 식량의 양

n=int(input())
#모든 식량 정보 입력
array = list(map(int,input().split()))

store = [0]*100

#첫 식량
store[0]=array[0]
#둘중 큰 값을 털기
store[1]=max(array[0],array[1])
#점화식 부분
for i in range(2,n):
    store[i]=max(store[i-1],store[i-2]+array[i])
#결과 출력
print(store[n-1])