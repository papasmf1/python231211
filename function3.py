#람다 함수 
g = lambda x,y:x*y 
print(g(3,4))

print( (lambda x:x*x)(3) )

print( globals() )

print("---필터링---")
lst = [10, 25, 30]
itemL = filter(lambda x:x>20, lst)
for item in itemL:
    print(item)


#분기구문 
#선택한 블럭을 주석처리: ctrl + / 
# score = int(input("점수를 입력:"))
# if 90 <= score <= 100:
#     grade = "A"
# elif 80 <= score < 90:
#     grade = "B"
# elif 70 <= score < 80:
#     grade = "C"
# else:
#     grade = "D"

# print("등급은 ", grade)

value = 5 
while value > 0:
    print(value)
    value -= 1 

fruits = {"apple":10, "kiwi":20}
for item in fruits.items():
    print(item)


print("---break---")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---continue---")
lst = list(range(1,11))
print(lst)
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))

#print(help("dir"))
print("---range()---")
years = list(range(2000, 2024))
print(years)
days = list(range(1,32))
print(days)

print("---리스트 내장---")
lst = list(range(1,11))
print([i**2 for i in lst if i > 5])
tp = ("apple", "kiwi", "orange")
print([len(i) for i in tp])


#구구단
for i in [2,3,4,5,6]:
    print("{0}단 출력".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(i, j, i*j))


#f-string문법을 사용 
for i in [2,3,4,5,6]:
    print(f"{i}단 출력")
    for j in [1,2,3,4,5,6,7,8,9]:
        print(f"{i} * {j} = {i*j}")


