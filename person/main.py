class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print("person name: %s" % self.name, " age: %d" % self.age)


class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def print(self):
        print("student name: %s" % self.name, "age: %d " % self.age, "grade: %d" % self.grade)


if __name__ == '__main__':
    p = Person("jack", 12)
    p.print()
    s = Student("Bob", 12, 9)
    s.print()

