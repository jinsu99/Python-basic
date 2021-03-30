# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
str = s.split('/')

l = len(str)
print(l)

for i in range(l) :
    if i!=l-1 :
        print('{0}/'.format(str[i]),end='')
    else :
        print('\n{0}'.format(str[i]))