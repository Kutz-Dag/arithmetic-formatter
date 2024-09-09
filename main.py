def arithmetic_arranger(problems, show_answers=False):
    # problems: A list of arithmetic problems (strings in the format "number1 operator number2").
    # show_answers: A boolean flag that determines whether to show the answers to the problems.
    
    if len(problems) > 5:
        return 'Error: Too many problems.'
        # If the number of problems exceeds 5, the function returns an error message, as it only supports a maximum of 5 problems for formatting.
    
    first_operands = []
    second_operands = []
    operators = []
    answers = []
    # These lists will store the individual components (first number, operator, second number, and answer) of each problem.
    
    for problem in problems:
        parts = problem.split()
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]
        # Each problem string is split into three parts:
        # first_operand: the first number.
        # operator: the arithmetic operator (+ or -).
        # second_operand: the second number.
          
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
             # Operator validation: Ensures the operator is either + or -. Any other operator returns an error.
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
            # Digit validation: Checks that both operands contain only digits. If either operand has non-numeric characters, an error is returned.
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
            # Length validation: Ensures that neither operand exceeds four digits. If so, an error is returned.
  
        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)
        # After validation, the function stores the operands and operators into their respective lists.
        
        if show_answers:
            if operator == '+':
                answers.append(str(int(first_operand) + int(second_operand)))
            else:
                answers.append(str(int(first_operand) - int(second_operand)))
        # If the show_answers flag is True, the function computes the answer for each problem and stores it in the answers list. Addition or subtraction is performed based on the operator.
    
    # These strings will store the formatted output for each problem, broken into lines for:
    
    first_line = ''
    # first_line: the first operand of each problem.
    
    second_line = ''
    # second_line: the second operand, with the operator.
    
    dashes_line = ''
    # dashes_line: a line of dashes separating the problem from the answer.
    
    answers_line = ''
    # answers_line: the computed answer (only populated if show_answers is True).
    
    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        # Width calculation: The width for each problem is determined by the longer operand, plus 2 spaces (for padding and the operator).
        
        first_line += first_operands[i].rjust(width)
        second_line += operators[i] + second_operands[i].rjust(width - 1)
        # rjust(width): Aligns the operands and answers to the right, ensuring proper spacing.
        
        dashes_line += '-' * width
        # The function concatenates each formatted problem into the respective lines (first_line, second_line, and dashes_line).
        
        if show_answers:
            answers_line += answers[i].rjust(width)
        
        if i < len(problems) - 1:
            first_line += ' ' * 4
            second_line += ' ' * 4
            dashes_line += ' ' * 4
            if show_answers:
                answers_line += ' ' * 4
        # Adds 4 spaces between each problem to create a clear visual separation in the output.
    
    arranged_problems = first_line + '\n' + second_line + '\n' + dashes_line
    if show_answers:
        arranged_problems += '\n' + answers_line
    # The final output is constructed by combining the three main lines (operands and dashes), and if the answers are requested, the answers_line is added as well.
    
    return arranged_problems
    # Returns the formatted string that displays the arranged arithmetic problems.

arithmetic_arranger(["3801 - 2", "123 + 49"])
# Example of function usage
