#=============================
# 4-1.py  - str.translate example
#=============================
from string import maketrans
intable = 'aeiou'
outtable = '12345'
trantable = maketrans(intable,outtable)
a = "The time has come"
print a.translate(trantable)

