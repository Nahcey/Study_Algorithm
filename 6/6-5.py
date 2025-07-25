# 셰이커 정렬 알고리즘 구현하기

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:
    """셰이커 정렬"""
    left = 0
    right = len(a) - 1
    last = right
    while left < right:
        for j in range(right, left, -1):
            if a[j-1] > a[j]:
                a[j-1] , a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left,right):
            if a[j] > a[j + 1]:
                a[j], a[j+1] = a[j+1], a[j]
                last = j
        right = last

if __name__ == '__main__':
    print('shaker 정렬 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    shaker_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')