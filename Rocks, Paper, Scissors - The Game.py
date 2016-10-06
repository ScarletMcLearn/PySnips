

m = int (raw_input('Choose your weapon ninga : 1 = Rock, 2 = Paper, 3 = Scissors.'))



import random

c = random.randrange(1,4)

if c == 1 and m == 1:
   print ("You picked Rock. I also picked Rock. The Match is a draw.")
elif m == 2 and c == 1:
  print ("You picked Paper. I picked Rock. I won niga! Wazza?")
elif m == 3 and c == 1:
  print ('You picked Scissors. I picked Rock. Shhhhhot! You won..')

elif (c == 2 and m == 2):
         print ('You picked Paper. I picked Paper. Real nigga ride dirty together. Draww!')
elif ( m == 1 and c == 2):
  print ('You picked Rock. I picked Paper. You wrapped me up. You won =_= ')
elif ( c == 2 and m == 3):
  print ('You picked Scissors. I picked Paper. You tore me. You won. *Claps* Bhalo. :( ')
  
elif ( c == 3 and m == 1):
         print ('You picked Rock. I picked Scissors. #Broken #You won real niga.')
elif ( c == 3 and m == 2):
         print ('You picked Paper. I picked Scissors. Nigga, you shreds. I won!')
elif ( c == 3 and m == 3):
         print ('You picked Scissors. I also picked Scissors. Drawwww.')

else:
   print ('Mama. Instructions kintu beshi chilo na. Porle kintu kono problem hoito na. =_= :3 ')
         
         
         
  
