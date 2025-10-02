class Student:
    names = []
    ages = []
    ids = []
    grades = []

    def __init__(self, name, age, grade, id=None):
        # validate name
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        self.name = name
        Student.names.append(name)

        # validate age
        if not isinstance(age, int):
            raise TypeError("Age must be integer")
        if age <= 0:
            raise ValueError("Age must be positive")
        self.__age = age
        Student.ages.append(age)

        # validate grade
        if not isinstance(grade, int):
            raise TypeError("Grade must be integer")
        if not (0 <= grade <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self.__grade = grade
        Student.grades.append(grade)

        # optional ID
        self.__id = None
        if id is not None:
            self.id_ver = id  # use property setter for validation

    @property
    def id_ver(self):
        return self.__id

    @id_ver.setter
    def id_ver(self, id):
        if not isinstance(id, int):
            raise TypeError("ID must be integer")
        if id in Student.ids:
            raise ValueError("ID already exists")
        self.__id = id
        Student.ids.append(id)

    def show_stats(self):
        return f"Student(name={self.name}, age={self.__age}, grade={self.__grade}, id={self.__id})"
