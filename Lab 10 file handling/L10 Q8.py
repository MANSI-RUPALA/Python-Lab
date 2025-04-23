
a = 'Story.txt'         
b = 'NewStory.txt'

remove = ['a', 'the', 'an']

with open(a, 'r', encoding='utf-8') as file:
    content = file.read()

for word in remove:
    content = content.replace(f" {word} ", " ") 

with open(b, 'w', encoding='utf-8') as file:
    file.write(content)

print(f"✅ Words {', '.join(remove)} removed and saved to '{b}'.")
