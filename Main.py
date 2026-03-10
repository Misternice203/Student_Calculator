print("Student Grade Calculator")
subject_count = int(input("Enter the number of subjects:"))
while subject_count <= 0:
    print("Invalid number of subjects. Please enter a positive number.")
    subject_count = int(input("Please enter a positive number between 0 and 100: "))
print(f"You have {subject_count} subjects.")
total_score = 0
print(f"Total so far: {total_score}")
for i in range(subject_count):
    score = float(input("Enter score for subject: "))
    total_score = total_score + score
    print(f"Total so far: {total_score}")
average_score = total_score / subject_count
print(f"Your average score is: {average_score:.2f}")
print(f"Total score: {total_score}")
if (total_score >= 90):
    Grade = "A"
elif (total_score >= 80):
    Grade = "B"
elif (total_score >= 70):
    Grade = "C"
elif (total_score >= 60):
    grade = "D"
else:
    print("F")
print(f"Your grade is: {Grade}")
