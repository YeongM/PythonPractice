# 내가 만든 Selection sort
array = list(map(int,input().split()))

#가장 작은것을 맨 앞으로 보내는 형식
for i in range(len(array)-1):
    min=array[i]
    for j in range(i+1,len(array)):
        if min > array[j]:
            min=array[j]
            array[j]=array[i]
            array[i]=min
    array[i]=min

print(array)

#해답
array = [ 7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i] , array[min_index] = array[min_index],array[i]

print(array)