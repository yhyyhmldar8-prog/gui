from PySide6.QtWidgets import * 
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
def h():
    label.setText("connected")
    button.setText("hehehe")
    button.setEnabled(False)
    label.setEnabled(False)
    window.setWindowTitle("next")
    label.setGeometry( 0 ,0 ,200 , 10)
def g():
    label.setEnabled(True)
def z():
    label.setText("its a joke dont angry")
    buttom.setStyleSheet(" color: red ; background-color:green")
app = QApplication([])
font = QFont("Arial", 10)
font1 = QFont("Arial" , 15)

window = QWidget()
window.setWindowTitle("first project")
window.setGeometry( 0 , 0 , 720 , 500 )

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
window.show()

app.exec()