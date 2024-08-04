# 숙제 - 93
# 전부 다 주석 다세요

students = [                                        #students 이름의 딕셔너리 선언
    {'name': 'won', 'age': 4444, 'grade': 'A'},     #student의 속성1
    {'name': 'babo', 'age': 444, 'grade': 'B'},     #student의 속성2
    {'name': 'baboo', 'age': 44, 'grade': 'C'},     #student의 속성3
    {'name': 'baboo', 'age': 44, 'grade': 'C'},     #student의 속성4
]

def get_student_grade(student):                     #학생의 성적을 가져오는 함수 선언
    return student['grade']                         #student의 키값 grade을 호출하여 성적을 가져온다.

    print(get_student_grade(students[0]))           #A
    print(get_student_grade(students[0]))           #A


class Student:                          #본격 클래스 만들기 (객체의 속성과 행동을 추상화하는 것)
    """                                 # 이때 __doc__를 쓰게 되면
    Student Class
    Date: 2044.04.44
    44444444444444444
    하기 싫어
    """
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'called __str__ >>> {self.name}, {self.age}'

    def __repr__(self):
        return f'called __repr__ >>> {self.name}, {self.age}'

    # instance method
    def get_grade(self):
        print(f'called get_grade >>> {id(self)}')
        return f'grade >>> {self.grade}'

student_1 = Student('won', 4444, 'A')
student_2 = Student('babo', 444, 'B')
student_3 = Student('baboo', 44, 'C')

# id        #student_1~3의 id가 모두 다름. 즉 객체는 id를 모두 부여받으며,객체 구별을 위한 일련번호임.
print(id(student_1))            #2838249012720
print(id(student_2))            #2838249012624
print(id(student_3))            #2838249012528

#dir()은 네임 스페이스에 등록되어 있는 모든 이름들을 리스트로 반환해주는 파이썬의 내장함수
print(f'dir func >>> {dir(student_1)}')  #student_1의 메소드를 모두 보여줌. #'age', 'get_grade', 'grade', 'name' 이 존재함
print(f'dir func >>> {dir(student_2)}')  #위 내용과 동일함
print('-' * 50)
print()

#__dict__는 student객체의 속성값을 딕셔너리형으로 보여주는 것
print(f'__dict__ >>> {student_1.__dict__}') #__dict__ >>> {'name': 'won', 'age': 4444, 'grade': 'A'}
print('-' * 50)
print()

#str 메소드는
print(student_1)                #called __str__ >>> won, 4444
print('-' * 50)
print()

# docstring
print(student_1.__doc__)
print(student_2.__doc__)

# docstring 사용하여야 오픈소스 개발잘엉나ㅣ러나ㅣㅇ러닌언아ㅣ
a_list = []
print(type(a_list))
print(dir(a_list))
print(a_list.__doc__)
print(a_list.append.__doc__)
print(a_list.remove.__doc__)
print('-' * 50)
print()

# self
print(f'method call _1 >>> {student_1.get_grade()}')
print(f'student_1 ID >>> {id(student_1)}')
print()
print(f'method call _2 >>> {student_2.get_grade()}')
print(f'student_2 ID >>> {id(student_2)}')
print('-' * 50)
print()

# __class__
print(student_1.__class__)
print(student_2.__class__)
print(f'id >>> {id(student_1.__class__)}, {id(student_2.__class__)}')
print(f'Class ID - Student >>> {id(Student)}')
print('-' * 50)
print()


class Student:
    """
    Student Class
    Date: 2044.04.44
    44444444444444444
    하기 싫어
    """
    # Class var
    student_total_count = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self._grade = grade
        self.__grade = grade
        Student.student_total_count += 1

    def __str__(self):
        return f'called __str__ >>> {self.name}, {self.age}'

    def __repr__(self):
        return f'called __repr__ >>> {self.name}, {self.age}'

    # instance method
    def get_grade(self):
        print(f'called get_grade >>> {id(self)}')
        return f'grade >>> {self.grade}'

student_1 = Student('won', 4444, 'A')
student_2 = Student('babo', 444, 'B')
student_2 = Student('baboo', 44, 'C')
student_2 = Student('baboo', 44, 'C')
student_2 = Student('ba', 44, 'C')
student_2 = Student('bo', 44, 'C')
student_2 = Student('babooo', 44, 'C')
student_2 = Student('baboooo', 44, 'C')
student_2 = Student('baboooooo', 44, 'C')

print(f'Class var-count student_1 >>> {student_1.student_total_count}')
print(f'Class var-count student_2 >>> {student_2.student_total_count}')
print()
print(f'instance var student_1 {student_1.name}')
print(f'instance var student_2 {student_2.name}')
print(student_2.name)