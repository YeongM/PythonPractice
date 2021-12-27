#이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, target, start, end):
    if start>end:
        return None
    mid = (start+end)//2
    #찾은 경우
    if array[mid] == target:
        return mid
    #target값이 중간값보다 작은 경우
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    #target값이 중간값보다 큰 경우
    else:
        return binary_search(array,target,mid+1,end)

n,target = list(map(int, input().split()))
array = list(map(int,input().split()))

result = binary_search(array,target,0,n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)