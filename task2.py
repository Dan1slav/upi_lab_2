class Student:
    def __init__(self, last_name, first_name, birth_date):
        self.last_name = last_name
        self.first_name = first_name
        self.birth_date = birth_date
        self.grades = []

    def add_grade(self, subject, exam_date, teacher):
        self.grades.append({
            'subject': subject,
            'exam_date': exam_date,
            'teacher': teacher
        })

def count_subjects(students):
    subject_count = {}
    
    for student in students:
        for grade in student.grades:
            subject = grade['subject']
            if subject in subject_count:
                subject_count[subject] += 1
            else:
                subject_count[subject] = 1
                
    return subject_count

def print_subject_count(subject_count):
    print(f"{'Предмет':<20} {'Количество студентов':<20}")
    print('-' * 40)
    for subject, count in subject_count.items():
        print(f"{subject:<20} {count:<20}")

# Пример использования
students = [
    Student("Иванов", "Иван", "2000-01-15"),
    Student("Петров", "Петр", "2001-02-20"),
    Student("Сидоров", "Сидор", "1999-03-25")
]

students[0].add_grade("Математика", "2024-01-10", "Смирнова И.А.")
students[0].add_grade("Физика", "2024-01-15", "Кузнецов А.B.")
students[1].add_grade("Математика", "2024-01-12", "Смирнова И.А.")
students[1].add_grade("Химия", "2024-01-20", "Сидорова М.В.")
students[2].add_grade("Физика", "2024-01-18", "Кузнецов А.B.")
students[2].add_grade("Химия", "2024-01-22", "Сидорова М.В.")

subject_count = count_subjects(students)
print_subject_count(subject_count)
