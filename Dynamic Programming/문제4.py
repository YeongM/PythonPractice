#NXM 크기의 광산에서 채굴자가 얻을 수 있는 금의 크기의 최댓값을 출력하시오
#채굴자는 1열에서 어느 곳이든 출발 할 수 있으며, 이동 방향은 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나이다.

#테스트 케이스 입력
for tc in range(int(input())):
    #광산 정보 입력
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    store =[]
    index=0
    #2차원 배열 만들기
    for i in range(n):
        store.append(array[index:index+m])
        index+=m
    #다이나믹 프로그램 진행
    for i in range(1,m):
        for j in range(n):
            #왼쪽 위에서 오는경우
            if j==0:
                left_up=0
            else:
                left_up=store[j-1][i-1]
            #왼쪽 아래에서 오는 경우
            if j==n-1:
                left_down=0
            else:
                left_down=store[j+1][i-1]
            #왼쪽이라면
            left=store[j][i-1]
            store[j][i] = store[j][i] + max(left,left_up,left_down)
    result=0
    for i in range(n):
        result = max(result,store[i][m-1])
    print(result)
