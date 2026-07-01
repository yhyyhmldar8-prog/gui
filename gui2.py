from PySide6.QtWidgets import * 
from PySide6.QtGui import QFont
def h():
    label.setText("connected")
    button.setText("hehehe")
    button.setEnabled(False)
    label.setVisible(False)
def g():
    label.setVisible(True)
app = QApplication([])
font = QFont("Arial", 10)

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
button1.clicked.connect(g)

window.show()

app.exec()