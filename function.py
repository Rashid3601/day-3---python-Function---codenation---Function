def press_grind_beans():
    print("Grinding for 20 seconds")
press_grind_beans()

coffee_is_grinding = False

def press_grind_beans():
    global coffee_is_grinding
    if coffee_is_grinding:
        print("Stopping the grind")
        coffee_is_grinding = False
    else:
        print("Grinding is about to begin")
        coffee_is_grinding = True 

press_grind_beans()
press_grind_beans() 

#Check day

def cash_withdrawl(amount, accnum):
    print(f"withdrawing {amount} from the account number{accnum}.")

cash_withdrawl(300, 50449921)
cash_withdrawl(30, 50449921)
cash_withdrawl(200, 50447921)

def coffee_order(size, typeofdrink):
    print(f"what is the size of the drink {size} and what is the type of drink {typeofdrink}.")

coffee_order(30, 1)
coffee_order(50, 2)
coffee_order(60, 3)

accnum = 12345678
w_amount = 1000

def cash_withdrawal(amount, acc_real):
    print(f"withdrawing amount {amount} from the account number {acc_real}!")

cash_withdrawal(w_amount, accnum) 


def add_up(num1, num2):
    return num1 + num2

add_up(7,3)
print(add_up(2,5))

#function task - operators

def calculation(a, b):
    return a+b, a-b, a*b, a/b
add, sub, mult, div = calculation(40, 10)
print(f"The result of 40 plus 10 = {add}")
print(f"The result of 40 minus 10 = {sub}")
print(f"The result of 40 times 10 = {mult}")
print(f"The result of 40 divided by 10 = {div}")




