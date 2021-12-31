#떡볶이 떡의 길이가 일정하지 않고, 한 봉지 안에 들어가는 떡의 총 길이는 절단기로 잘라서 맞춘다. 절단기에 높이를 지정하면
#줄지어진 떡을 한 번에 절단합니다. 높이가 H보다 긴 떡은 H위의 부분이 잘릴 것이고, 낮은 떡은 잘리지 않습니다. 예를 들어 19,14,10,17cm인 떡이
#나한히 있고 높이가 15cm이면 15,14,10,15cm가 된다. 잘린 떡의 길이는 차례대로 4,0,0,2cm이다. 손님은 총 6cm만큼의 길이를 가져간다.
#손님이 왔을 때 요청한 길이가 M일 때 적어도 M만큼의 떡을 얻기 위해 절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

#입력한 정수의 범위가 10억이므로 이진탐색을 해야한다.
#떡을 자르는 높이의 최댓값은 떡의 길이의 최대값이다. 이를 통해 이진탐색을 한다.
#내 풀이
n, m = map(int,input().split())
data = list(map(int,input().split()))
max_data=max(data)
#시작점은 0
start=0
#떡의 최댓값에서 /2를 하면서 중간값 설정
midle=int(max_data/2)
while True:
    result=0
    #손님에게 주는 떡
    for j in range(n):
        #떡의 길이가 더 클 경우
        if data[j]>midle:
            #떡의 길이에서 중간값을 빼면 제공하는 떡
            result+=data[j]-midle
    #원하는 떡의 길이와 제공하는 떡의 길이가 같을 경우
    if(result==m):
        #증간값이 높이
        print(midle)
        break
    #원하는 떡의 길이보다 제공하는 떡의 길이가 작을 경우
    elif result<m :
        midle = int((start+midle)/2)
    #원하는 떡의 길이보다 제공하는 떡의 길이가 클 경우
    else:
        start = midle
        midle = int((start+max_data)/2)

#해답
n, m = map(int,input().split())
data = list(map(int,input().split()))
start = 0
end = max(data)

result=0
while(start <= end):
    total = 0
    mid = (start+end)//2
    for x in data:
        #잘랐을 때의 떡의 양 계산
        if x>mid :
            total+= x-mid
    #떡의 양이 부족한 경우 더 많이 자르기
    if total<m:
        end=mid-1
    else:
        result = mid #최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid+1

print(result)