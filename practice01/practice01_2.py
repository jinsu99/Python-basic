# 문제2. 키보드로 정수 수치를 입력 받아 짝수인지 홀수 인지 판별하는 코드를 작성하세요.

num = int(input('정수 입력 : '))
if num==0 :
    print('0 입니다 ')
elif num%2==0 :
    print('%d : 짝수 입니다 '%num)
else :
    print('%d : 홀수 입니다 '%num)