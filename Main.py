print("Student Grade Calculator")
print("=" * 25)

while True:
    total_score = 0
    grade = ""
    subject_scores = {}
    subject_names = []

    subject_count = int(input("Enter the number of subjects: "))
    while subject_count <= 0:
        print("Invalid number of subjects. Please enter a positive number.")
        subject_count = int(input("Enter the number of subjects: "))

    print("Great! now lets enter the name of the subjects!")
    print(f"You have {subject_count} subjects.")

    for i in range(subject_count):
        subject_names.append(input(f"Enter the name of subject {i+1}: "))

    print("Now let's enter the scores for each subject.")

    for i in range(subject_count):
        score = float(input(f"Enter score for {subject_names[i]}: "))
        while score < 0 or score > 100:
            print("Invalid score. Please enter a value between 0 and 100.")
            score = float(input(f"Enter score for {subject_names[i]}: "))
        total_score += score
        subject_scores[subject_names[i]] = score

    average_score = total_score / subject_count

    if average_score >= 90:
        grade = "A"
    elif average_score >= 80:
        grade = "B"
    elif average_score >= 70:
        grade = "C"
    elif average_score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("--- Student Report ---")
    for subject, score in subject_scores.items():
        print(f"{subject}: {score}")
    print(f"Total Score: {total_score}")
    print(f"Average Score: {average_score:.2f}")
    print(f"Grade: {grade}")

    restart = input("Do you want to calculate again? (yes/no): ").strip().lower()
    while restart not in ("yes", "no"):
        restart = input("Please type 'yes' or 'no': ").strip().lower()

    if restart == "yes":
        print("Restarting the calculator!!")
    else:
        print("Thank you for using the Student Grade Calculator!")
        break
