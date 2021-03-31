# 문제10. 입력받은 n이 홀수면 0~n까지의 홀수의 합을 출력, 짝수면 짝수의 합을 출력

n = int(input('숫자를 입력하세요 : '))
sum = 0
if n%2==0 :
    for i in range(0,n+1) :
        if i%2==0 :
            sum+=i
else :
    for i in range(0,n+1) :
        if i%2!=0 :
            sum+=i

print('결과 값 :',sum)