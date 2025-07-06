# +와 -를 번갈아 출력하기 2

print('+와 -를 번갈아 출력')
n = int(input('몇 개를 출력'))

for _ in range(n // 2):
    print('+-',end = '')
    
if n % 2:
    print('+',end = '')

print()