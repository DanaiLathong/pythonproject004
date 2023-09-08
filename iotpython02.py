#Function 2 : Have Parameter/No Return
#parameter คือ ตัวแปรประเภทหนึ่ง
# จะใช้ได้เฉพาะในฟังก์ชั่นนั้นๆ เท่านั้น
def  funcA( x, y) :
    print('Hi...')
    z = x + y
    print(f'{x} + {y} = {z}')
    #ไม่มีคำสั่ง Return

def funcB( x ) :
    print(f'X is {x} 555...')

funcA(10,20) #Aregument คือ ข้อมูลที่ส่งไปให้ Parameter
funcA(5,5)
funcB('SAU IOT')