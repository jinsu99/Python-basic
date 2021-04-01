# 문제1-1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
s = s[1:len(s)]
str = s.split('/')
for s in str :
    print("'{0}'".format(s), end=' ')

# 문제1-2. 디렉토리 경로명과 파일명을 분리하여 출력하세요.
