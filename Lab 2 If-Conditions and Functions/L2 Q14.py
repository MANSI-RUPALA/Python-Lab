def grade(m):
    if m == "Absent":
        return "NA"
    m = int(m)
    if m <= 39:
        return "F"
    elif 40 <= m <= 44:
        return "P"
    elif 45 <= m <= 49:
        return "C"
    elif 50 <= m <= 54:
        return "B"
    elif 55 <= m <= 59:
        return "B+"
    elif 60 <= m <= 69:
        return "A"
    elif 70 <= m <= 79:
        return "A+"
    elif 80 <= m <= 100:
        return "O"
    else:
        return "Invalid"

def result(marks):
    for m in marks:
        if m == "Absent" or int(m) <= 39:
            return "Fail"
    return "Pass"

marks = []
for i in range(1, 4):
    m = input(f"Enter marks for subject {i} (or 'Absent'): ")
    marks.append(m)

valid = [int(m) for m in marks if m != "Absent"]
total = sum(valid)
avg = total / len(valid) if valid else 0

res = result(marks)
grades = [grade(m) for m in marks]

print("\nResults:")
for i, m in enumerate(marks, 1):
    print(f"Subject {i}: Marks = {m}, Grade = {grades[i-1]}")
    
print(f"Total: {total}")
print(f"Average: {avg:.2f}")
print(f"Result: {res}")
