DATASET = {
    "meta": {
        "dataset_id": "university_courses_v1",
        "institution": "Example University",
        "semester": "summer_2025",
        "notes": [
            "Oceny są w skali 2.0–5.0, mogą być None (brak zaliczenia).",
            "Nie każdy student zapisał się na każdy kurs.",
            "Występują błędy danych: brakujące ID, duplikaty zapisów, punkty ECTS spoza zakresu.",
            "Czas nauki podany w godzinach (float)."
        ]
    },

    # Lista kursów oferowanych w semestrze
    "courses": [
        {"course_id": "CS101", "name": "Podstawy programowania", "ects": 6},
        {"course_id": "CS102", "name": "Algorytmy i struktury danych", "ects": 7},
        {"course_id": "CS103", "name": "Bazy danych", "ects": 5},
        {"course_id": "CS104", "name": "Inżynieria oprogramowania", "ects": 6},
        {"course_id": "CS105", "name": "Statystyka", "ects": 4},
        {"course_id": "CS999", "name": "Kurs testowy", "ects": 0},
    ],

    # Studenci – brak wieku lub kierunku jest dopuszczalny
    "students": [
        {"student_id": "S001", "age": 21, "major": "Informatyka"},
        {"student_id": "S002", "age": 22, "major": "Informatyka"},
        {"student_id": "S003", "age": 24, "major": "Informatyka i ekonometria"},
        {"student_id": "S004", "age": None, "major": "Informatyka"},
        {"student_id": "S005", "age": 20, "major": "Analiza danych"},
        {"student_id": "S006", "age": 23, "major": None},
        {"student_id": "S007", "age": 25, "major": "Informatyka"},
        {"student_id": "S008", "age": 22, "major": "Analiza danych"},
        {"student_id": "S009", "age": 21, "major": "Informatyka"},
        {"student_id": "S010", "age": 27, "major": "Informatyka"},
    ],

    "enrollments": [
        {
            "enrollment_id": 3001,
            "student_id": "S001",
            "course_id": "CS101",
            "grade": 4.5,
            "study_hours": 42.0
        },
        {
            "enrollment_id": 3002,
            "student_id": "S001",
            "course_id": "CS102",
            "grade": 4.0,
            "study_hours": 55.5
        },
        {
            "enrollment_id": 3003,
            "student_id": "S002",
            "course_id": "CS101",
            "grade": 3.5,
            "study_hours": 38.0
        },
        {
            "enrollment_id": 3004,
            "student_id": "S002",
            "course_id": "CS103",
            "grade": None,
            "study_hours": 20.0
        },
        {
            "enrollment_id": 3005,
            "student_id": "S003",
            "course_id": "CS104",
            "grade": 5.0,
            "study_hours": 60.0
        },
        {
            "enrollment_id": 3006,
            "student_id": "S003",
            "course_id": "CS105",
            "grade": 4.0,
            "study_hours": 35.0
        },
        {
            "enrollment_id": 3007,
            "student_id": "S004",
            "course_id": "CS101",
            "grade": 2.0,
            "study_hours": 15.0
        },
        {
            "enrollment_id": 3008,
            "student_id": "S005",
            "course_id": "CS103",
            "grade": 4.5,
            "study_hours": 48.0
        },
        {
            "enrollment_id": 3009,
            "student_id": "S005",
            "course_id": "CS103",
            "grade": 4.5,
            "study_hours": 48.0
        },
        {
            "enrollment_id": 3010,
            "student_id": "S006",
            "course_id": "CS999",
            "grade": 3.0,
            "study_hours": 5.0
        },
        {
            "enrollment_id": 3011,
            "student_id": "S007",
            "course_id": "CS102",
            "grade": 5.0,
            "study_hours": 70.0
        },
        {
            "enrollment_id": 3012,
            "student_id": "S008",
            "course_id": "CS105",
            "grade": 3.0,
            "study_hours": 25.0
        },
        {
            "enrollment_id": 3013,
            "student_id": "S009",
            "course_id": "CS104",
            "grade": 4.0,
            "study_hours": 50.0
        },
        {
            "enrollment_id": 3014,
            "student_id": "S010",
            "course_id": "CS102",
            "grade": 2.0,
            "study_hours": 18.0
        },
        {
            "enrollment_id": 3015,
            "student_id": None,
            "course_id": "CS101",
            "grade": 3.5,
            "study_hours": 30.0
        },
        {
            "enrollment_id": 3016,
            "student_id": "S001",
            "course_id": "CS404",
            "grade": 4.0,
            "study_hours": 40.0
        },
        {
            "enrollment_id": 3017,
            "student_id": "S008",
            "course_id": "CS101",
            "grade": 5.0,
            "study_hours": 65.0
        },
        {
            "enrollment_id": 3018,
            "student_id": "S004",
            "course_id": "CS105",
            "grade": 2.0,
            "study_hours": 12.0
        },
        {
            "enrollment_id": 3019,
            "student_id": "S002",
            "course_id": "CS104",
            "grade": 3.0,
            "study_hours": None
        },
        {
            "enrollment_id": 3020,
            "student_id": "S010",
            "course_id": "CS103",
            "grade": 4.5,
            "study_hours": 52.0
        },
    ]
}

