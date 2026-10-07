def avg_grade(grades):
    total_marks = 0
    for i in grades:
        total_marks += grades[i]

    return total_marks/len(grades)

mark_dict = {
    "English": 95,
    "Physics": 92,
    "Maths": 89
}
print("Average Grade: ", avg_grade(mark_dict))