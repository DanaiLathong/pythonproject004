#หาพื้นที่สี่เหลี่ยม และ สามเหลี่ยม โดยรับกว้างยาว ฐานสูง ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ
#future การทำงานอะไรบ้าง
# 1.รับค่ากว้างยาว 2.รับค่าฐานสูง 
#3.คำนวณพืนที่สี่เหลี่ยม และ แสดงพื้นที่สี่เหลี่ยม 4.คำนวณพื้นที่สามเหลี่ยม และ แสดงพื้นที่สามเหลี่ยม
def inputWithdlong( ):
    wi = float( input('ป้อนความกว้าง : '))
    io = float( input('ป้อนความยาว : '))
    return wi,io

def inputBaseHigh( ):
    ba = float( input('ป้อนฐาน : '))
    hi = float( input('ป้อนความสูง : '))
    return ba,hi

def calAndShowAreSquare( wi,io ) :
    area = wi * io
    print(f'สี่เหลี่ยมกว้าง {wi} ยาว {io} มีพื้นที่ {area}')

def calAndShowAreSquare( ba,hi ) :
    area = ba * hi
    print(f'สามเหลี่ยมฐาน {ba} สูง {hi} มีพื้นที่ {area}')

wi,io = inputWithdlong( )
calAndShowAreSquare( wi,io )
print('------------------------')
ba,hi = inputBaseHigh( )
calAndShowAreSquare( ba,hi )