#=============================
# 8-6.py - Variables in and out of functions # 3
#=============================
a = 5
def test(a):
    print('A = %d' % a)
    a += 10
    print('A is now %d' % a)
    return a

print('A starts with %d' % a)
a = test(a)
print('After test function a = %d' % a)

