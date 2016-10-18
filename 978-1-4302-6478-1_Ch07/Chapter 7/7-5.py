#=============================
# 7-5.py 
#   nonlocal keyword example
# NOTE: Python 3.x ONLY
#=============================
def Funct1():
	test = 1
	def Within():
		nonlocal test
		test = 2
		print("Routine Funct1|Within- test = ", test)
	Within()
	print("Routine Funct1 - test = ", test)
    
def Funct2():
    test = 1
    def Within():
        test = 2
        print("Routine Funct2|Within - test = ", test)
    Within()
    print("Routine Funct2 - test = ",test)
    
Funct2()
Funct1()
