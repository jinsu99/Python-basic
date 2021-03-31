# 문제4. 가로로 구구단 출력하기

for i in range(2,10) :
    for j in range(1,10) :
        print('%2d x %2d = %2d\t'%(j,i,(i*j)), end='')
    print()