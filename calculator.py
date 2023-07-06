# Create a simple calculator application that asks a user to enter two numbers and the operation

# created 3 def functions that returns equations 
def addition (x,y):
    return (x+y)

def subtraction (x,y):
    return (x-y)

def multiplication (x,y):
    return (x*y)

def division (x,y):
    try:
        return (x/y)
    except(ZeroDivisionError):
        return("Division by zero")


def calculator():
# created a def function called calculator 
# while loop runs progarame continually 

    while True:
        if menu == "1":
# if menu equals 1 its goes menu and ask user to enter 2 numbers 
# try and execept catches the error if user types a word  
            try:
                number_1 = int(input("Enter your first number of choice: "))
                number_2 = int(input("Enter your 2nd number of choice: "))
            except ValueError:
                print("Invalid Error, Enter a number not word  ")
                continue
# operations signs asks user to input a prefferd ,if user types in the wrong sign 
# invalid messgae appears                         
            operations_signs = input("Enter your prefferd sign: ")
            if operations_signs not in ("+","-","/","*",):
                print("Invalid Error,Enter +, / ,* , - ")

# line 41 - 54 used if,elif,statements calculate numbers 
            if operations_signs == "+" :
                sum = number_1 + number_2
                print(f" the answer is {sum}")
                    
            elif operations_signs == "-" :
                sum = number_1-number_2
                print(f" the answer is {sum}")
                        
            elif operations_signs == "*" :
                sum = number_1 * number_2
                print(f" the answer is {sum}")
                        
            elif operations_signs == "/" : 
                sum = number_1 / number_2
                print(f"the answer is {sum}")
                
                
# writing to a file that writes the equations into a file     
                with open("output.txt","a") as f:
                    f.write(str(number_1)+" "+operations_signs+" "+str(number_2)+" "+ "=" +" "+str(sum)+"\n" )
                
            return menu
                        
def view_calculations():
# created a def function 

    while True:
 # while loop runs continually if the condition is met       
        if menu == "2" :
# if user selectes 2 they can view their equations 

# user_input asks user to enter the file they want to view 
            user_input = input("\n Enter the file you would like to view:")

# opens the f and reads the data 
# try and accept block catches the error and prints out message 
            try:
                with open(user_input,"r") as f :
                    lines = f.readlines()
                    for line in lines:
                        print(line)   
                    
            except FileNotFoundError:
                print("The file you are trying to access does not exist")
                
            return menu             
 
#while loop runs continually if the condition is met                                               
while True :  
    print("The JM2.0_pro_max Calculator")    

# menu is created to allow user to make a choice 
    menu = input("\n 1.calculator \n 2.To view calculations. \n 3.To exit \n ")        
 
# line 97-103 calls the def fucntions to activate            
    if menu == "1":
        calculator()
    
    elif menu == "2":
        view_calculations()
    
    elif menu == "3":
       print("Goodbye")
       break 
 
 # if user enters by mistake a wrong selction messgae will dispaly 
 
    else:
        print("Invalid option")

        
        
    

               
                








