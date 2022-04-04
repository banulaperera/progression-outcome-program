# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20212085
# Date : 23 / 11 / 2021


def txtFile():
    """write to a text file"""
    with open('Test.txt' , 'w') as f:
        for i in list:
            lines = "{}{}{}{}{}{}\n".format(i[0], i[1], i[2], i[3], i[4], i[5])
            f.write(lines)

    with open('Test.txt' , 'r') as mF:
        myLines = mF.read()
        print(myLines)    
         
     
def lists():
    """access the stored data from the list"""
    print()
    for i in list:
        print(i[0] , i[1] , i[2] , i[3] , i[4] , i[5] )
    print()   


def table():
    """table"""
    print()
    print("-" * 60)
    print("|" , " " * 24 , "Menu" , " " * 26 , "|")
    print("-" * 60)
    print("|" , " 1 - Horizontal Histrogram" , " " * 29 , "|")
    print("|" , " 2 - Vertical Histrogram" , " " * 31 , "|")
    print("|" , " 3 - Preview of Input data" , " " * 29 , "|")
    print("|" , " 4 - To write in a Text file" , " " * 27 , "|")
    print("|" , " 5 - Quit" , " " * 46 , "|")
    print("-" * 60)
    

def h_histrogram(progress , trailer , retriever , exclude):
    
    """horizontal histrogram"""
    print(" " * 20 , "\u001b[33mHorzontal Histrogram\u001b[0m")
    print()
    total = progress + trailer + retriever + exclude
    # horizontal histrogram code goes here
    print("Progress  ", progress , " :" , "*" * progress )
    
    print("Trailer   " , trailer , " :" , "*" * trailer)
    
    print("Retriever " , retriever , " :" , "*" * retriever)
    
    print("Exclude   " , exclude , " :" , "*" * exclude)

    print("\n")
    print(total , " outcomes in total.")
    print("-" * 70)


def v_histrogram(progress , trailer , retriever , exclude):

    """vertical histrogram"""
    print(" " * 20 , "\u001b[33mVertical Histrogram\u001b[0m")
    print()
    total = progress + trailer + retriever + exclude
    #printing menu bar
    print("Progress" , progress , end =" |")

    print("Trailer" , trailer , end=" |")

    print("Retriever" , retriever , end=" |")

    print("Exclude" , exclude , end="\n")

    # vertical histrogram code goes here
    for i in range(8): 
        
        if i < progress :
            print("  *" , end="            ")
            
        else:
            print("              " , end=" ")
            
        if i < trailer :
            print("*" , end="            ")
            
        else:
            print("            " , end=" ")
            
        if i < retriever:
            print("*" , end="            ")
            
        else:
            print("            " , end=" ")
            
        if i < exclude:
            print("*" , end="            ")
            
        else:
            print("            " , end=" ")                          
                    
        print("\n")
    print(total , "outcomes in total.")
    print("-" * 70)



#main function starts from here      
print()
print(" " * 20 , "\u001b[4mStaff Version with Histrogram\u001b[0m")
print()
# assign total no. of input values to 0
progress = 0
trailer = 0
retriever = 0
exclude = 0
list = []

while True:  
    try:
        
        passCr = int(input("Please enter your credits at pass:\n "))
        if passCr not in range(0,121,20): #validate that the input values are in the range 0, 20, 40, 60, 80, 100, 120
            print("\nOut of range")
            break
            
        deferCr = int(input("Please enter your credit at defer:\n "))
        if deferCr not in range(0,121,20): #validate that the input values are in the range 0, 20, 40, 60, 80, 100, 120
            print("\nOut of range")
            break
            
        failCr = int(input("Please enter your credit at fail:\n "))
        if failCr not in range(0,121,20): #validate that the input values are in the range 0, 20, 40, 60, 80, 100, 120
            print("\nOut of range")       
            break
        
        total = passCr + deferCr + failCr 

        if total == 120: #validate that the total equals to 120
          # progress calculation     
            if passCr == 120:
                print("\nProgress\n")
                progress += 1
                count_list = ["Progress - " ,passCr,", ",deferCr,", ",failCr]

            elif passCr == 100:
                print("\nProgress (module trailer)\n")
                trailer += 1
                count_list = ["Progress (module trailer) - " ,passCr,", ",deferCr,", ",failCr]

            elif failCr <= 60 and passCr <= 80:
                print("\nModule retriever\n")
                retriever += 1
                count_list = ["Module retriever - " ,passCr,", ",deferCr,", ",failCr]

            else:
                print("\nExclude\n")
                exclude += 1
                count_list = ["Exclude - " ,passCr,", ",deferCr,", ",failCr]

            list.append(count_list) # Modify the list       

        else:
            print("Total incorrect")

        user = str(input("Would you like to enter another set of data? Enter 'y' for yes or 'q' to quit:\n ")) # ask from user that he wants to continue the programe or not
        print()
        
        if user == "y":
            continue
        
        elif user == "q":
            
            table() # Calling table function
            
            x = int(input("Press the number:\n ")) # if the user input q ask whether that he want hotizontal histrogram or vertical histrogram

            print("-" * 70, "\n")

            if x == 1: # if the user inputs 1 programe runs the horizontal histrogram

                h_histrogram(progress , trailer , retriever , exclude)
                break

            elif x == 2: # if the user inputs 2 programe runs the vertical histrogram

                v_histrogram(progress , trailer , retriever , exclude)
                break

            elif x == 3:
                lists()
                break
            
            elif x == 4:
                txtFile()
                break

            elif x == 5:
                 break
            
            else:
                print()
                print("Invalid option")
                print()

        else:
            print("Invalid option")        
            
    except ValueError: # if the user not enters the integer value it dispaly a invalid integer 
        print("\nInteger required")
        break
print()
print("Have a nice day!")
print()
    
