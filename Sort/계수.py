array = list(map(int,input().split()))
count = [0]*(max(array)+1)

for i in range(len(array)):
    #해당 데이터 인덱스 +1
    count[array[i]] += 1
#리스트에 기록된 정령 정보 확인
for i in range(len(count)):
    for j in range(count[i]):
        #띄어쓰기로 문장 쓰기
        print(i,end=' ')