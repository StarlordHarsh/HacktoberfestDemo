import random

def MidnightDice(dice):
	main=[]
	mainKeep=[]
	
	player=input("Player Name : ")
	while True:
		roll=int(input("1. Roll\n2. Quit\n\nEnter Your Choice : "))
		if roll==1:
			outComes=[]
			for chance in range(dice):
				outComes.append(random.randrange(1,7))
			main.append(outComes)
			print("\n\t\t",outComes)
			keep=input("\nDice you wanna choose. You should Choose at least ONE :  ").split(" ")
			for choice in keep:
				if int(choice) in outComes:
					mainKeep.append(int(choice))
					dice-=1
				else:
					print("Invalid choice")
					exit()
			
		if roll==2:
			exit()
			
		if roll>2:
			print("Invalid Option")
			exit()
			
		if dice<=0:
			break
	print("\n\n\n\t\t",mainKeep)
	if 1 in mainKeep and 4 in mainKeep:
		mainKeep.remove(1)
		mainKeep.remove(4)
		print("\n\n\n"+player+"'s score is  ",sum(mainKeep))
	
	else:
		print("Your choice doesn't have 1 and 4. So its not Considerable")
		
		

MidnightDice(6)	
				
		
		
		