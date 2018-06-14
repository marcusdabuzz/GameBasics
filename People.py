
import random

#The person is defnied as a function that have som chars
#Hearts; lives, health
#Strength; actions to take
#Toughness; actions to soakup
#Move; how far to move

def InitativeOrder(Number):
	IntOrder = [0 for y in range(Number)]
	for x in range(Number):
		IntOrder[x]=random.randint(1,Number)
	return IntOrder
	

def Person(Hearts,dH,Strength,dS,Tough,dT,Move,dM):
	#check hearts
	if dH>0:
		Hearts=Hearts-dH
	if dS>0:
		Strength=Strength-dS
	if dT>0:
		Tough=Tough-dT
	if dM>0:
		Move=Move-dM
	return Hearts,Strength,Tough,Move
def Movement(Move,dM):
	if Move==0:
		IntOrder=IntOrder+1
def MoveDirect(OldPlace,Direct,Value,Move):
	#Direct is the direction given in UP,UPR,RIGHT,RIGHTDOWN,DOWN,DOWNLEFT,UPLEFT	
	#Value is the number of steps taken
	#OldPlace is the coordinate for the old place, (x,y)
	#NewPlace is the new coordinate (x,y)
	if Move==0:
		NewPlace=OldPlace
		return Move,NewPlace
	if Move>0 and Value>0:
		NewPlace = Direct*Value+OldPlace
		
		
#this below is a test code
print(InitativeOrder(8))
print(Person(10,0,4,0,5,4,10,5))

