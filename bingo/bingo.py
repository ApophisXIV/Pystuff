from random import randint

def get_trimmed_lst_rnd(number_list,n):
    for i in range(n): #N_NUMBERS
       number_list.pop(randint(0,len(number_list)-1))
    return number_list

def random_row(max_cols):
    row = []
    index_with_number = get_trimmed_lst_rnd(list(range(max_cols+1)), 5)
    for columns in index_with_number:
        row.append(randint(1+10*columns,9+10*columns))
    return row

def fill_cardboard():
    cardboard = []
    for rows in range(3): #MAX_ROW
        cardboard.append(random_row(9)) #MAX_COLUMNS
    return cardboard

""" TODO: Format Cardboard
def print_cardboard(raw_cardboard, rows, cols):
    for i in range(rows):
        for j in range(cols):
            if(raw_cardboard[i][j] % j)
"""

print(fill_cardboard())
