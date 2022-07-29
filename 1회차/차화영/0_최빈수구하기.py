import sys
sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for test_case in range(T):
    n = int(input())
    numbers = int, input().split()
    
    cnt = 0
    for score in range(101): # score는 0부터 100까지의 범위
        if 