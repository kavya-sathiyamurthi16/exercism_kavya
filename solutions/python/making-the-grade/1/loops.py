"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    return [round(score) for score in student_scores]


def count_failed_students(student_scores):
    count = 0
    for score in student_scores:
        if score <= 40:
            count += 1
    return count


def above_threshold(student_scores, threshold):
    result = []
    for score in student_scores:
        if score >= threshold:
            result.append(score)
    return result

def letter_grades(highest):
    step = (highest - 40) // 4
    return [41 + step * i for i in range(4)]


def student_ranking(student_scores, student_names):
    ranking = []
    for index, (name, score) in enumerate(zip(student_names, student_scores), start=1):
        ranking.append(f"{index}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []