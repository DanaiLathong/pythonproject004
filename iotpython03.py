#Function 3 : No Parameter/Have Return ***
def funcA( ):
    print('AAA')
    print('BBB')
    return 'wow wow wow'

def funcB( ):
    return 999, True, 10+20

# funcA( ) เขียนได้  แต่เขาไม่ทำกัน
print( funcA( ) )
x = funcA( )
a, b, c = funcB( ) #***
print(f'{a} {b} {c}')