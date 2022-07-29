from re import I
import sys
sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for tc in range(1, T+1):
    n = list(map(int, input().split()))
    sum = 0
    for i in range(len(n)): 
        if i % 2 == 0: # 인덱스가 짝수이면
            sum += 2 * n[i] # 짝수 인덱스에 해당하는 n 값에 2를 곱해준 후 sum에 더해준다.
        else: # 인덱스가 홀수이면
            sum += n[i] # 홀수 인덱스에 해당하는 n값 그대로를 sum에 더해준다.
    if sum % 10 == 0: # sum이 이미 10의 배수면 굳이 16번째 숫자에 1~9를 더해줄 필요가 없다.
        print("#{} {}".format(tc, 0)) # 0을 출력한다.
    else: 
        print("#{} {}".format(tc, 10 - int(str(sum)[-1]))) # sum과 n을 더한 숫자가 10의 배수 --> sum의 마지막자리 숫자 + n = 10