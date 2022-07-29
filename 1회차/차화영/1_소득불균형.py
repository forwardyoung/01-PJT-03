import sys
sys.stdin = open("_소득불균형.txt")
T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    income = list(map(int, input().split()))
    avg = int(sum(income)/len(income)) # avg : income의 합을 income의 길이(개수)로 나눈 평균
    cnt = 0
    for i in income:
        if i <= avg: # 변수 i가 avg이하일 때
            cnt += 1 # 1씩 개수를 더한다.
    print('#{} {}'.format(test_case, cnt))