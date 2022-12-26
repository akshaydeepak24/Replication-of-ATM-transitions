print("WELOCOME TO THE ATM")
#showing the user his/her name.
print("name: Mr.John")
#amount avaliable in user account
balance=10000
print("Savings in your account:",balance)
#Showing  info to user

print(""" choose your service 
			1-balance enqiuery
			2-withdraw cash
			3-deposit cash
			4-exit
			""")   
 #taking an option from user
option = int(input("Please enter your choise: "))
        
 #for option 1        
if option == 1:
    print(f"Your current balance is {balance}")
    print("Thank you!\nVisit Again")
                            
#for option 2
if option == 2:
    withdraw_amount = int(input("please enter withdraw_amount : "))
    balance = balance - withdraw_amount
    print(f"{withdraw_amount} is debited from your account")
    print(f"Your updated balance is {balance}")
    print("Thank you!\nVisit Again")

            
#for option 3
if option == 3:
    deposit_amount = int(input("Please enter deposit_amount : "))
    balance = balance + deposit_amount
    print(f"{deposit_amount} is credited to your account")
    print(f"Your updated balance is {balance}")
    print("Thank you!\nVisit Again")
    
#for option 4
if option==4:
    print("thank you!\nVisit Again")
    
#for low balance
if balance<=5000:
    print("Low balance")

           


