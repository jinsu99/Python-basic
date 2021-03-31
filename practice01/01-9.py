#문제9. 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴 : ')
price = { '오뎅':300, '순대':400, '만두': 500 }

if menu in price.keys() :
    print('가격 : {0}원 '.format(price[menu]))
else :
    print('가격 : 0')
