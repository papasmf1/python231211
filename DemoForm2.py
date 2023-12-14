# DemoForm2.py 
# DemoForm2.ui(화면단)  + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 
#웹서버에 요청
import requests
#크롤링
from bs4 import BeautifulSoup

#화면을 로딩
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스를 정의(QMainWindow)
class DemoForm(QMainWindow, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    def firstClick(self):
        url = "https://www.daangn.com/fleamarket/"
        response = requests.get(url)
        #검색이 용이한 객체
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all("div", attrs={"class":"card-desc"})
        #파일에 저장
        f = open("dangn.txt", "wt", encoding="utf-8")
        for post in posts:
            title = post.find("h2", attrs={"class":"card-title"})
            price = post.find("div", attrs={"class":"card-price"})
            addr = post.find("div", attrs={"class":"card-region-name"})
            title = title.text.strip().replace("\n", "")
            price = price.text.strip().replace("\n", "")
            addr = addr.text.strip().replace("\n", "")
            print("{0}, {1}, {2}".format(title, price, addr))
            f.write(f"{title}, {price}, {addr}\n")
        f.close() 
        self.label.setText("당근마켓 크롤링 완료")
    def secondClick(self):
        self.label.setText("두번째 버튼을 클릭~!")
    def thirdClick(self):
        self.label.setText("세번째 버튼을 클릭했어~~")


#직접 모듈을 실행했는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm() 
    demoWindow.show() 
    app.exec_() 

    