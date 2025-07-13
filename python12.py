# 3. function ที่ไม่มี parameter และมี return
# return คือ คำสั่งที่จะส่งค่าข้อมูลกลับไปยังจุดเรียกใข้ฟังก์ชัน (จุด call function)

def say_hi() :
    print('Hi...')
    return 'hello world'

def showSenPa() : 
    return '-----------------------'

print( showSenPa())
x = say_hi()
print( showSenPa())
print(x)
