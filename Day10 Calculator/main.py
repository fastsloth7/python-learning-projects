from calculate import calculate, operator_function

while True:
    try:
        starting_number = float(input("What's the first number? "))
    except ValueError:
        print("Only a decimal number is accepted.")
        continue

    calculation_on = True

    while calculation_on :
        operator = input("Which operation you want to apply\n+\n*\n-\n/\n")
        if operator not in operator_function:
            print("Please enter valid operator")
            continue
        try:
            num2 = float(input("What is the next number? "))
        except ValueError:
            print("Only a decimal number is accepted.")
            continue
        try:
            starting_number = calculate(starting_number, operator, num2)
        except ZeroDivisionError:
            print("Error, you can divide a number with zero.")
            continue

        print(f"Your ans is {starting_number}")
        ok = input("Type 'y' to apply operation on ans. Type 'n' to continue from the start, Type 'x' to exit ")
        if ok == 'n':
            calculation_on = False
        elif ok == 'x':
            exit()