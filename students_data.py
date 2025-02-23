students = [
    {"name": "Alice", "subjects": ("Math", "Physics", "English"), "scores": {"Math": 85, "Physics": 78, "English": 92}},
    {"name": "Bob", "subjects": ("Math", "Biology", "English"), "scores": {"Math": 72, "Biology": 88, "English": 80}},
    {"name": "Charlie", "subjects": ("Math", "Physics", "Chemistry"), "scores": {"Math": 90, "Physics": 95, "Chemistry": 85}},
]

def display_students(students):
    for student in students:
        print(f"Student: {student['name']}")
        print("Subjects:", ", ".join(student["subjects"]))
        print()

def get_average_score(name, students):
    for student in students:
        if student['name'] == name:
            scores = student['scores'].values()
            average_score = sum(scores) / len(scores)
            return average_score
    return None

def find_top_student(students):
    top_student = None
    top_score = 0
    for student in students:
        average_score = get_average_score(student['name'], students)
        if average_score > top_score:
            top_score = average_score
            top_student = student['name']
    return top_student

def failed_students(students, passing_score=50):
    failed = []
    for student in students:
        for subject, score in student['scores'].items():
            if score < passing_score:
                failed.append(student['name'])
                break
    return failed

def unique_subjects(students):
    subjects = set()
    for student in students:
        subjects.update(student["subjects"])
    return subjects

display_students(students)
print("Average score of Alice:", get_average_score("Alice", students))
print("Top student:", find_top_student(students))
print("Students who failed:", failed_students(students, passing_score=75))
print("Unique subjects:", unique_subjects(students))
