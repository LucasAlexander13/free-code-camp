def arithmetic_arranger(problems, result = False):

    if len(problems) > 5:
        return "Error: Too many problems."

    for problem in problems:
        if "x" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."
    
    for problem in problems:
        for value in problem:
            if value.isalnum():
                return "Error: Numbers must only contain digits."

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))