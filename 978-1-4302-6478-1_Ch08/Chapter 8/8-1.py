#=============================
# 8-1.py - Returning Values
#=============================
def TestFunction(val1,val2):
    return val1,val2
    
a,b = TestFunction(3,2)
print('Returned from function... a = %d, b = %d' % (a,b))
