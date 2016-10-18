#=============================
# 7-2.py class example
#=============================
class test1:
    def __init__(self,inval):
        self.a = inval #dummy statement
		
    def run(self):
        for cntr in range(self.a):
            print cntr

t = test1(20)
t.run()
