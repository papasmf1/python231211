# DemoForm.py 
# DemoForm.ui(화면단)  + DemoForm.py(로직단)

import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#화면을 로딩
form_class = uic.loadUiType("DemoForm.ui")[0]

#폼클래스를 정의
class DemoForm(QDialog, form_class):
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.label.setText("첫번째 데모입니다~~")

#직접 모듈을 실행했는지 체크
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm() 
    demoWindow.show() 
    app.exec_() 

    