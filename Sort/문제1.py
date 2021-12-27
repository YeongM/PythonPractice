#두 개의 배열 A와 B가 있습니다. 두 배열은 N개의 원소로 구성되어 있으며, 배열의 원소는 모두 자연수 입니다. 최대 K번의 바꿔치기 연산을 수행할 수 있는데,
#바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 말합니다. 최종 목표는 배열 A의 모든 원소의 합이
#최대가 되도록 하는 것이다. N, K, 배열 A와 B의 정보가 주어졌을 때, 최대 K 번의 바꿔치기 연산을 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값을 출력

#내 풀이 : B의 가장 큰 값과 A의 가장 작은 값을 비교하여 B_MAX>A_MIN 이면 바꾼다.

A=[1,2,5,4,3]
B=[5,5,6,6,5]

n=5
k=3

A_min_index=0
B_max_index=0

for i in range(k):
    for j in range(n):
        if A[j]<A[A_min_index]:
            A_min_index=j
        if B[j]>B[B_max_index]:
            B_max_index=j
    if A[A_min_index]<B[B_max_index]:
        A[A_min_index], B[B_max_index] = B[B_max_index], A[A_min_index]

print(sum(A))

#해답 코드
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse = True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]
    else:    #정렬이 되어 있으므로 else 문 통과시 반복문 종료
        break

print(sum(A))