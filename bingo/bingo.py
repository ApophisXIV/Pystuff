from random import randint

def get_trimmed_lst_rnd(number_list,n):
    for i in range(n): #N_NUMBERS
       number_list.pop(randint(0,len(number_list)-1))
    return number_list

def random_row(max_cols):
    row = []
    index_with_number = get_trimmed_lst_rnd(list(range(max_cols)), 4)
    for columns in index_with_number:
        row.append(randint(1+10*columns,10+10*columns))
    return row

def fill_card():
    cardboard = []
    for rows in range(3): #MAX_ROW
        cardboard.append(random_row(9)) #MAX_COLUMNS
    return cardboard

print(fill_card())
