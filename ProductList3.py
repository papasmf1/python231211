import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5 import uic 
import sqlite3
import os.path 

# DB 파일이 없으면 만들고 있다면 접속한다.
if os.path.exists("ProductList.db"):
    con = sqlite3.connect("ProductList.db")  # 데이터베이스 파일이 있는 경우 연결
    cur = con.cursor()
else: 
    con = sqlite3.connect("ProductList.db")  # 데이터베이스 파일이 없는 경우 생성 후 연결
    cur = con.cursor()
    cur.execute("create table Products (id integer primary key autoincrement, Name text, Price integer);")

# 디자인 파일을 로딩
form_class = uic.loadUiType("ProductList3.ui")[0]

class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        # 초기값 셋팅 
        self.id = 0 
        self.name = ""
        self.price = 0 

        # QTableWidget의 컬럼폭 셋팅하기 
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 200)
        self.tableWidget.setColumnWidth(2, 100)
        # QTableWidget의 헤더 셋팅하기
        self.tableWidget.setHorizontalHeaderLabels(["제품ID", "제품명", "가격"])
        # 탭키로 네비게이션 금지 
        self.tableWidget.setTabKeyNavigation(False)
        
        # 더블클릭 시그널 처리
        self.tableWidget.doubleClicked.connect(self.doubleClick)

    def addProduct(self):
        try:
            # 입력 파라메터 처리 
            self.name = self.prodName.text()
            self.price = int(self.prodPrice.text())  # 가격을 정수로 변환
            cur.execute("insert into Products (Name, Price) values(?,?);", (self.name, self.price))
            con.commit()  # 커밋
            self.getProduct()  # 리프레시
        except ValueError:
            QMessageBox.warning(self, '입력 오류', '올바른 가격을 입력하세요.')

    def updateProduct(self):
        try:
            # 업데이트 작업시 파라메터 처리 
            self.id  = self.prodID.text()
            self.name = self.prodName.text()
            self.price = int(self.prodPrice.text())  # 가격을 정수로 변환
            cur.execute("update Products set name=?, price=? where id=?;", (self.name, self.price, self.id))
            con.commit()  # 커밋
            self.getProduct()  # 리프레시
        except ValueError:
            QMessageBox.warning(self, '입력 오류', '올바른 가격을 입력하세요.')

    def removeProduct(self):
        try:
            # 삭제 파라메터 처리 
            self.id  = self.prodID.text() 
            cur.execute("delete from Products where id=?", (self.id,))
            con.commit()  # 커밋
            self.getProduct()  # 리프레시
        except ValueError:
            QMessageBox.warning(self, '입력 오류', '올바른 ID를 입력하세요.')

    def getProduct(self):
        try:
            cur.execute("select * from Products;") 
            rows = cur.fetchall()
            
            self.tableWidget.setRowCount(len(rows))
            
            for row, item in enumerate(rows):
                int_as_strID = "{:10}".format(item[0])
                int_as_strPrice = "{:10}".format(item[2])
                
                itemID = QTableWidgetItem(int_as_strID)
                itemID.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(row, 0, itemID)
                self.tableWidget.setItem(row, 1, QTableWidgetItem(item[1]))
                
                itemPrice = QTableWidgetItem(int_as_strPrice)
                itemPrice.setTextAlignment(Qt.AlignRight)
                self.tableWidget.setItem(row, 2, itemPrice)
                
        except Exception as e:
            QMessageBox.critical(self, '오류', '데이터를 가져오는 동안 오류가 발생했습니다:\n{}'.format(str(e)))

    def doubleClick(self):
        self.prodID.setText(self.tableWidget.item(self.tableWidget.currentRow(), 0).text())
        self.prodName.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.prodPrice.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = Window()
    myWindow.show()
    app.exec_()
