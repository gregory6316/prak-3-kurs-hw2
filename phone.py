from itertools import product

def phone_comb(num) :
    dictionary = {'0' : (' '), '1' : ('_'), '2' : ('a', 'b', 'c'), '3' : ('d', 'e', 'f'), '4' : ('g', 'h', 'i'), '5' : ('j', 'k', 'l'), '6' : ('m', 'n', 'o'), '7' : ('p', 'q', 'r', 's'), '8' : ('t', 'u', 'v'), '9' : ('w', 'x', 'y', 'z')}
    arrays = []
    for i in num :
        arrays.append(dictionary[i])
    temp = list(product(*arrays))
    result = []
    for i in temp :
        result.append(''.join(i))
    print(result)

user_input = input()
phone_comb(user_input)
