# # hair = ['brown', 'bitch', 'black']

# # eyes = ['1 eye', '2 eyes', 'no eyes']

# # number = [1, 2, 3, 4]


# # for i in range(0, 3):
# # 	print hair[i],
# # 	print number[i],
# # 	print eyes[i],


# the_count = [1, 2, 3, 4, 5]
# fruits = ['apples', 'oranges', 'pears', 'apricots']
# change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# # this first kind of for-loop goes through a list
# for number in the_count:
#     print "This is count %d" % number

# # same as above
# for fruit in fruits:
#     print "A fruit of type: %s" % fruit

# # also we can go through mixed lists too
# # notice we have to use %r since we don't know what's in it
# for i in change:
#     print "I got %r" % i

# # we can also build lists, first start with an empty one
# elements = []

# # then use the range function to do 0 to 5 counts
# for i in range(0, 6):
#     print "Adding %d to the list." % i
#     # append is a function that lists understand
#     elements.append(i)

# # now we can print them out too
# for i in elements:
#     print "Element was: %d" % i





ten_things = "I got one question"

#for i in ten_things:
#	print ten_things[i]

print ten_things

print 

print "Wait.! Not 10 things in there mate!"

things_list = ten_things.split(' ')

#for i in range (0, ten_things.__sizeof__()):
#	print things_list[i]

things_to_be_added = ["How", "Do", "You", "Put", "All", "That", "In", "Them", "Jeans", "?"]


while (len(things_list) != 10):
	next_thing = things_to_be_added.pop()
	print "Adding: ", next_thing
	things_list.append(next_thing)
	print "There are %d items now." %len(things_list)


print "Here we goo Niggo: ", things_list

print things_list[1]
print things_list[-1]
print things_list.pop()

print ' '.join(things_list)

print "#$".join(things_list[3:-1])