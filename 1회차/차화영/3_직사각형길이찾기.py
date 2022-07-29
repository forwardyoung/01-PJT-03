import sys
sys.stdin = open("_직사각형길이찾기.txt")
T = int(input())
for test_case in range(1, T+1): 
    n = list(map(int, input().split())) # 세 변의 길이를 입력받는다.
    l = list(set(n)) # 중복을 제거하여 l이라는 리스트에 저장
    for i in l:
        size = 0 # 구하고자 하는 한 변의 길이를 0으로 초기화
        if len(l) == 1: # 중복제거한 l의 길이가 1일 때; 세 변의 길이가 모두 같을 때 결국 정사각형이므로
            size += i # 남은 한 변의 길이 역시 l과 동일하다.
        else: # 중복 제거한 l의 개수가 1이 아니면 -- 서로 다른 두 변의 길이
            size += sum(l) * 2 - sum(n) # 남은 한 변의 길이 : 서로 다른 두 변의 길이*2 - 남은 세 변의 길이의 합
    print("#{} {}".format(test_case, size))