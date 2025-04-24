# export QT_SELECT=qt6

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic

# ui 파일 연결 - 코드 파일과 같은 폴더 내에 위치
from_class = uic.loadUiType("calculator.ui")[0]

# 화면 클래스
class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("CALCULATOR")

        self.result = ''
        self.prev = ''
        self.count = 0
        self.nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.calcs = ['/', '*', '-', '+', '=']
        self.on = False

        # buttons
        # ON/OFF
        self.onOff_btn.clicked.connect(self.onOff)

        # numbers
        self.btn_0.clicked.connect(self.btn0_clicked)
        self.btn_1.clicked.connect(self.btn1_clicked)
        self.btn_2.clicked.connect(self.btn2_clicked)
        self.btn_3.clicked.connect(self.btn3_clicked)
        self.btn_4.clicked.connect(self.btn4_clicked)
        self.btn_5.clicked.connect(self.btn5_clicked)
        self.btn_6.clicked.connect(self.btn6_clicked)
        self.btn_7.clicked.connect(self.btn7_clicked)
        self.btn_8.clicked.connect(self.btn8_clicked)
        self.btn_9.clicked.connect(self.btn9_clicked)

        # operator
        self.btn_add.clicked.connect(self.add)
        self.btn_sub.clicked.connect(self.subt)
        self.btn_mul.clicked.connect(self.multi)
        self.btn_div.clicked.connect(self.div)
        self.btn_equal.clicked.connect(self.equal)

        # delete
        self.btn_clear.clicked.connect(self.clear)
        self.btn_allc.clicked.connect(self.all_clear)

        # dot
        self.btn_dot.clicked.connect(self.dot)

        # sign
        self.btn_sign.clicked.connect(self.sign)

        self.resultOut.setText(self.result)

    # ON/OFF
    def onOff(self):
        if self.result == '':
            self.on = True
            self.result = '0'
        else:
            self.on = False
            self.result = ''

        self.resultOut.setText(self.result)

    # nums pad
    def btn0_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '0'
        self.resultOut.setText(self.result)
    
    def btn1_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '1'
        self.resultOut.setText(self.result)

    def btn2_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '2'
        self.resultOut.setText(self.result)

    def btn3_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '3'
        self.resultOut.setText(self.result)

    def btn4_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '4'
        self.resultOut.setText(self.result)

    def btn5_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '5'
        self.resultOut.setText(self.result)

    def btn6_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '6'
        self.resultOut.setText(self.result)

    def btn7_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '7'
        self.resultOut.setText(self.result)

    def btn8_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '8'
        self.resultOut.setText(self.result)

    def btn9_clicked(self):
        if self.on == False:
            return

        if self.result == '0':
            self.result = ''

        if len(self.result) >= 2:
            if self.result[-1] == '0':
                if self.result[-2] in self.calcs:
                    self.result = self.result[:-1]

        self.result += '9'
        self.resultOut.setText(self.result)

    # operators pad
    def add(self):
        if self.on == False:
            return
        
        if self.result == '0':
            return
        
        if self.result[-1] in self.calcs:
            self.result = self.result[:-1]
        
        self.count = 0
        self.result += '+'
        self.resultOut.setText(self.result)

    def subt(self):
        if self.on == False:
            return
        
        if self.result == '0':
            return
        
        if self.result[-1] in self.calcs:
            self.result = self.result[:-1]

        self.count = 0
        self.result += '-'
        self.resultOut.setText(self.result)
    
    def multi(self):
        if self.on == False:
            return
        
        if self.result == '0':
            return
        
        if self.result[-1] in self.calcs:
            self.result = self.result[:-1]

        self.count = 0
        self.result += '*'
        self.resultOut.setText(self.result)

    def div(self):
        if self.on == False:
            return
        
        if self.result == '0':
            return
        
        if self.result[-1] in self.calcs:
            self.result = self.result[:-1]
        
        self.count = 0
        self.result += '/'
        self.resultOut.setText(self.result)

    def equal(self):
        try:
            if self.on == False:
                return
        
            if (self.result == '0') or (self.result[-1] in self.calcs):
                return
            
            if self.count >= 1:
                self.result = self.result + self.prev
            else:
                for i in range(len(self.result)-1, -1, -1):
                    if self.result[i] in self.calcs:
                        if self.result[i-1] in self.nums:
                            self.prev = self.result[i:]
                            break
                        elif self.result[i-1] in self.calcs:
                            self.prev = self.result[i-1:]
                            break

            self.result = str(eval(self.result))
            
            if (abs(float(self.result)) > 10**15 or abs(float(self.result)) < 10**-15):
                if float(self.result) == 0:
                    self.result = '0'
                else:
                    self.result = str('%.14e'%float(self.result))
            
            self.count += 1
            self.resultOut.setText(self.result)

        except:
            QMessageBox.warning(self, 'QMessageBox - setText', 'ERROR')

            self.result = '0'
            self.resultOut.setText(self.result)

    # delete pad
    def clear(self):
        if self.on == False:
            return
        
        if len(self.result) > 2:
            if self.result[-1] not in self.calcs and self.result[-2] == '-' and self.result[-3] in self.calcs:
                self.result = self.result[:-2]
        
        self.result = self.result[:-1]

        if self.result == '':
            self.result = '0'

        self.resultOut.setText(self.result)

    def all_clear(self):
        if self.on == False:
            return
        
        self.count = 0
        self.prev = ''
        self.result = '0' 
        self.resultOut.setText(self.result)

    # etc
    def dot(self):
        if self.on == False:
            return
        
        if self.result[-1] != '.':
            if self.result[-1] in self.calcs:
                self.result += '0.'
            else:
                dot_num = 0

                for i in range(len(self.result)-1, -1, -1):
                    if self.result[i] == '.':
                        dot_num += 1

                    if self.result[i] in self.calcs:
                        break

                if dot_num >= 1:
                    return

                self.result += '.'

            self.resultOut.setText(self.result)

        else:
            return

    def sign(self):
        if self.on == False:
            return
        
        if self.result == '0':
            return
        else:
            for i in range(len(self.result)-1, -1, -1):
                if self.result[i] in self.calcs:
                    if self.result[i] in self.calcs and i == len(self.result) - 1:
                        break                    
                    elif self.result[i] == '-' and self.result[i-1] in self.calcs:
                        self.result = self.result[:i] + self.result[i+1:]
                        break
                    elif i == 0 and self.result[i] == '-':
                        self.result = self.result[1:]
                        break
                    else:
                        self.result = self.result[:i+1] + '-' + self.result[i+1:]
                        break
                else:
                    if i == 0:
                        self.result = '-' + self.result
                        break
                    elif self.result[i] == '0' and self.result[i-1] in self.calcs:
                        if i == len(self.result) - 1:
                            break
                        else:
                            continue
                    else:
                        continue

            self.resultOut.setText(self.result)

# Python 메인 함수
if __name__ == "__main__":
    app = QApplication(sys.argv) # 프로그램 실행
    myWindow = WindowClass()     # 화면 클래스 생성
    myWindow.show()              # 프로그램 화면 보이기

    sys.exit(app.exec())         # 프로그램 종료까지 동작