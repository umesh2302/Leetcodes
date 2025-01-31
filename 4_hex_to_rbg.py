def hex_string_to_RGB(hex_string): 
    # your code here
    return {'r': int(hex_string[1:3], 16), 'g': int(hex_string[3:5], 16), 'b': int(hex_string[5:7], 16)}
def RGB_to_hex_string(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb['r'], rgb['g'], rgb['b'])

#test cases 
print(hex_string_to_RGB("#FF9933")) # {'r': 255, 'g': 153, 'b': 51}
print(hex_string_to_RGB("#bebebe")) # {'r': 190, 'g': 190, 'b': 190}
print(RGB_to_hex_string({'r': 255, 'g': 153, 'b': 51})) # '#ff9933'