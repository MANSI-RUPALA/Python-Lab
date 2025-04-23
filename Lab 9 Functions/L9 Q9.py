def count_alpha_digits(input_string):
    result = {'alphabets': 0, 'digits': 0}
    for char in input_string:
        if char.isalpha():
            result['alphabets'] += 1
        elif char.isdigit():
            result['digits'] += 1
    return result
input_string = "Hello123"
print(count_alpha_digits(input_string))