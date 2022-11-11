from random import randint


def select_no_duplicates(pool, rows, n):
    selection = []
    for i in range(rows):
        row = [col.pop(randint(0, len(col)-1)) for col in pool]
        for j in range(n//rows - 1):
            index = randint(0, len(row)-1)
            while row[index] == "X":
                index = randint(0, len(row)-1)
            row[index] = "X"
        selection.append(row)
    return selection


def get_carboard():
    pool = list(list(range(1 + 11 * i, 12 + 11 * i)) for i in range(9))
    return select_no_duplicates(pool, 3, 15)


def get_cardboards(n):
    cardboards = []
    while len(cardboards) < n:
        cardboard = get_carboard()
        if cardboard not in cardboards:
            print("CARTON")
            print(cardboard)
            cardboards.append(cardboard)
    return cardboards


def lines_win(cardboard):
    lines = []
    for row in cardboard:
        if row.count("*") == 5:
            lines.append(True)
        else:
            lines.append(False)
    return lines


# Cardboard example with 1 line
cardboard = [['X', '*', '*', 'X', '*', 'X', '*', '*', 'X'],
             ['X', 12, 'X', 41, 48, 59, 'X', 85, 'X'],
             [5, 16, 32, 40, 'X', 'X', 'X', 86, 'X']]


# get_cardboards(5)
print(get_score_per_row(get_carboard()))
# print(get_cardboards(5))
