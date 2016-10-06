def collatz(number):
	
		#number % 2
		number = int(number)
		if (number % 2 == 0):
			print (number // 2)
			return (number // 2)

		else:
			print (3*number + 1)
			return (3*number + 1)


print
print

print("We Are Going To Show The Number Of Trials Till You Finish The Cobalz Sequence.")


#counter = 0


while (True):
	
	print
	print

#	print("We Are Going To Show The Number Of Trials Till You Finish The Cobalz Sequence.")
	try: 
		number = int(raw_input("Please Enter Your Number: "))

		#number = 3
		counter = 0

		while ( (number)  != 1):
			number = collatz(number)
			counter = counter + 1

		print
		print"It took ", counter, " number of steps to end."

	except (ValueError):
		print
		print "Puppies!"
