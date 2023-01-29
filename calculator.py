print("Enter first operand: ", end="")
# spot for user to enter first operand

operand_1 = float(input())
# stores input as new variable

print("Enter second operand: ", end="")
# spot for user to enter second operand

operand_2 = float(input())
# stores input as new variable than before

print("Calculator Menu", "---------------", "1. Addition", "2. Subtraction", "3. Multiplication", "4. Division", sep="\n")
# prints out the menu for the user to see

print("Which operation do you want to perform?")
# asks the user what they want to do with the operands

operation = int(input())
# allows input for which operation the user wants to perform

if operation < 1 or operation > 4:
    print("Error: Invalid selection! Terminating program.")
# when the user does not choose a number from the menu then they will receive an error message

else:
    if operation == 1:
        result = operand_1 + operand_2
    # addition operation

    if operation == 2:
        result = operand_1 - operand_2
    # subtraction operation

    if operation == 3:
        result = operand_1 * operand_2
    # multiplication operation

    if operation == 4:
        result = operand_1 / operand_2
    # division operation

    print(f"The result of the operation is {result}. Goodbye!")
# shows the user the final calculation
