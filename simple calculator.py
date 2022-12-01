while True:
    num1 = int(input("> Enter the first number: "))
    operator = (input("> Enter '+', '-', '*' or '/' "))
    num2 = int(input("> Enter the second number: "))

    if operator == '+':
        answer = num1 + num2

    if operator == '-':
        answer = num1 - num2

    if operator == '*':
        answer = num1 * num2

    if operator == '/':
        answer = num1 / num2

    print("> The answer is " + str(answer))