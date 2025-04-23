import csv


filename = 'sample_data.csv'


header = ['Name', 'Age', 'City']
rows = [
    ['Anjali', 30, 'Ahmedabad'],
    ['Baani', 25, 'Baroda'],
    ['Chandni', 35, 'Chandigarh'],
    ['Deepti', 28, 'Delhi']]

with open(filename, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(header)  
    writer.writerows(rows)   

print(f"CSV file '{filename}' created successfully!")
