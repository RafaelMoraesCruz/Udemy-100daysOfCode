student_scores = {
    "Harry": 81,
    "Ron" : 78,
    "Hermionee" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

stundent_grades = {}

for k, v in student_scores.items():
    if(91 <= v <= 100):
        stundent_grades[k] = "Outstanding"
    if (81 <= v <= 90):
        stundent_grades[k] = "Exceeds Expectations"
    if (71 <= v <= 80):
        stundent_grades[k] = "Acceptable"
    if (70 >= v):
        stundent_grades[k] = "fail"
print(stundent_grades)