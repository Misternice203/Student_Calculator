print("Student Grade Calculator")
subject_count = int(input("Enter the number of subjects:"))
print(f"You have {subject_count} subjects.")
total_score = 0
print(f"Total so far: {total_score}")
for i in range(subject_count):
    score = float(input("Enter score for subject: "))
    print(f"Total so far: {total_score}")
    total_score = total_score + score
    average_score = total_score / subject_count
print(f"Your average score is: {average_score:.2f}")
print(f"Total score: {total_score}")
grade = average_score
if grade >= 90 and grade <= 100:
    print("A")
elif grade >= 80 and grade <= 89.99:
    print("B")
elif grade >= 70 and grade <= 79.99:
    print("C")
elif grade >= 60 and grade <= 69.99:
    print("D")
else:
    print("F")
print(f"Your grade is: {grade}")
