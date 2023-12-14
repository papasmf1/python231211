# web1.py 
#웹크롤링을 위한 선언 
from bs4 import BeautifulSoup

#웹페이지를 로딩(전체 문서를 하나의 문자열 변수로 담기)
#메서드체인(함수나 메서드를 한번에 호출) 
page = open("test01.html", "rt", encoding="utf-8").read() 

#검색이 용이한 객체(HTML문서를 로딩)
soup = BeautifulSoup(page, "html.parser")

#전체 문서 
#print(soup.prettify())
#<p>태그 전부 검색
#print(soup.find_all("p"))
#첫번째<p>만 검색
#print(soup.find("p"))
#필터링:<p class="outer-text">
#print(soup.find_all("p", class_ ="outer-text"))
#최근에 사용하는 코드(attributes)
#print(soup.find_all("p", attrs={"class":"outer-text"}))

#특정태그(id)
#print(soup.find(id="first"))

#태그 내부에 컨텐츠(text)
for tag in soup.find_all("p"):
    title = tag.text.strip() 
    title = title.replace("\n", "")
    print(title)









