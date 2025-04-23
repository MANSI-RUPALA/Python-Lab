def frequency(input_string):
    words = input_string.split()
    freq_dict = {}
    for word in words:
        word = word.lower() 
        freq_dict[word] = freq_dict.get(word, 0) + 1
    sorted_freq = sorted(freq_dict.items())
    return sorted_freq

input_string = "This is a test. This test is only a test."
input_string = ''.join(char for char in input_string if char.isalnum() or char.isspace())
result = frequency(input_string)
print("Word Frequencies:", result)