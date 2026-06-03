def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculate():
    num1 = int(input("whats the first number? "))
    for symbol in operations:
        print(symbol)
    continue_ = False
    while not continue_:
        operation_symbol = input("select symbol ")
        num2 = int(input("whats the second number? "))
        calculation_function = operations[operation_symbol]
        answer = float(calculation_function(num1,num2))
        print(num1 ,operation_symbol,num2,"=",answer)

        if input("typ 'y' to continue or typ 'n' to new calculate ")=="n":
            continue_=True
            calculate()
        else:
            num1 = answer
calculate()