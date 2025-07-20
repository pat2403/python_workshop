# ชนิดข้อมูลแบบ Tuple
# ประกอบด้วยข้อมูลหลายข้อมูล
# ที่แต่ละข้อมูลมี index number กำกับ โดยเริ่มจาก 0
# ทุกข้อมูลไม่สามารถเปลี่ยนค่าได้
# ต้องเขียนใน ()
# เพิ่มข้อมูลได้ ลบข้อมูลออก ไม่ได้ 
# การเข้าถึงข้อมูลใน Tuple ใช้ index number

tupleData1 = (10, 20, 30, 40)
tupleData2 = (10, 20, 'สมชาย', True, [1, 2, 3])
print(tupleData1[2])
print(tupleData1[-2])
print('-----------------------------')
print(tupleData2[3])
print(tupleData2[-2])
print('-----------------------------')
print(tupleData2)
#tupleData2[2] = 'สมหญิง' # ******Error******