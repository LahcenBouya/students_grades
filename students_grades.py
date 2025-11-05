student_score={"lahcen":90,"rida":85,"mohamed":100,"khalid":75,"jalil":65}
students_grades={}
for student in student_score:
    score=student_score[student]
    if score>90:
        students_grades[student]="very good"
    elif score>80:
        students_grades[student]="good"
    elif score >70:
        students_grades[student]="acceptable"
    else:
        students_grades[student]="fail"
print(students_grades)
