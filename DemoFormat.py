#문자열 연결 
url = "http://www.multi.com/?page=" + str(1) 
print(url)

for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(5))


print("---서식문자---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))
print("{0:,}".format(15000))

#파일쓰기
#raw string notation(가공하지 않은 표기)
f = open(r"c:\work\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close() 

#파일읽기
print("---파일 읽기---")
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)
#처음으로 돌아가~ 
f.seek(0)
#코드에서 보정
print(f.readline(), end="")
print(f.readline(), end="")

f.seek(0)
result = f.readlines()
for item in result:
    print(item, end="")

f.close()


