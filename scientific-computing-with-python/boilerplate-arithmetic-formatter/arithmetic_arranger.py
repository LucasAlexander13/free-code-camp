def first_line(problem):
    max_len = len(max(problem))
    spaces = " " * (max_len - len(problem[0]) + 2)
    beetween = " " * 4
    return f"{spaces}{problem[0]}{beetween}"

def secnd_line(problem):
    max_len = len(max(problem))
    spaces = " " * (max_len - len(problem[2]) + 1)
    beetween = " " * 4
    return f"{problem[1]}{spaces}{problem[2]}{beetween}"

def third_line(problem):
    max_len = len(max(problem))
    underlines = "-" (max_len + 2)
    beetween = " " * 4
    return f"{underlines}{beetween}"

def solve_line(problem):
    if problem[1] == "+":
        result = int(problem[0]) + int(problem[2])
    elif problem[1] == "-":
        result = int(problem[0]) - int(problem[2])
    
    max_len = len(max(problem)) + 2
    result_len = len(str(result))
    spaces = " " * (max_len - result_len)
    beetween = " " * 4
    return f"{spaces}{result}{beetween}"


def arithmetic_arranger(problems, result=False):

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
    if result == True:
        line4 = ""
    for problem in problems:
        terms = problem.split()

        line1 += first_line(terms)
        line2 += secnd_line(terms)
        line3 += third_line(terms)
        if result == True:
            line4 += solve_line(terms)
    
    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))