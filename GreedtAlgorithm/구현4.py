#알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어집니다. 이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
#그 뒤에 모든 숫자를 더한 값이 이어서 출력합니다.

#내 코드
data=input()
array=list()
result=0
#문자를 각 하나씩 쪼개기 위해 리스트 형식으로 만듬
for i in range(len(data)):
    array.append(data[i])
#알파벳은 뒤로 가고, 숫자는 앞으로 놓임
array.sort()

for i in range(len(data)):
    #data의 숫자들은 덧셈하고, array의 그 숫자들을 제거한다.
    if(int(ord(data[i]))<int(ord('A'))):
        result+=int(data[i])
        array.remove(data[i])
#마지막에 append하여 뒤에 덧셈 결과를 붙인다
if(result!=0):
    array.append(str(result))
data=""

#리스트를 문자열로 변환하는 과정
for i in range(len(array)):
    data+=array[i]
print(data)




#풀이
data = input()
result = []
value=0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    #숫사인 경우 더하기
    else:
        value+=int(x)

#알파벳은 오름차순 정렬
result.sort()
#숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))
#최종 결과 출력(리스트를 문자열로 변환하여출력)
print(''.join(result))