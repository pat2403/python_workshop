# Function (การงานหนึ่งๆ) Ep.01
# นิยาม คือ การทำงานหนึ่งๆ จำไม่ทำงานหากไม่ถูกเรียกใช้ (call function)
# Function มี 4 ประเภทใหญ่
# 1. ไม่มี return
# 2. มี return แต่ไม่มี argument
# 3. มี return และมี argument
# 4. ไม่มี return และไม่มี argument

# การสร้าง function ใน python ต้องมีคีย์เวิร์ด def
# 1. function ที่ไม่มี parameter และไม่มี return
def say_h() :
    print('hello...')
    print('hi...')
    print('Hey...')

def show_cal() :
    print(10 + 20 + 30)
    x = 10 
    y = x 
    print(x + y)

say_h()
show_cal()
say_h()
say_h()