def arithmetic_arranger(problems, show_answers=False):
    
    # If there are more than 5 problems, then an error will be returned. Max 5 only! 
    if len(problems) > 5:
        return 'Error: Too many problems.'
    
    # Declaring variables for the problems
    first_operands = []
    second_operands = []
    operators = []
    answers = []

    # Assigning problem to variables to capture their value
    for problem in problems:
        parts = problem.split()
        first_operand = parts[0]
        operator = parts[1]
        second_operand = parts[2]
        
        if operator not in ('+', '-'):
            return "Error: Operator must be '+' or '-'."
        
        if not first_operand.isdigit() or not second_operand.isdigit():
            return 'Error: Numbers must only contain digits.'
        
        if len(first_operand) > 4 or len(second_operand) > 4:
            return 'Error: Numbers cannot be more than four digits.'
        
        first_operands.append(first_operand)
        operators.append(operator)
        second_operands.append(second_operand)
        
        if show_answers:
            if operator == '+':
                answers.append(str(int(first_operand) + int(second_operand)))
            else:
                answers.append(str(int(first_operand) - int(second_operand)))
    
    first_line = ''
    second_line = ''
    dashes_line = ''
    answers_line = ''
    
    for i in range(len(problems)):
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        first_line += first_operands[i].rjust(width)
        second_line += operators[i] + second_operands[i].rjust(width - 1)
        dashes_line += '-' * width
        
        if show_answers:
            answers_line += answers[i].rjust(width)
        
        if i < len(problems) - 1:
            first_line += ' ' * 4
            second_line += ' ' * 4
            dashes_line += ' ' * 4
            if show_answers:
                answers_line += ' ' * 4
    
    arranged_problems = first_line + '\n' + second_line + '\n' + dashes_line
    if show_answers:
        arranged_problems += '\n' + answers_line
    
    return arranged_problems

# arithmetic_arranger(["3801 - 2", "123 + 49"])
