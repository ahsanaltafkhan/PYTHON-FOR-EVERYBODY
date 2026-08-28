"""\nClasses\n\n"""\n\nclass Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"I am {self.name}."

student = Student("Learner")
print(student.introduce())\n