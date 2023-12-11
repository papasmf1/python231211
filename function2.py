#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #지역변수로 리스트를 저장
    result = [] 
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result 

#함수 호출(중단점 추가)
print(intersect("HAM", "SPAM"))

#지역변수와 전역변수
x = 10 
def func1(a):
    return a+x 

#호출
print(func1(1))

def func2(a):
    x = 5 
    return a+x 

#호출
print(func2(1))



