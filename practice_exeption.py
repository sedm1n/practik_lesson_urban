from random import randint
def generate_calc_txt():
    operands = "+ - / * // %".split()
    arr = []
    for i in range(100):
        arr.append(f"{randint(1,159)} {operands[randint(0,5)]} {randint(1,421)}")

    with open('calc.txt', 'w') as file:
         for line in arr:
            file.write(line+"n")

def calc(lins):

    value = 0
    openrand1, operation, operand2 = line.split()
    match operation:
        case '-':
            value = int(openrand1)-int(operand2)
        case '+':
            value = int(openrand1)+int(operand2)
        case '*':
            value = int(openrand1)*int(operand2)
        case '/':
            value = int(openrand1)/int(operand2)
        case '//':
            value = int(openrand1)//int(operand2)
        case '%':
            value = int(openrand1)-int(operand2)

    return value

total = 0
generate_calc_txt()

with open('calc.txt', 'r') as file:

    for line in file:
        try:
            total += calc(line)
        except ValueError as exc:
            if 'unpack' == exc.args[0]:
                print("Errors ", line)
            else:
                print("Errors", exc.args)








