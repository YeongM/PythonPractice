array = list(map(int,input().split()))

for i in range(1,len(array)):
    for j in range(i,0,-1): # 인덱스 i부터 1까지 1씩 감소하여 반복하는 문법
        if array[j]<array[j-1]: #한 칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j] # 그 때마다 자리를 바꾼디
        else:
            break
print(array)