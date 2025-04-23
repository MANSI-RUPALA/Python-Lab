import openpyxl


filename = 'sample_data.xlsx'  
wb = openpyxl.load_workbook(sample_data.xlsx)
sheet = wb.active


students_dict = {}


for row in sheet.iter_rows(min_row=2, values_only=True):
    rollno, name, mark1, mark2, mark3 = row
    total = mark1 + mark2 + mark3
    students_dict[rollno] = {
        'name': name,
        'marks': [mark1, mark2, mark3],
        'total': total
    }


for rollno, info in students_dict.items():
    print(f"Roll No: {rollno}")
    print(f"Name: {info['name']}")
    print(f"Marks: {info['marks']}")
    print(f"Total: {info['total']}")
    print('-' * 30)
