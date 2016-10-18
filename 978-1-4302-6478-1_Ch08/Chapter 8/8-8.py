#=============================
# 8-8.py - Anatomy of a Python Program #2
#=============================
a = 24
b = 42

class Test:
	z = 10
	def __init__(self):
		z = 42
		print z
	
	def funct1(self):
		print('Z = %d' % self.z)
		
	def funct2(self):
		pass
		
def function1(varA,varB):
    print(varA,varB)
    
def main():
    t = Test() # instantiate the Test class
    t.funct1() # call the function 'funct1' in the Test class
    
    function1(a,b)  # call the function 'function1' in the "normal" code
    
#...

if __name__ == '__main__' :
    main()
    

    
