from PySide6.QtWidgets import *

def but1():
    txtinline = line.text()
    if txtinline != "":
        lis.addItem(txtinline)
        line.clear()
        line.setFocus()
    else:
        line.setPlaceholderText("dont click add when this spot is empty!")

def but2():
    ite = lis.currentRow()
    if ite != None:
        lis.takeItem(ite)    
    else:
        pass
def but3():
    lis.clear()

app = QApplication([])

window = QWidget()
window.setWindowTitle("third project")
window.setFixedSize(480 , 360)

lay1 = QVBoxLayout(window)

text1 = QLabel("thank you for using this app" , window)
lay1.addWidget(text1)


line = QLineEdit(window)
line.setPlaceholderText("enter your mission")
lay1.addWidget(line)

lay2 = QHBoxLayout(window)
lay1.addLayout(lay2)

bu1 = QPushButton("add" , window)
bu1.clicked.connect(but1)
lay2.addWidget(bu1)

bu2 = QPushButton("delete" , window)
bu2.clicked.connect(but2)
lay2.addWidget(bu2)

lis = QListWidget(window)
lay1.addWidget(lis)

bu3 = QPushButton("clear list" , window)
bu3.clicked.connect(but3)
lay1.addWidget(bu3)
window.show()

app.exec()