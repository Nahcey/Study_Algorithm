# 셀 정렬 알고리즘 구현하기(h * 3 + 1의 수열 사용)

from typing import MutableSequence

def shell_sort(a: MutableSequence) -> None:
    """셀 정렬(h * 3 + 1의 수열 사용)"""
    n = len(a)
    h = 1 

    while h < n // 9:
        h = h * 3 + 1

    while h > 0:
        for i in range(h,n):
            j = i - h
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j + h] = tmp
        h //= 3

if __name__ == '__main__':
    print('셀 정렬을 수행합니다(h * 3 + 1의 수열 사용)')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')

    