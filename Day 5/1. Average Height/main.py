student_heights = input("Enter the students' heights").split()
sum_of_student_heights = 0
number_of_students = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_of_student_heights += student_heights[n]
    number_of_students += 1

average_height_of_students = round(sum_of_student_heights / number_of_students)
print(f"All students heights: {student_heights}")
print(f"Sum of students heights: {sum_of_student_heights}")
print(f"Number of students: {number_of_students}")
print(f"Average height of students: {average_height_of_students}")
