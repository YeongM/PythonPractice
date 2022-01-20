import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) #무한

#노드의 개수, 간선의 개수를 입력받기
n, m = map(int,input().split())
#시작 노드 번호를 입력받기
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력 받기
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

#다익스트라 알고리즘
def dijkstra(start):
    q=[]
    #시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq(q,(0,start))
    distance[start]=0
    #큐가 빌때까지
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        #현재 노드가 이미 처리 되었다면
        if distance[now] < dist:
            continue
        #현재노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #더 짧을 경우
            if distance[i[0]] > cost:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
#다익스트라 실행
dijkstra(start)

#모든 노드로 가기 위한 최단 거리 출력
for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])