def arithmetic_arranger(problems, result = False):

    if len(problems) > 5:
        raise "Error: Too many problems."

    for problem in problems:
        if "x" in problem or "/" in problem:
            raise "Error: Operator must be '+' or '-'."

    return arranged_problems


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))