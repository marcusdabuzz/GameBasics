
import random
import copy

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
	

def ChangeOfStats(Hearts,dH,Strength,dS,Tough,dT,Move,dM):
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
def MoveDirect(OldPlace,Direct,Move,Value):
	#Direct is the direction given in UP,UPR,RIGHT,RIGHTDOWN,DOWN,DOWNLEFT,UPLEFT
	#OldPlace is the coordinate for the old place, (x,y)
	#NewPlace is the new coordinate (x,y)
	#Value is the number of steps
	#Move is the number of steps left to take until turn ends
	if Move==0:
		NewPlace=OldPlace
		return Move,NewPlace
	if Move>0 and Value>0 and (Move<=Value==True):
		NewPlace = Direct*Value+OldPlace
		NewValue = copy.copy(Move-Value)
		return copy.copy(NewPlace),Value
	else:
		return OldPlace,Move,Value


#The person is defnied as a function that have som chars
#Hearts; lives, health
#Strength; actions to take
#Toughness; actions to soakup
#Move; how far to move	
#Initiative; when will the person do something
def RandomMook():
	Hearts = random.randint(1,15)
	Strength = random.randint(1,25)
	Toughness = random.randint(1,5)
	Move = random.randint(1,7)
	Initiative = random.randint(1,8)
	return Hearts,Strength,Toughness,Move,Initiative 



#this below is a test code
print(InitativeOrder(8))
print(ChangeOfStats(10,0,4,0,5,4,10,5))
#create some coordinates, directions and the move value
Dir = [1,1]
Move = 5
Value = 3
print(MoveDirect([0,0],Dir,Move,Value))
[a,b,c,d,e]=RandomMook()
print(a,b,c,d,e)
