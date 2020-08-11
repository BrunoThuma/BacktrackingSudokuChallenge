# Objetivo: Aprender sobre backtracking usando
# conceitos já aprendidos em ProLog

# Takes 2 parameters: a list and the number of 
# in terms in each groupset
def permute(list, s):
    if list == 1:
        return s

    # If not the last iteration will recurse 
    # returning a list with the concat of
    # the list itself plus s-1 itens concated 
    # by the same process
    else:
        return [ y + x
                    for y in permute(1, s)
                    for x in permute(list - 1, s)
                    ]

print(permute(2, ["a","b","c"]))