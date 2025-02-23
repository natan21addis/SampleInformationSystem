def calculate_gpa(midterm, assignment, final_exam):
    total_score = midterm + assignment + final_exam
    if total_score >= 90:
        return 4.0
    elif total_score >= 80:
        return 3.5
    elif total_score >= 70:
        return 3.0
    elif total_score >= 60:
        return 2.5
    else:
        return 2.0