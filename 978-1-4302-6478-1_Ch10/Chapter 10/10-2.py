#=============================
# 10-2.py - Dog Class example #2
#=============================

class Dog():
    def __init__(self,dogname,dogcolor,dogheight,dogbuild,dogmood,dogage):
        #here we setup the attributes of our dog
        self.name = dogname
        self.color = dogcolor
        self.height = dogheight
        self.build = dogbuild
        self.mood = dogmood
        self.age = dogage
        self.Hungry = False
        self.Tired = False
        
    def Eat(self):
        if self.Hungry:
            print 'Yum Yum...Num Num'
            self.Hungry = False
        else:
            print 'Sniff Sniff...Not Hungry'
            
    def Sleep(self):
        print 'ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ'
        self.Tired = False
        
    def Bark(self):
        if self.mood == 'Grumpy':
            print 'GRRRRR...Woof Woof'
        elif self.mood == 'Laid Back':
            print 'Yawn...ok...Woof'
        elif self.mood == 'Crazy':
            print 'Bark Bark Bark Bark Bark Bark Bark'
        else:
            print 'Woof Woof'

            
Beagle = Dog('Archie','Brown','Short','Chubby','Grumpy',12)
Lab = Dog('Nina','Black','Medium','Chubby','Laid Back',8)
Shepherd = Dog('Bear','Black','Big','Skinny','Crazy',14)
Lab.Hungry = True
print 'My name is %s' % Beagle.name
print 'My color is %s' % Beagle.color
print 'My mood is %s' % Beagle.mood
print 'I am hungry = %s' % Beagle.Hungry
Beagle.Eat()
Beagle.Hungry = True
Beagle.Eat()
Beagle.Bark()
print 'My name is %s' % Lab.name
print 'My mood is %s' % Lab.mood
if Lab.Hungry == True:
	print 'I am starving!'
	Lab.Eat()
	Lab.Sleep()
	Lab.Bark()
else:
	print 'No...not hungry.'

