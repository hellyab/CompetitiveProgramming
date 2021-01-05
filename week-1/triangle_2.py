def triangle_2(lines):
    for i in range(lines+1):
        asterisks = (i * 2) + 1
        spaces = ((lines * 2) + 1 - asterisks) // 2
        print(spaces * " ", asterisks * "*", spaces * " ")

triangle_2(6)