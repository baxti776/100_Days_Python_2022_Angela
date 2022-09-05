student_scores = input("Input a list of student s: ").split()
max_number = 0
min_number = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if max_number < student_scores[n]:
        max_number = student_scores[n]
print(f"Max number: {max_number}")
print(f"Student scores: {student_scores}")
