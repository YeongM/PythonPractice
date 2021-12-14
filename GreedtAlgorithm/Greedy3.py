# 각 자리가 숫자(0~9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오
# 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.

#내가 씉 코드
#풀이 : 0이거나 1이 나오면 +로 하고, 이것이 아닌 숫자가 나오면 *를 한다.
a=input().split()
result=0
b=list()
for i in range(len(a[0])):
    b.append(int(a[0][i]))

for i in range(len(b)-1):
    if(b[i]<=1 or b[i+1]<=1):
        result=(b[i]+b[i+1])
        b[i+1]=result
    else:
        result = (b[i] * b[i + 1])
        b[i + 1] = result
print(result)



#해답 : 두 수중에 0또는 1이 있으면 + 그게 아니면 x가 효율적이다.
data=input()
#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1,len(data)):
    #두 수 중에서 하나라도 '0'혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result<=1:
        result +=num
    else:
        result *=num
print(result)