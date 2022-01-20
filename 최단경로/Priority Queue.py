# 우선순위 큐는 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조
#Heap을 사용하여 구현

import heapq
#오름차순 힘 정렬(Heap Sort)
def heapsort_Ascending(iterable):
    h=[]
    result=[]
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,value)

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result
#내림차순 힘 정렬(Heap Sort)
def heapsort_Descending(iterable):
    h=[]
    result=[]
    #모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h,-value)

    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort_Ascending([1,3,5,7,9,2,4,6,8,0])
print(result)

result = heapsort_Descending([1,3,5,7,9,2,4,6,8,0])
print(result)