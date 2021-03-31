# 문제8. 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

def my_reverse(str) :
    l = len(str)-1
    res = ''
    for i in range(l, -1, -1) :
        res += str[i]
    return res

str = input('입력 : ')
print('출력 :',my_reverse(str))