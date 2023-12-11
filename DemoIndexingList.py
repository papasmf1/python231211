# DemoIndexingList.py 
strA = "파이썬은 강력해"
strB = "python is very powerful"

print(len(strA))
print(len(strB))
print(strA[:3])
print(strB[:6])
print(strB[-3:])
print(strB[-8:])

print("---리스트---")
colors = ["red", "blue", "green"]
print(len(colors))
colors.append("white")
colors.extend(["red","yellow","pink"])
print(colors)
colors.sort()
print(colors)
colors.remove("blue")
print(colors)

#반복구문
#디버깅할 때 중단점(Break Point)
for item in colors:
    print(item)

