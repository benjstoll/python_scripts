sentence = "what is the most used character in this sentence?"

char_frequency = {}

#checks to see if character is in list, if not, add to list.
for char in sentence:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

#sort tuple in ascending order 
sorted_char_frequency = sorted(char_frequency.items(), key=lambda item:item[1])

print(sorted_char_frequency)
