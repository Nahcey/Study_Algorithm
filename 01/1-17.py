#가로 세로 길이가 정수이고 넓이가 area인 직사각형에서 변의 길이 나열하기

area = int(input('넓이'))

for i in range(1, area + 1):
    if i * i > area: break
    if area % i: continue
    print(f'{i} x {area//i}')