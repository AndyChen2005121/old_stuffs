def win():
	print "You won the game!\n"

def lose():
	print "You lose the game!\n"

def unknown():
	print "I don't know what are you doing. STOP."

print "You enter a dark room with three doors.  Do you go through door #1, door #2 or door #3?"
print "(Or type 4 to stumble around.)"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake.  What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Attack the bear."
	print "4. Do nothing."

	bear = raw_input("> ")

	if bear == "1":
		print "The bear eats your face off."
		lose()
	elif bear == "2":
		print "The bear eats your legs off."
		lose()
	elif bear == "3":
		print "The bear eat you."
		print "Now you're at the bear's stomach. What do you do?"
		print "1. Take a tour in it."
		print "2. Sting it's stomach with sharp things."
		print "3. Do nothing."

		body = raw_input("> ")

		if body == "1":
			print "You followed through the body but you can't breathe and die."
			lose()
		elif body == "2":
			print "The bear can't stand this sting and vomited. You finally get out!"
			win()
		elif body == "3":
			print "The acid in the stomach rot you."
			lose()
		else:
			unknown()
	elif bear == "4":
		print "Well, that is probably better.  Bear runs away." 
		win()
	else:
		unknown()


elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina. What do you see?"
	print "1. Blueberries."
	print "2. Yellow jacket clothspins."
	print "3. Understanding revolvers yelling melodies."

	insanity = raw_input("> ")

	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello."
		win()
	elif insanity == "3":
		print "The insanity rots your eyes into a pool of muck."
		print "Now you can't see anything. What do you do?"
		print "1. Stumble around."
		print "2. Just stand there."

		see = raw_input("> ")

		if see == "1":
			print "You stumbled around and fall on a knife and die."
			lose()
		elif see == "2":
			print "You stood there and can't get out anymore, since the door is permantly closed."
			lose()
		else:
			unknown()

	else:
		unknown()


elif door == "3":
	print "You saw a computer in the room. What do you do?"
	print "1. Play the computer."
	print "2. Stare at the computer."
	print "3. Destroy the computer."

	computer = raw_input("> ")

	if computer == "1":
		print "You played it and you suddenly dropped into an unknown place."
		print "But it wasn't the ending."
		print "Now you're at a mysterious world. What do you do?"
		print "1. Shout out something."
		print "2. Explored it."
		print "3. Tried to run to a door."

		place = raw_input("> ")

		if place == "1":
			print "The shout doesn't help you, but you attracted a monster to eat you."
			lose()

		elif place == "2":
			print "You explored for a while, accidently entered a portal and backed to the computer room."
			win()

		elif place == "3":
			print "You tried but not paying attention to the cliff below. You landed hard on the rock like a broken egg."
			lose()

		else:
			unknown()

	elif computer == "2":
		print "You stared at it and nothing happened."
		win()
	elif computer == "3":
		print "The damaged computer caused a huge fire and you are burned like a charcoal."
		lose()
	else:
		unknown()


elif door == "4":
	print "You stumble around and fall on a knife and die."
	lose()

else:
	unknown()