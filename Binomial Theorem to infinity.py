x = float(input('The value of x'))
first_term = 1
term_number_counter = 1
term_number = float(input('no. of terms'))

print ("1",)

if (x < 1) and (x > -1):
  while term_number != term_number_counter:
    sum_value = x + 1
    print ( "+", x,)
    x = x*x
    term_number_counter = term_number_counter + 1

  print ('=', sum_value,)    

else:
    print ('wrong inputs')



    
