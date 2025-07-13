# function แบบ default parameter
# default parameter คือ พารามิเตอร์ที่มีการกำหนดค่า default ให้มัน
# โดนเวลาเรียกใข้ฟังก์ชัน หากไม่ส่งค่าพารามิเตอร์ตัวนั้น จะใช้ค่า default ที่กําหนดไว้

def sumNumber(n1, n2,n3 = 10, n4 = 100) :
    print(n1 + n2 + n3 + n4)


def sayhello(name = 'no-name'):
    return f'สวัสดีคุณ {name}'

print(sayhello('Sombat'))
print(sayhello())
print(sayhello('Somjai'))

sumNumber(10, 10 ,20 ,20)
sumNumber(100, 200, 50)
sumNumber(0, 0)