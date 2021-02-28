print "enter your math sentence here:\n"

a = int(raw_input("First number: "))
calc = raw_input("Symbol: ")
b = int(raw_input("Second number: "))

if "+" in calc:
	print "%d + %d = %d" % (a, b, a + b)
elif "-" in calc:
	print "%d - %d = %d" % (a, b, a - b)
elif "*" in calc:
	print "%d * %d = %d" % (a, b, a * b)
elif "/" in calc:
	print "%d / %d = %d" % (a, b, a / b)
else:
	print "Error! Try again."