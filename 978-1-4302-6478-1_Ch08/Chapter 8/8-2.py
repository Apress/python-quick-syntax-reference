#=============================
# 8-2.py - Optional Parameters
#=============================
def TestFunction2(val1, val2=0):
    print('Required value = %d' % val1)
    if val2 != 0:  # Only print the line below if val2 was provided
        print('Optional value = %d' % val2)
    
TestFunction2(1) # call function with only one value
print('')
TestFunction2(1,2) # call function with two values
