# 1000이하의 소수를 나열하기

counter = 0

for n in range(2,1001):
    for i in range(2,n):
        counter += 1
        if n % i == 0:
            break
    else:
        print(n)
print(f'나눗셈을 실행한 회수: {counter}')