import statistics
import copy

class Student:
    def __init__(self, id, age, major):
        self.id = id
        self.age = age
        self.major = major
        self.enrollments = []

    def __str__(self):
        return f"id: {self.id}, age: {self.age}, major: {self.major}, enrollments: {self.enrollments}"

    def add_enrollment(self, course_id, grade, study_hours):
        enrollment = {"course_id": course_id, "grade": grade, "study_hours": study_hours}
        self.enrollments.append(enrollment)

    def calculate_average(self):
        grade_sum = 0
        grade_counter = 0

        for enrollment in self.enrollments:
            grade = enrollment["grade"]

            if grade is not None:
                grade_counter += 1
                grade_sum += enrollment["grade"]

        if grade_counter == 0:
                return None

        return grade_sum / grade_counter


class University:
    def __init__(self):
        self.students = []

    def __str__(self):
        students_string = ""
        for student in self.students:
            students_string += f"{student}\n"
        return students_string

    def add_student(self, student):
        self.students.append(student)

    def _function_courses(self, course_id):
        grades = []
        for student in self.students:
            for enrollment in student.enrollments:
                if enrollment["course_id"] == course_id and enrollment['grade'] is not None:
                    grades.append(enrollment['grade'])
        return grades

    def average_grade_for_course(self, course_id):
        grades = self._function_courses(course_id)
        if len(grades) == 0:
            return None
        return sum(grades)/len(grades)

    def percentage_of_people_who_failed(self, course_id):
        grades = self._function_courses(course_id)
        counter = 0
        for grade in grades :
            if grade <= 2 :
                counter += 1
        if len(grades) == 0:
            return None
        percent = counter / len(grades) * 100
        return percent

    def median_grade(self, course_id: str) -> float | None:
        grades = self._function_courses(course_id)

        if len(grades) == 0:
            return None
        mediana = statistics.median(grades)
        return mediana


    def effectivness_in_course(self,course_id):
        students_learning_hours = 0
        students_grades = []
        for student in self.students:
            for enrollment in student.enrollments:
                if enrollment['course_id'] == course_id:
                    if  enrollment['study_hours'] is not None and enrollment['grade'] is not None and enrollment['study_hours'] != 0:
                        students_learning_hours += enrollment['study_hours']
                        students_grades.append(enrollment['grade'])
        if len(students_grades) == 0:
            return None
        if students_learning_hours == 0:
            return None
        students_average_grades = sum(students_grades)/len(students_grades)
        return students_average_grades/students_learning_hours

    def find_students_in_course(self, course_id):
        students_in_course = []

        for student in self.students:
            for enrollment in student.enrollments:
                if enrollment["course_id"] == course_id and enrollment['grade'] is not None:
                    students_in_course.append(student)
                    break

        # zmieniamy atrybut enrollments studentów tak, żeby zostały tylko enrollmentsy z danego kursu
        students_in_course_copy = copy.deepcopy(students_in_course)
        for student in students_in_course_copy:
            enrollments_copy = []
            for e in student.enrollments:
                if e["course_id"] == course_id:
                    enrollments_copy.append(e)
            student.enrollments = enrollments_copy
        return students_in_course_copy

    def find_students_in_major(self, major):
        students_in_major = []

        for student in self.students:
            if student.major == major:
                students_in_major.append(student)

        return students_in_major

    def create_ranking(self, input_students):
        students = input_students.copy()
        students_sorted = []

        while students:
            best = students[0]
            for student in students:
                if best.calculate_average() is None:
                    best = student
                elif student.calculate_average() is None:
                    continue
                elif student.calculate_average() > best.calculate_average():
                    best = student

            students_sorted.append(best)
            students.remove(best)

        return students_sorted


    def find_best_students(self):
        students_ranked = self.create_ranking(self.students)
        best_student = students_ranked[0]
        best_students = [best_student]

        for student in students_ranked[1:]:
            if student.calculate_average() == best_student.calculate_average():
                best_students.append(student)
            if student.calculate_average() < best_student.calculate_average():
                break

        return best_students

    def _remove_duplicates(self):
        for student in self.students:
            seen_courses = []
            without_duplicates = []
            for enrollment in student.enrollments:
                if enrollment['course_id'] not in seen_courses:
                    without_duplicates.append(enrollment)
                    seen_courses.append(enrollment['course_id'])
            student.enrollments = without_duplicates


    def average_study_hours_in_course(self, course_id):
        study_hours = 0

        for student in self.students:
            for enrollment in student.enrollments:
                if enrollment["course_id"] == course_id and enrollment["study_hours"] is not None and enrollment["grade"] is not None:
                    study_hours += enrollment["study_hours"]

        if len(self.find_students_in_course(course_id)) == 0:
            return None

        return study_hours / len(self.find_students_in_course(course_id))

    def average_study_hours_in_major(self, major):
        study_hours = 0

        for student in self.students:
            for enrollment in student.enrollments:
                if student.major == major and enrollment["study_hours"] is not None and enrollment["grade"] is not None:
                    study_hours += enrollment["study_hours"]

        if len(self.find_students_in_major(major)) == 0:
            return None

        return study_hours / len(self.find_students_in_major(major))

    def average_age_in_major(self, major):
        age_list = []
        for student in self.students:
            if student.major == major and student.age is not None:
                age_list.append(student.age)
        if student.age is None:
            return None
        return sum(age_list) / len(age_list)


