from random import randint

def select_no_duplicates(pool,rows,n):
    selection = []
    for i in range(rows):
        row = [col.pop(randint(0, len(col)-1)) for col in pool]
        for j in range(n//rows - 1):
            row.pop(randint(0,len(row)-1))
        selection.append(row)
    return selection

def get_carboard():
    pool = list(list(range(1 + 11 * i, 12 + 11 * i)) for i in range(9))
    return select_no_duplicates(pool,3,15)

def get_cardboards(n):
    cardboards = []
    while len(cardboards) < n:
        cardboard = get_carboard()
        if cardboard not in cardboards:
            print("CARTON")
            print (cardboard)
            cardboards.append(cardboard)
    return cardboards

get_cardboards(5)
#print(get_cardboards(5))
