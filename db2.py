# db2.py 
#커밋이 없으면 데이터 사라진다! 
import sqlite3

#연결객체(파일 저장)
con = sqlite3.connect("c:\\work\\sample.db")
#커서객체
cur = con.cursor() 

#테이블 구조(자료구조)
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('김길동', '010-111-1234');")

#입력 파라메터 처리 
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))

#다중의 레코드 
datalist = (("강감찬","010-333"), ("박문수","010-456"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색 구문
cur.execute("select * from PhoneBook;")
# for row in cur:
#     print(row)
# print("---fetchone()--")
# print(cur.fetchone())
# print("---fetchmany(2)--")
# print(cur.fetchmany(2))
print("---fetchall()--")
print(cur.fetchall())

#연결객체
con.commit() 