def main():
    university = University()

    courses_list = []
    for course in DATASET["courses"]:
        if course['ects'] != 0:
            courses_list.append(course['course_id'])


    for dataset_student in DATASET["students"]:
        student = Student(dataset_student["student_id"], dataset_student["age"], dataset_student["major"])
        university.add_student(student)

    for student in university.students:
        for dataset_enrollment in DATASET["enrollments"]:
            if dataset_enrollment["student_id"] == student.id and dataset_enrollment["course_id"] in courses_list:
                student.add_enrollment(dataset_enrollment["course_id"], dataset_enrollment["grade"], dataset_enrollment["study_hours"])

    university._remove_duplicates()

    print("-- Najlepszy student --\n")
    best_students = university.find_best_students()
    for best_student in best_students:
        print(f"id: {best_student.id}, śrenia ocen: {best_student.calculate_average()}")
    print()
    print("---------------------------------------------------------\n")

    print("-- Analiza poszczególnych kursów --\n")
    for course in DATASET["courses"]:
        if course["ects"] > 0:
            print(f"- {course["name"]} -\n")
            print("Ranking studentów:")
            best_students_in_course = university.create_ranking(university.find_students_in_course(course["course_id"]))
            index = 1
            for student in best_students_in_course:
                print(f"{index}. id: {student.id}, ocena: {round(student.calculate_average(), 2)}")
                index += 1
            print()
            print(f"Średnia ocen: {round(university.average_grade_for_course(course['course_id']), 2)}\n")
            print(f"Mediana ocen: {university.median_grade(course['course_id'])}\n")
            print(f"Średni czas nauki: {round(university.average_study_hours_in_course(course['course_id']), 2)} h\n")
            print(f"Śreni czas nauki / ects: {round(university.average_study_hours_in_course(course["course_id"]) / course["ects"], 2)} h / 1 ects\n")
            print(f"Procent studentów którzy nie zdali: {round(university.percentage_of_people_who_failed(course['course_id']))}%\n")
            # print(f"Wskaźnik efektywności dla kursu {course['name']} wynosi {university.effectivness_in_course(course['course_id'])}")
            print("---------------------------------------------------------\n")


    print("-- Analiza dla poszczególnych kierunków --\n")
    majors = {student["major"] for student in DATASET["students"] if student["major"] != None}
    for major in majors:
        print(f"- {major} -\n")
        print("Ranking studentów:")
        best_students_in_major = university.create_ranking(university.find_students_in_major(major))
        index = 1
        for student in best_students_in_major:
            print(f"{index}. id: {student.id}, średnia ocen: {round(student.calculate_average(), 2)}")
            index += 1
        print()
        print(f"Średni czas nauki: {round(university.average_study_hours_in_major(major), 2)} h\n")
        print(f"Średni wiek: {round(university.average_age_in_major(major))}")
        print("---------------------------------------------------------\n")

main()