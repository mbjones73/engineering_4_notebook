##Dice roll code
  import random
min = 1
max = 6
roll_again = "yes"
while roll_again == "yes":          #if you say yes it will roll again
#or roll_again == "y":              
    print ("Rolling the dices...")
    print ("The values are....")
    print (random. randint(min, max))
    print (random. randint(min, max))
    roll_again = input("Roll the dices again?")
