#1)클래스 형식을 정의
class Person:
    #초기화 루틴을 실행
    def __init__(self):
        #인스턴스 멤버 변수
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))


#2)인스턴스(복사본)을 생성(Break Point)
p1 = Person() 
p2 = Person() 
#런타임시에 변수 추가
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)

