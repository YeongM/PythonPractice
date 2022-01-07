#다익스트라 알고리즘 동작 원리
#1. 출발 노드를 설정한다.
#2. 최단 거리 테이블을 초기화한다.
#3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드를 선택한다.
#4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산라여 최단 거리 테이블을 갱신한다.
#5. 위 과정에서 3번 4번을 반복한다.

import sys
input = sys.stdin.readline()
INF = int(1e9) #무한

#노드의 개수와 간선의 개수를 입력받기
n, m = map(int,input().split())
#시작노드 입력 받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#방문 체크 리스트 만들기
visited = [False] * (n+1)
#최단 거리 테이블 모두 무한으로 설정
distance = [INF] * (n+1)

#모든 간선 정보 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    #a번 노드에서 b번 노드로 가는 비용 c
    graph[a].append((b,c))

#방문하지 않은 노드 중에서 가장 거리가 짧은 노드 번호 반환
def get_smallest_index():
    min_value = INF
    index = 0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijstra(start):
    #시작 노드 초기화
    distance[start]=0
    visited[start]=True
    #시작 노드에 대한 distance 처리
    for j in graph[start]:
        distance[j[0]]=j[1]
    #위에서 시작노드에 대한 처리를 했으므로 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #distance중 가장 짧은 인덱스 반환
        now = get_smallest_index()
        visited[now] = True
        #현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] +j[1]
            #cost가 더 작을경우(최소 거리가 될 경우)
            if cost<distance[now]:
                distance[j[0]] = cost

#다익스트라 실행
dijstra(start)

#모든 노드로 가기 위한 최단거리 출력
for i in range(1,n+1):
    #도달 불가능 : INF
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])