from math_operations import Calculator
from Operators_dict import Operators
def in_to_post(exercise):
    """
    Converts an infix expression to a postfix expression
    """
    operators_lst = []
    expression = []
    current = 0

    for char in exercise:
        # If the number has a factorial (!) compute it and add to the expression
        if char.endswith("!") and char.rstrip("!").isdigit():
            expression.append(Calculator.factorial(int(char.rstrip("!"))))
        # If the number has a negation (~) compute it and add to the expression
        elif char.startswith("~") and char.lstrip("~").isdigit():
            expression.append(Calculator.negation(int(char.lstrip("~"))))

        # If the character is a number add it to the expression
        elif char.isdigit():
            expression.append(int(char))

        # If the character is a decimal number, add it to the expression
        elif char.replace('.', '', 1).replace('-', '', 1).isdigit():
            expression.append(float(char))
        elif char.replace('.', '', 1).replace('-', '', 1).replace('!','',1).isdigit():
            expression.append(Calculator.factorial(int(char.rstrip("!").lstrip('-')))*-1)
        else:
            # If its an opening parenthesis add it to the stack
            if char == "(":
                operators_lst.append(char)
            # If its a closing parenthesis pop until an opening parenthesis
            elif char == ")":
                while operators_lst and operators_lst[-1] != "(":
                    expression.append(operators_lst.pop())
                # Pop the opening parenthesis and dont add it
                if operators_lst and operators_lst[-1] == "(":
                    operators_lst.pop()
            # If the stack is empty or has an opening parenthesis add the operator to the stack
            elif len(operators_lst) == 0 or operators_lst[-1] == "(":
                operators_lst.append(char)
            else:
                # While there are operators in the stack with higher or equal precedence pop them
                while (
                    len(operators_lst) != 0
                    and operators_lst[-1] != "("
                    and Operators[char] <= Operators[operators_lst[-1]]
                ):
                    expression.append(operators_lst.pop())
                # Add the current operator to the stack
                operators_lst.append(char)

    # At the end, pop all remaining operators from the stack to the expression
    while len(operators_lst) != 0:
        expression.append(operators_lst.pop())

    return expression
