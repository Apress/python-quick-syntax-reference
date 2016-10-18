#=============================
# 7-4.py yield example
#=============================
def CreateGen():
    mylist = range(5)
    print mylist
    for i in mylist:
        yield i*i
        
mygen = CreateGen()
for cntr in mygen:
    print(cntr)
