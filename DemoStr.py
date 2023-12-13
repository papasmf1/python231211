# DemoStr.py 
#print(dir(str))

strA = "python is very powerful"
strB = "파이썬은 강력해"

print(len(strA))
print(len(strB))
print(strA.capitalize())
print(strA.count("p"))
print(strA.count("p", 7))

print("demo.ppt".startswith("demo"))
print("demo.ppt".endswith("ppt"))
print("MBC2580".isalnum())
print("MBC:2580".isalnum())
print("2580".isdecimal())

data = "<<< spam and ham  >>>"
result = data.strip("<> ")
print(data)
print(result)
result2 = result.replace("spam", "spam egg")
print(result2)
print("---리스트로 분리---")
lst = result2.split()
print(lst)
print("---하나의 문자열---")
print(":)".join(lst))


