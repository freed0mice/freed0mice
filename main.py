class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __repr__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {get_middle_marks(self.grades)}\nКурсы в процессе изучения: {" ".join(self.courses_in_progress)}\nЗавершенные курсы: {" ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __repr__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {get_middle_marks(self.grades)}'

    def __eq__(self, other):
        return get_middle_marks(self.grades) == get_middle_marks(other.grades)

    def __ne__(self, other):
        return get_middle_marks(self.grades) != get_middle_marks(other.grades)

    def __lt__(self, other):
        return get_middle_marks(self.grades) < get_middle_marks(other.grades)

    def __le__(self, other):
        return get_middle_marks(self.grades) <= get_middle_marks(other.grades)

    def __gt__(self, other):
        return get_middle_marks(self.grades) > get_middle_marks(other.grades)

    def __ge__(self, other):
        return get_middle_marks(self.grades) >= get_middle_marks(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __repr__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def get_middle_marks(grades):
     if sum(list(map(lambda x: len(x[1]), grades.items()))) == 0:
         middle_mark = 0
     else:
         middle_mark = round(sum(list(map(lambda x: sum(x[1]), grades.items()))) / sum(
             list(map(lambda x: len(x[1]), grades.items()))), 2)
     return round(middle_mark, 2)


def get_middle_marks_students(students, course):
    student_middle_marks = []
    for student in students:
        if len(student.grades[course]) == 0:
            student_middle_marks.append(0)
        else:
            student_middle_marks.append(sum(student.grades[course]) / len(student.grades[course]))
    if len(student_middle_marks) == 0:
        return 0
    return round(sum(student_middle_marks) / len(student_middle_marks), 2)


def get_middle_marks_lectures(lectures, course):
    lecture_middle_marks = []
    for lecture in lectures:
        if len(lecture.grades[course]) == 0:
            lecture_middle_marks.append(0)
        else:
            lecture_middle_marks.append(sum(lecture.grades[course]) /
                                        len(lecture.grades[course]))
    if len(lecture_middle_marks) == 0:
        return 0
    return round(sum(lecture_middle_marks) / len(lecture_middle_marks), 2)


# -----------------------------------------------------

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

ne_student = Student('My', 'Name', 'your_gender')
ne_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_lecturer = Lecturer('John', 'Boss')
new_lecturer = Lecturer('my', 'bro')
cool_lecturer.courses_attached += ['Python']
new_lecturer.courses_attached += ['Python']

best_student.rate_hw(cool_lecturer, 'Python', 10)

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(ne_student, 'Python', 5)

