# input statement ตัว python ใช้คำสั่ง input()
# แต่มีข้อกำหนดว่า input() จะรับข้อมูลเป็น string เท่านั้น 
# คำสั่งแปลง string เป็นตัวเลข ต้องแปลงด้วย int(), float(), ....

fname = input("ป้อนชื่อ : ")
year_born = input('ป้อนปีเกิด พ.ศ. : ')
salary = float(input('ป้อนเงินเดือน : '))

print(f'สวัสดีคุณ {fname}')
print(f'คุณเกิดในปี พ.ศ.{year_born} ตอนนี้คุณอายุ {2568 - int(year_born)} ปี')
print(f'เงินเดือนของคุณ {salary} บาท ภาษี 7% เป็นเงิน {salary * 7 / 100} บาท')