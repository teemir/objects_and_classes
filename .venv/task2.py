class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_l(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return "Ошибка"

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        Mentor.__init__(self, name, surname)
        self.finished_courses = []
        self.grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"


best_student = Student('Ruby', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_Reviewer = Reviewer('Some', 'Buddy')
cool_Reviewer.courses_attached += ['Python']

cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 10)
cool_Reviewer.rate_hw(best_student, 'Python', 10)

print(best_student.grades)


lecturer1 = Lecturer('Ann', 'Ban')
lecturer1.courses_attached += ['Python']

student1 = Student('Pit', 'Fas', 'your_gender')
student1.finished_courses += ['Python']

student1.rate_l(lecturer1, 'Python', 8)
student1.rate_l(lecturer1, 'Python', 9)
student1.rate_l(lecturer1, 'Python', 11)

print(lecturer1.grades)
# Lecture1 = Lecturer('Some', 'Buddy')
# print(Lecture1.name)
# print(Lecture1.surname)
# print(Lecture1.courses_attached)