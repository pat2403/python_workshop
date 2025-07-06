# output statment Ep.02
# กรณี print เดียวมีข้อมูลหลายประเภท
# แบบที่ 1 ใช้ , คั่น โดยทุกๆ , จะเว้นวรรค 1 sapce (1 ตัวอักษร)
fullname = 'Somjai'
print('AAAA', 1111, 10 + 20 + 30,True, 'Wow wow wow',fullname)

# แบบที่ 2 ใช้ + คั่น แต่มีข้อกำหนดอยู่ว่า ข้อมูลใดที่ไม่ใช่ string ต้องแปลงให้เป็น string
# และ โดยทุกๆ + จะไม่เว้นวรรค
print('AAAA' + str(1111) + str((10 + 20 + 30))+str(True)+ 'Wow wow wow',fullname)
print('AAAA' + ' '+str(1111)+' ' + str((10 + 20 + 30))+' '+str(True)+' '+ 'Wow wow wow'+ ' '+fullname)

# แบบที่ 3 ใช้เมธอด format() คือ ตรงไหนไม่ใช่ string รวมถึงตัวแปรและนิพจน์ ให้ใส่ {} แล้วเอาข้อมูลที่ไม่ใช้ string ไปใส่ใน () ของเมธอด format()
print('AAAA {} {} {} Wow wow wow {}'.format(1111, 10+20+30, True, fullname))

# แบบที่ 4 ใช้ f-string มีข้อกำหนด ตรงไหนไม่ใช่ string ให้ใส่ข้อมูล ตัวแปร นิพจน์ {}
print(f'AAAA {1111} {10+20+30} {True} Wow wow wow {fullname}')
