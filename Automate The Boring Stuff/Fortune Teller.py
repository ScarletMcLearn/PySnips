# import random
# def getAnswer(answerNumber):
#        if answerNumber == 1:
#            return 'It is certain'
#        elif answerNumber == 2:
#            return 'It is decidedly so'
#        elif answerNumber == 3:
#            return 'Yes'
#        elif answerNumber == 4:
#            return 'Reply hazy try again'
#        elif answerNumber == 5:
#            return 'Ask again later'
#        elif answerNumber == 6:
#            return 'Concentrate and ask again'
#        elif answerNumber == 7:
#            return 'My reply is no'
#        elif answerNumber == 8:
#            return 'Outlook not so good'
#        elif answerNumber == 9:
#            return 'Very doubtful'



# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)


# print ('Hello', 'There', sep=',')
# print 'World'



def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))