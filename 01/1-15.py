# +를 n개 출력하되 w개마다 줄바꿈하기 1

print('*를 출력합니다.')
n = int(input('몇개 출력'))
w = int(input('몇개마다 줄바꿈'))

for _ in range(n //w ):
    print('*'*w)

rest  = n % w
if rest:
    print('*'*rest)