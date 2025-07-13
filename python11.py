# 2. function ที่มี parameter และไม่มี return

def sayHi(name, year_born) : 
    print(f'สวัสดีคุณ {name}')
    print(f'คุณเกิดในปี พ.ศ.{year_born} ตอนนี้คุณอายุ {2568 - year_born} ปี')

def sumNumber(n1, n2) :
        print(f'{n1} + {n2} = {n1 + n2}')

sayHi('Sombat', 2500) # ข้อมูลที่ส่งใน parameter เราเรียกว่า argument
sayHi('Somjai', 2525)

sumNumber(10, 20)
sumNumber(100, 200)

sayHi('Somsri', 2545)