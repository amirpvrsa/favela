
def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

calculator_dic = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}

def calculator():
    should_continue = True
    
    n1 = float(input("what is your first number ?\n Your first number is : "))
    for key in calculator_dic:
        print(key)
    operation = input("which operatation do you wanna use from the above list ?  ")
    while should_continue == True:    
        n2 = float(input("what is your second number of calcualtion ? "))
        selected_operation = calculator_dic[operation]
        answer = selected_operation(n1,n2)
        print(answer)
        remain = input(f"do you wish to continue calculating with {answer} ? type Y if yes , type N to go to new calculation")
        if remain == "N":
            should_continue =False
            calculator()
        if remain == "Y":
            n1=answer
        
calculator()