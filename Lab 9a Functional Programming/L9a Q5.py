faculty_list = ['Arpana Jha', 'Bhavani Kumar', 'Chandni', 'Devi', 'Elizabeh', 'Johnathon']
filtered_list = filter(lambda name: len(name) > 8, faculty_list)

print(list(filtered_list))
