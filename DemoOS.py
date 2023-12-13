import random
from os.path import * 
from os import * 

print(random.random())
print(random.random())
#리스트 내장(리스트 컴프리헨션)
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print([random.randrange(20) for i in range(10)])
print("---sample---")
print(random.sample(range(20), 10))
print(random.sample(range(20), 10))
print("---로또번호생성---")
print(random.sample(range(1,46), 5))

print(abspath("python.exe"))
print(basename("c:\\python310\\python.exe"))

fileName = "c:\\python310\\python.exe"
if exists(fileName):
    print("파일의 크기:{0}".format(getsize(fileName)))
else:
    print("파일 없음")

print("현재 작업폴더:{0}".format(getcwd()))

print("---운영체제---")
print(name)
print(environ)
system("notepad.exe")


