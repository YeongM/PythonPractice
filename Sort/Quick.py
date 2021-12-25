def quick(array, start, end):
    if start >= end:
        return
    pivot = start  #피벗은 첫 번째 원소
    left = start+1
    right = end
    # 오른쪽 인덱스 값이 왼쪽 인덱스 값보다 클때까지
    while (left <= right):
        #왼쪽 값이 피벗 값보다 작을 때까지 +1
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        #오른쪽 값이 피벗 값보다 클 때까지 -1
        while(right>start and array[right]>=array[pivot]):
            right -=1
        #왼쪽 인덱스 값이 오른쪽 인덱스 값보다 클 경우 : 교차가 일어 났다
        if(left>right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]

    quick(array,start,right-1)
    quick(array,right+1,end)

array=[5,7,9,8,3,1,6,2,4,3]
quick(array,0,len(array)-1)
print(array)