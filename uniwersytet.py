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

    def calculate_grade(self):
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
    
    def _function_courses(self,course_id):
        grades = []
        for student in self.students:
            for enrollment in student.enrollments:
                if enrollment["course_id"] == course_id and enrollment['grade'] is not None:
                    grades.append(enrollment['grade'])
        return grades
    def average_grade_for_course(self,course_id):
        grades = self._function_courses(course_id)
        if len(grades) == 0:
            return None
        return sum(grades)/len(grades)

    def percentage_of_people_who_failed(self,course_id):
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
    def learning_effectiveness(self,student_id,course_id):
            for student in self.students:
                    if student.id == student_id:
                        for enrollment in student.enrollments:
                                if enrollment['course_id'] == course_id:
                                    if  enrollment['study_hours'] is None or enrollment['grade'] is  None or enrollment['study_hours'] == 0:
                                        return None
                                    effectiveness = enrollment['grade'] / enrollment['study_hours']
                                    return effectiveness
    
    def best_student_ranking(self,course_id):
        student_list = []
        for student in self.students:
            for enrollment in student.enrollments:
                if enrollment["course_id"] == course_id and enrollment['grade'] is not None:
                    student_list.append((student,enrollment['grade']))
        if len(student_list) == 0:
            return None
        student_list.sort(key = lambda x: x[1],reverse = True)
        return student_list
    



def main(): 
    university = University() 
    
    for dataset_student in DATASET["students"]: 
        student = Student(dataset_student["student_id"], dataset_student["age"], dataset_student["major"]) 
        university.add_student(student) 
    

    for student in university.students: 
        for dataset_enrollment in DATASET["enrollments"]: 
            if dataset_enrollment["student_id"] == student.id: 
                enrollment = dataset_enrollment.copy() 
                del enrollment["student_id"] 
                student.add_enrollment(dataset_enrollment["course_id"], dataset_enrollment["grade"], dataset_enrollment["study_hours"])
 
    print(university) 
    print(university.average_grade_for_course("CS102"))
    print(university.median_grade("CS102"))
    print(university.students[1].calculate_grade())
    ranking = university.best_student_ranking("CS102")
    for student,grade in ranking:
        print(student.id,grade)


main() 
