class Person:
    def __init__(self, id, name, phoneNum):
        self.id = id
        self.name = name
        self.phoneNum = phoneNum

    def printInfo(self):
        print(f"ID: {self.id}, Name: {self.name}, Phone Number: {self.phoneNum}")

class Manager(Person):
    def __init__(self, id, name, phoneNum, skill):
        super().__init__(id, name, phoneNum)
        self.skill = skill

    def printInfo(self):
        super().printInfo()
        print(f"Skill: {self.skill}")

class Employee(Person):
    def __init__(self, id, name, phoneNum, title):
        super().__init__(id, name, phoneNum)
        self.title = title

    def printInfo(self):
        super().printInfo()
        print(f"Title: {self.title}")

class Alba(Person):
    pass

# 샘플 객체 생성
person1 = Manager("M001", "John", "123-456-7890", "Management")
person2 = Manager("M002", "Jane", "987-654-3210", "Leadership")
person3 = Employee("E001", "Alice", "555-123-4567", "Developer")
person4 = Employee("E002", "Bob", "444-789-1234", "Designer")
person5 = Alba("A001", "Eva", "777-555-2222")
person6 = Alba("A002", "David", "888-111-3333")
person7 = Manager("M003", "Olivia", "666-333-9999", "Problem Solving")
person8 = Manager("M004", "Liam", "111-222-3333", "Communication")
person9 = Employee("E003", "Sophia", "222-444-6666", "Analyst")
person10 = Employee("E004", "Mason", "333-777-8888", "Engineer")

# 객체 정보 출력
person1.printInfo()
person2.printInfo()
person3.printInfo()
person4.printInfo()
person5.printInfo()
person6.printInfo()
person7.printInfo()
person8.printInfo()
person9.printInfo()
person10.printInfo()
