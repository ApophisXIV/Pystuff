from random import randint

def select_rand_cols(number_list,n):
    avaliable_index = [i for i in range(len(number_list)) if len(number_list[i]) > 0]
    for i in range(n - 1):
       avaliable_index.pop(randint(0,len(avaliable_index)-1))
    return avaliable_index

def get_cardboard(pool):
    cardboard = []
    for rows in range(3):
        row = []
       
        selected_cols = select_rand_cols(pool, 5)
        for col in selected_cols:
            choice = randint(0,len(pool[col]) - 1)
            row.append(pool[col].pop(choice))

        cardboard.append(row)
    return cardboard

def get_cardboards(n):
    avaliable_numbers = []
    for col in range(9):
        avaliable_numbers.append(list(range(1 + 11 * col, 12 + 11 * col)))
 
    cardboards = []
    for i in range(n):
        cardboards.append(get_cardboard(avaliable_numbers))
    return cardboards

print(get_cardboards(5))
