import random
def create():
    name=input("Enter your name: ")
    amount=int(input("Enter your amount: "))
    dig='0123456789'
    acc_no=''.join(random.choice(dig) for i in range(6))
    return name,amount,acc_no
def check_bal(bal):
    print("The current balance amount is: ",bal)
    return bal
def deposit(bal):
    dep=int(input("Enter the amount you want to deposit: "))
    bal+=dep
    print("Amount deposited successfully")
    return bal
def withdraw(bal):
    wd=int(input("Enter amount you want to withdraw: "))
    if wd<bal:
        bal-=wd
        print("Amount withdrawn successfully")
    else:
        print("Insufficient amount")
    return bal

print("*****************Welcome to Banking System*******************")
a=input("Do you already have an account? (yes/no)\n")
if a.lower()=='yes':
    na=input("Enter your name: ")
    acc=int(input("Enter account number: "))
    bal=int(input("Enter the current amount: "))
    if len(str(acc))!=6:
        print("Invalid account number")
        exit()
if a.lower()=='no':
    print("Please create an account")
    na,bal,acc=create()
print("Name:  ",na)
print("Amount:  ",bal)
print("Account number:  ",acc)
print("""Enter the following to proceed:
                   1- To Check bank balance
                   2- To Deposit
                   3- To Withdraw
                   4- To Exit""")
while True:
    ch=int(input("Enter your choice: "))
    if ch==1:
        bal=check_bal(bal)
    elif ch==2:
        bal=deposit(bal)
    elif ch==3:
        bal=withdraw(bal)
    elif ch==4:
        print("You are exiting the program. Thank you!")
        break
    else:
        print("Incorrect choice")

    
