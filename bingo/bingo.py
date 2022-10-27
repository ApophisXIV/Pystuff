from random import randint

def select_rnd_index(number_list, n):
    for i in range(n):  # N_NUMBERS
        number_list.pop(randint(0, len(number_list)-1))
    return number_list

def get_carboard():
    carboard = []
    for i in range(3):
        row = []
        selected_index = select_rnd_index(list(range(10)), 5)
        for col in selected_index:
            row.append(randint(1+10*col, 9+10*col))
        carboard.append(row)
    return carboard

def get_cardboards(n):
    cardboards = []
    while len(cardboards) < n:
        cardboad = get_carboard()
        if cardboad not in cardboards:
            cardboards.append(cardboad)
    return cardboards

print(get_cardboards(5))