# 이진 검색 알고리즘

from typing import Any, Sequence

def bin_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 일치하는 원소를 이진 검색"""
    pl = 0                  
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2 #중앙 원소 인덱스
        if a[pc] == key: 
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1

if __name__ == '__main__':
    num = int(input('원소 수 입력: '))
    x = [None] * num

    print('배열 데이터 오름차순 입력: ')

    x[0] = int(input('x[0]: '))

    for i in range(1, num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= x[i - 1]:
                break

    ky = int(input('검색할 값 입력: '))

    idx = bin_search(x, ky)

    if idx == -1:
        print('n')
    else: 
        print(f'검색값은 x[{idx}]에 있습니다.')