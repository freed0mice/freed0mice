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

    def __repr__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __repr__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {get_middle_marks(self.grades)}'

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

first_student = Student('Vadim', 'Legend', 'male')
first_student.courses_in_progress += ['Python']

second_student = Student('Alina', 'Legend', 'female')
second_student.courses_in_progress += ['Python']

first_mentor = Mentor('Dima', 'Popov')
first_mentor.courses_attached += ['Python']

second_mentor = Mentor('Sveta', 'Panova')
second_mentor.courses_attached += ['Python']

first_lecturer = Lecturer('Sonya', 'Shaman')
first_lecturer.courses_attached += ['Python']

second_lecturer = Lecturer('Yulia', 'Gagarina')
second_lecturer.courses_attached += ['Python']

first_reviewer = Reviewer('Dina', 'Faripova')

second_reviewer = Reviewer('Lisa', 'Falina')

first_student.rate_hw(first_lecturer, 'Python', 10)
second_student.rate_hw(second_lecturer, 'Python', 10)

first_mentor.rate_hw(first_student, 'Python', 10)
second_mentor.rate_hw(second_student, 'Python', 10)

first_lecturer.rate_hw(first_student, 'Python', 10)
second_lecturer.rate_hw(second_student, 'Python', 10)

print(first_student)
print()
print(second_student)
print()
print(first_mentor)
print()
print(second_mentor)
print()
print(first_lecturer)
print()
print(second_lecturer)
print()
print(first_reviewer)
print()
print(second_reviewer)
print()
print('Для студентов:', get_middle_marks_students([first_student, second_student], 'Python'))
print('Для лекторов:', get_middle_marks_lectures([first_lecturer, second_lecturer], 'Python'))
print()
print(first_lecture == second_lecture)
print(first_lecture != second_lecture)
print(first_lecture < second_lecture)
print(first_lecture <= second_lecture)
print(first_lecture > second_lecture)
print(first_lecture >= second_lecture)