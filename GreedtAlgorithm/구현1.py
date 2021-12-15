#여행가 A 는 N X N크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 X 1 쿠기의 정사각형으로 나누어져 있습니다. 가장 왼쪽 위 좌표는 (1,1)이며, 가장 오른쪽 아래 좌표는
#N X N 에 해당합니다. 여행가 A 는 상하좌우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1,1)입니다. 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.
#계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L R U D 중 하나의 문자가 반복적으로 적혀 있습니다.
#L-왼쪽으로 한 칸, R-오른쪽으로 한 칸, U-위쪽으로 한 칸, D-아래쪽으로 한 칸

x, y = 1, 1
N=int(input())
datas=input().split()

dx=[0,0,-1,1]
dy=[-1,1,0,0]

move_type=['L',"R","U","D"]

for data in datas:
    for i in range(len(move_type)):
        if(data==move_type[i]):
            tmpx=x+dx[i]
            tmpy=y+dy[i]
    if tmpx<1 or tmpx>N or tmpy<1 or tmpy>N:
        continue
    x=tmpx
    y=tmpy
print(x,y)