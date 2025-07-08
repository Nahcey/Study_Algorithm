# while 문으로 작성한 선형 검색 알고리즘

from typing import Any, Sequence

def seq_search(a: Sequence, key: Any) -> int:
    """시퀀스 a에서 key와 같이 원소를 선형 검색(while문)"""
    i = 0

    while True:
        if i == len(a):
            return -1
        if a[i] == key:
            return i
        i += 1

if __name__ == '__main__':
    num = int(input('원소 수를 입력: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    ky = int(input('검색할 값 입력: '))

    idx = seq_search(x, ky)

    if idx == -1:
        print('N')
    else:
        print(f'검색 값은 x[{idx}]에 있습니다.')