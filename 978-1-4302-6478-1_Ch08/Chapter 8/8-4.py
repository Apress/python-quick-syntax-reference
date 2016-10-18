#=============================
# 8-4.py - Variables in and out of functions
#=============================
a = 5
def test(a):
    print('A = %d' % a)
    a += 10
    print('A is now %d' % a)

print('A starts with %d' % a)
test(a)
print('After test function a = %d' % a)
