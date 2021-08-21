def first_line(problem):
    max_len = len(max(problem))
    spaces = " " * (max_len - len(problem[0]) + 2)
    beetween = " " * 4
    return f"{spaces}{problem[0]}{beetween}"


def arithmetic_arranger(problems, result = False):

    if len(problems) > 5:
        return "Error: Too many problems."
    
    for problem in problems:
        if "x" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."
    
        for value in problem:
            if value.isalnum():
                return "Error: Numbers must only contain digits."
            elif len(value) > 4:
                return "Error: Numbers cannot be more than four digits."

    line1 = ""
    line2 = ""
    line3 = ""
    for problem in problems:
        terms = problem.split()

        line1 += first_line(terms)
    
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))