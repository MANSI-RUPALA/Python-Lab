def convert(input_string):
    words = input_string.split()
    unique_sorted_words = sorted(set(words))
    result = ' '.join(unique_sorted_words)
    return result

input_string = "apple banana orange apple mango banana"
output_string = convert(input_string)
print("Output:", output_string)
