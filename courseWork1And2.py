# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20212085
# Date : 21 / 11 / 2021


def progression(passCr , deferCr , failCr):

    """Progress calculation"""
    
    total = passCr + deferCr + failCr

    if total == 120:
        # progress calculation
        if passCr == 120:
            print("\nProgress")
            
        elif passCr == 100:
            print("\nProgress (module trailer)")
        
        elif failCr <= 60 and passCr <= 80:
            print("\nModule retriever")
            
        else:
            print("\nExclude")
                        
    else:
        print("\nTotal incorrect")

# main function starts from here
print()
print(" " * 25 , "\u001b[4mMain Version\u001b[0m")
print()
while True :
    
    try:
        passCr = int(input("Please enter your credits at pass:\n "))
        if passCr not in range(0,201,20):   #validate that the input values are in the range 0, 20, 40, 60, 80, 100, 120
            print("\nOut of range")
            break
        
        deferCr = int(input("Please enter your credit at defer:\n "))
        if deferCr not in range(0,201,20):  #validate that the input values are in the range 0, 20, 40, 60, 80, 100, 120
            print("\nOut of range")
            break
        
        failCr = int(input("Please enter your credit at fail:\n "))
        if failCr not in range(0,201,20):   #validate that the input values are in the range 0, 20, 40, 60, 80, 100, 120
            print("\nOut of range")       
            break
   
        progression(passCr,deferCr,failCr)
        break
          
    except ValueError:  # if the user not enters the integer value it dispaly a invalid integer     
          print("\nInteger required")
          break

print()
print("Have a nice day!")
print()
