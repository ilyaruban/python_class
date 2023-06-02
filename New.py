class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.dict = {}                 # данный словарь необходим для хранения средней оценки курсов
        self.course_question_list = [] # данный список необходим для сохранения выбранного курса

    def course_question_list_1(self):  # в данной функции сохраняется выбранный курс студента, и считается средняя оценка для всех курсов
        course_question = input('Введите курс студента, который вас интересует (Python, Git): ')
        self.course_question_list.append(course_question)
        for n in self.grades.keys():
            self.dict[n] = sum(self.grades[n]) / (len(self.grades[n]))

    def __str__(self):
        if 'Python' in self.course_question_list or 'Git' in self.course_question_list:
            print()
            return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания по курсу {self.course_question_list[0]}: {self.dict[self.course_question_list[0]]} \nКурсы в процессе изучения: {", ".join(self.courses_in_progress)} \nЗавершенные курсы: Введение в программирование'
        else:
            return f'Данный студент, {self.name} {self.surname}, не обучается на курсе {self.course_question_list[0]}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.lection_grade = {}
        self.dict = {}                  # данный словарь необходим для хранения средней оценки курсов
        self.course_question_list = []  # данный список необходим для сохранения выбранного курса


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Должность: проверяющий \nИмя: {self.name} \nФамилия: {self.surname}'


class Lecturer(Mentor):
    def lection_rate(self, student, course, grade): # в данной функции ставится оценка преподавателю и вычисляется средняя
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in self.lection_grade:
                self.lection_grade[course] += [grade]
            else:
                self.lection_grade[course] = [grade]
        else:
            return 'Ошибка'
        for n in self.lection_grade.keys():
            self.dict[n] = sum(self.lection_grade[n]) / (len(self.lection_grade[n]))

    def course_question_list_1(self):
        course_question = input('Введите курс лектора, который вас интересует (Python, Git): ')
        self.course_question_list.append(course_question)

    def __str__(self):
        if 'Python' in self.course_question_list or 'Git' in self.course_question_list:
            print()
            return f'Должность: Лектор курса {self.course_question_list[0]} \nИмя: {self.name}\nФамилия: {self.surname}\nСредняя оценка: {self.dict[self.course_question_list[0]]}'
        else:
            return f'Данный лектор, {self.name} {self.surname}, не преподает на курсе {self.course_question_list[0]}'


some_student = Student('Ruoy', 'Eman', 'gender')
some_student_1 = Student('Name', 'Eman', 'gender_1')
some_student.courses_in_progress += ['Git']
some_student.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Python']
some_student_1.courses_in_progress += ['Git']

some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer_1 = Reviewer('Some_1', 'Buddy_1')
some_reviewer_1.courses_attached += ['Python']
some_reviewer.courses_attached += ['Python']
some_reviewer.courses_attached += ['Git']
some_reviewer_1.courses_attached += ['Git']

some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Python', 10)
some_reviewer.rate_hw(some_student, 'Git', 8)
some_reviewer.rate_hw(some_student, 'Git', 5)
some_reviewer_1.rate_hw(some_student_1, 'Python', 5)
some_reviewer_1.rate_hw(some_student_1, 'Git', 6)
some_reviewer_1.rate_hw(some_student_1, 'Git', 5)
some_reviewer_1.rate_hw(some_student_1, 'Git', 5)

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer_1 = Lecturer('Some_1', 'Buddy_1')
some_lecturer_1.courses_attached += ['Python']
some_lecturer_1.courses_attached += ['Git']
some_lecturer.courses_attached += ['Python']
some_lecturer.courses_attached += ['Git']

some_lecturer.lection_rate(some_student, 'Python', 10)
some_lecturer.lection_rate(some_student, 'Python', 8)
some_lecturer.lection_rate(some_student, 'Git', 4)
some_lecturer.lection_rate(some_student, 'Git', 8)
some_lecturer_1.lection_rate(some_student_1, 'Python', 6)
some_lecturer_1.lection_rate(some_student_1, 'Python', 8)
some_lecturer_1.lection_rate(some_student_1, 'Git', 10)
some_lecturer_1.lection_rate(some_student_1, 'Git', 3)

print(some_reviewer)
print()
print(some_reviewer_1)
print()
some_lecturer.course_question_list_1()
print()
some_lecturer_1.course_question_list_1()
print()


# функция для сравнения двух лекторов по средней оценке
def compare_lectures(list_1, list_2):
    if list_1.course_question_list == list_2.course_question_list:
        if list_1.dict[list_1.course_question_list[0]] > list_2.dict[list_2.course_question_list[0]]:
            return list_1
        else:
            return list_2
    else:
        return 'Сравнение производится в рамках одного курса, пожалуйста, введите одинаковые курсы лекторов'


question = input('Сравнить лекторов по наибольшей средней оценке за лекции?: ')
if question.lower() == 'нет':
    print()
    print(some_lecturer)
    print()
    print(some_lecturer_1)
elif question.lower() == 'да':
    print()
    print(compare_lectures(some_lecturer, some_lecturer_1))

print()
some_student.course_question_list_1()
print()
some_student_1.course_question_list_1()
print()


# функция для сравнения двух студентов по средней оценке
def compare_students(list_1, list_2):
    if list_1.course_question_list == list_2.course_question_list:
        if list_1.dict[list_1.course_question_list[0]] > list_2.dict[list_2.course_question_list[0]]:
            return list_1
        else:
            return list_2
    else:
        return 'Сравнение производится в рамках одного курса, пожалуйста, введите одинаковые курсы студентов'


question = input('Сравнить студентов по наибольшей средней оценке за домашние задания?: ')
if question.lower() == 'нет':
    print()
    print(some_student)
    print()
    print(some_student_1)
elif question.lower() == 'да':
    print()
    print(compare_students(some_student, some_student_1))