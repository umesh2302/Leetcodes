def descending_order(num):
    # Bust a move right here
    num_str = str(num)
    numbers = []
    for nu in num_str : 
        numbers.append(int(nu))
    numbers.sort(reverse = True)
    new_num = ""
    for nu in numbers : 
        new_num += str(nu)
        
    return int(new_num)
        
print(descending_order(123456789))