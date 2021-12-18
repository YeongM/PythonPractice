#N X M 크기의 얼음 틀이있습니다. 구멍이 뚫려 있는 부분은 0, 컨막이가 존재하는 부분은 1로 표시됩니다.
#구멍이 뚫려있는 부분끼리 상하좌우로 붙어 있는 경우 서로 연셜되어 있는 것으로 간주합니다.
#이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크임의 개수를 구하는 프로그램을 작겅하세요.

#DFS로 특정 노드를 방문하고 연결괸 모든 노드들도 방문
def dfs(x,y):
    #주어진 범위를 벗어나면 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        #해당 노드 방문처리
        graph[x][y]=1
        #상하좌우의 위치를 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

n, m = map(int,input().split())
#2차원 리스트의 맵 정보 입력 받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

#모든 노드에 대해 음료수 채우기
result=0
for i in range(n):
    for j in range(m):
        #현재위치에서 DFS 수행
        if dfs(i,j) ==True:
            result+=1
print(result)