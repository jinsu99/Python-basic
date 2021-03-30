# 문제1. 키보드로 정수 수치를 입력 받아 그것이 3의 배수인지 판단하세요

num = int(input('정수 입력 : '))
if num%3==0 :
    print('%d은 3의 배수입니다'%num)
else :
    print('%d은 3의 배수가 아닙니다'%num)