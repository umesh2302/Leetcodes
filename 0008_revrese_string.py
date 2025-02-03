import re

def reverse_words(text):
    words = re.split(r'(\s+)', text)
    reverse_word = []
    for word in words:
        reverse_word.append(word[::-1])
    return ''.join(reverse_word)
        

print(reverse_words("This is an example!")) # "sihT si na !elpmaxe"
print(reverse_words(" double  spaces ")) # " elbuod  secaps "