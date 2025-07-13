# control statement Ep.03
# คำสั่ง break และ continue ใน loop
# break -> หยุด loop ที่กําลังทำงาน
# continue -> ไม่ทำงานของ loop ที่กําลังทำงาน

for x in range(1, 6) :
    print(f'{x} SAU')
    if x == 3 :
        break
    print(f'{x} IoT')
print('------------------------')
for x in range(1, 6) :
    print(f'{x} SAU')
    if x == 3 :
        continue
    print(f'{x} IoT')