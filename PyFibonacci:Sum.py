#ThisProgramPrintsTheFibonaciSequence

    #FirstWeTakeTheNumberOfTermsToPrintFromUser
number_of_terms=int(input('Koyta Term Pirint Dibuh?:'))

#CreateVariableStartingTermAndNextTerm
#1stAnd2ndTermsOfTheSequence
#StoreTheirValues
starting_term=0
next_term =1
summation = 0

if number_of_terms>0:
    print (starting_term,'',)
    print ( )
    print (summation)

summation=1
if number_of_terms>1:
    print (next_term,'',)
    print ( )
    print (summation)

for iteration in range (3, number_of_terms +1):
    temporary_variable = next_term 
    next_term = next_term + starting_term
    starting_term = temporary_variable
    summation = summation + next_term
    print (next_term,'',)
    print (' ')
    print (summation)
