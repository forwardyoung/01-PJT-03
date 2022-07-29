import sys
sys.stdin = open("_문자열의거울상.txt")
T = int(input())
for test_case in range(1, T+1):
    word = input()
    reverse_ = word[::-1] # 먼저 거꾸로 슬라이싱을 한다.
    mirror = '' # mirror라는 str 타입의 변수 생성
    for l in reverse_: # 거꾸로 슬라이싱한 문자의 인덱스 l이 있을 때 
        if l == 'b': # l이 b이면
            mirror += 'd' # mirror에 d를 저장한다.
        elif l == 'd':
            mirror += 'b'
        elif l == 'q':
            mirror += 'p'
        else:
            mirror += 'q'
    print("#{} {}".format(test_case, mirror))