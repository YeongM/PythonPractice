#정수 N이 입력되면 00시 00분 00초 부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오

#24*60*60=86400 이므로 완전탐색을 한다.
#1이 증가할때마다 3이 포한되어 있는지 확인

n=int(input())
count=0
#0~n-1 시간까지
for i in range(n+1):
    #60분
    for j in range(60):
        #60초
        for k in range(60):
            #문자열에 3이 들어가면 조건문이 true
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)