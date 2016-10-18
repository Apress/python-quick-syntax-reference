#=============================
# 8-3.py - Optional Parameters #2
#=============================
def TestFunction2(val1, val2=None):
    print('Required value = %d' % val1)
    if val2 != None:
        print('Optional value = %d' % val2)
    
TestFunction2(1)
print('')
TestFunction2(1,0)
