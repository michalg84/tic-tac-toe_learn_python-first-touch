from typing import List


def ask(question):
    return str(input(question))


def askAndValidateList(question, expectedValues):
    value = ""
    while value.upper() not in list(expectedValues):
        value = ask(question)
    return value


# player = input("Insert player name: ")
# print("Player name is:", player)
#
# sign = askAndValidateList("choose your sign [O / X]", ["X", "O"])
# print("Your sign is:", sign)

def validField(field):
    if len(field.strip()) == 3:
        split: list[str] = field.split()
        if (len(split) == 2):
            if (all(element.isdigit() and 1 <= int(element) <= 3 for element in split)):
                return split


field: list = ""
while not validField(field):
    field = ask("Chose your field [row and col: 1 1 or 3 1 etc]: ")

row = -1
col = -1

# row = int(field[0])
# col = int(field[1])
