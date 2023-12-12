#전역변수
str = "Not Class Member"

class GString:
    def __init__(self):
        #인스턴스 멤버변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그 수정
        print(self.str)

#파이썬은 모호한 것보다 명확한 것이 좋다. 
g = GString()
g.set("First Message")
g.print()
