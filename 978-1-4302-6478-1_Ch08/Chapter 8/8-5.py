#=============================
# 8-5.py - Variables in and out of functions # 2
#=============================
a = 1
def test1():
    a = 42
    print('Inside test1...a = %d' % a)

def test2():
    global a
    a = a + 1
    print('Inside test2...a = %d' % a)
	
print('a starts at %d' % a)
test1()
print('After test1, a is now %d' % a)
test2()
print('After test2, a is now %d' % a)
