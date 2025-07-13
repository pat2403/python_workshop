# Primitive Data types (ขนิดข้อมุลพื้นฐาน)
# 1. integer
# 2. float
# 3. boolean
# 4. string
# 5. Complex Number จำนวนเชิงซ้อน เช่น 1 + 2j

# Compound Data types (ขนิดข้อมูลแบบกลุ่ม)
# 1. list
# 2. tuple
# 3. set
# 4. dictionary
# ---------------------------------------------
# ขนิดข้อมูลแบบ List
# ประกอบด้วยข้อมูลหลายข้อมูล ที่แต่ละข้อมูลมี index number กำกับ และทุกข้อมูลสามารถเปลี่ยนค่าได้ และต้องเขียนใน []
listData1 = [10, 20, 30, 40]
listData2 = [10, 20, 'สมชาย', True, [1, 2, 3]] 
print(listData1[2]) #เข้าถึงข้อมูล 30
print(listData1[-2]) #เข้าถึงข้อมูล 30
print('-----------------------------')
print(listData2[3]) #เข้าถึงข้อมูล True
print(listData2[-2]) #เข้าถึงข้อมูล True
print('-----------------------------')
listData2[2] = 'สมหญิง' #เปลี่ยนค่าข้อมูล
print(listData2)
listData2[4][0] = 111
listData2[4][1] = 333
print(listData2)