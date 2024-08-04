# 08.02 경원튜터님 클래스 만들기 숙제
class Pizzashop:

    def __init__(self, name, price, *topping):
        self.name = name
        self.price = price
        self.topping = list(topping)

    def __str__(self):
        return f'{self.name}피자, 가격은 {self.price}이고, 토핑은 {self.topping} 추가하실 수 있습니다.'

    def __add__(self, other):
        tuesday = 0.5                       #Buy one, get one free 피자 1+1
        return (self.price + other.price) * tuesday

    # def __add__(self, topping):           #아 시간 부족으로 이건 실패
    #     pepperoni = 1000
    #     cheeze = 1000
    #     onion = 500
    #     return self.price + self.topping

    def __sub__(self, topping):
        self.topping.remove(topping)
        return self.topping



p1 = Pizzashop('페퍼로니', 14000, 'pepperoni')
p2 = Pizzashop('고르곤졸라', 11000, 'cheeze')
p3 = Pizzashop('콤비네이션', 13000, 'pimento','onion','tomato')      #아 영어 힘든데 걍 한국말해
p4 = Pizzashop('쉬림프피자', 20000, '새우', '할라피뇨')

#이 피자 뭐예요?
print(p3)       #콤비네이션피자, 가격은 13000이고, 토핑은 ['pimento', 'onion', 'tomato'] 추가하실 수 있습니다.
print(p4)       #쉬림프피자피자, 가격은 20000이고, 토핑은 ['새우', '할라피뇨'] 추가하실 수 있습니다.

#화요일은 피자 1+1 행사
print(p1 + p2)              #14000 + 11000 = 25000 반값해서 12500
print(p3 + p4)              #16500.0

#저 이거 못 먹는뎅
print(p3 - 'pimento')       #콤비네이션 피자에 피망 빼서 ['onion', 'tomato']


