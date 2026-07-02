from PySide6.QtWidgets import * 
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
def x():
   print(label.isVisible())
   print(button.isEnabled())
def h():
    label.setText("connected")
    button.setText("hehehe")
    button.setEnabled(False)
    label.setEnabled(False)
    window.setWindowTitle("next")
    label.setGeometry( 0 ,0 ,200 , 10)
def g():
    label.setEnabled(True)
    window.close()
def z():
    label.setText("its a joke dont angry")
    buttom.setStyleSheet(" color: red ; background-color:green")
app = QApplication([])
font = QFont("Arial", 10)
font1 = QFont("Arial" , 15)

window = QWidget()
window.setWindowTitle("first project")
window.setFixedSize(720 , 720)

label = QLabel ("hello world" , window)
label.setGeometry(0 , 0 , 300 , 20)
label.setFont(font)
label.setStyleSheet("color: green; background-color : yellow")

button = QPushButton("click me" , window)
button.setGeometry(340 , 100 , 340 , 100)
button.clicked.connect(h)

button1 = QPushButton("its a joke click again" , window)
button1.setGeometry( 50 , 100 , 200 , 50)
button1.setCursor(Qt.CursorShape.ClosedHandCursor)
button1.setObjectName("dokme")
button1.clicked.connect(g)

buttom = QPushButton("again test", window)
buttom.setGeometry( 20, 20 , 100,100 )
buttom.clicked.connect(z)
buttom.setFont(font1)
buttom.setToolTip("if you click this button you will die or get rich")
def k():
    print(inpot.text())
t = QPushButton("he" , window)
t.clicked.connect(k)

inpot = QLineEdit(window)
inpot.setGeometry(0 , 500 , 100 , 20)

but = QPushButton("setvisiable or enable" , window)
but.clicked.connect(x)
but.setGeometry(500 , 500 , 200 , 100)
window.show()

app.exec()