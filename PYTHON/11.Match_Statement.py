# "match Statement" is similar to the "switch Statement", but more modern and powerful. 
# PYTHON dont use the "switch" but use the "match".

x = int(input("Enter the Number: \n"))

# Match the value of 'x']

match x:
    case 0:
        print('You entered Zero')
    
    case 1:
        print("you entered One.")

    case 3:
        print("you entered Three.")

    case _ if x < 0:
        print("You entered Negative number.")
    
    case _ if x > 2 :
        print("you entered a number greater than Two.")

    case _ :
        print("Unknown")



# Note:
  # No need to use the break;