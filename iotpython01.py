#Function 1 : No Parameter/No Return
def funcA( ) :
    print('Wow')
    print('Woo')
    print('Wee')
    print('Wea')  
    funcB( )  
    #ไม่มีคำสั่ง Return

def funcB( ) :
    print('Hi')
    #funcA( ) ทำได้แต่ไม่ควรทำ
funcA( )
funcA( )
funcB( )
funcA( )