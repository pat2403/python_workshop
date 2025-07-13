# 4. function ที่มี parameter และมี return

def calSquareArea(width, long) : #หา พื้นที่สี่เหลี่ยม
    area = width * long
    return area

def calTriangleArea(base, height) : #หา พื้นที่สามเหลี่ยม
    return base * height / 2


print(f'พท.สี่เหลี่ยม กว้าง 10 ยาว 20 คือ {calSquareArea(10, 20)}')
print('----------------------------------------')
print(f'พท.สี่เหลี่ยม กว้าง 5 ยาว 100 คือ {calSquareArea(5, 100)}')
print('----------------------------------------')
print(f'พท.สามเหลี่ยม ฐาน 20 สูง 15 คือ {calTriangleArea(205, 15)}')