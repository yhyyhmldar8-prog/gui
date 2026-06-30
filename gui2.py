from PySide6.QtWidgets import * 
from PySide6.QtGui import QFont
def h():
    label.setText("connected")

app = QApplication([])
font = QFont("Arial", 32)

window = QWidget()
window.setWindowTitle("first project")
window.setGeometry( 0 , 0 , 720 , 500 )

label = QLabel ("hello world" , window)
label.setGeometry(100 , 10 , 300 , 200)
label.setFont(font)

button = QPushButton("click me" , window)
button.setGeometry(340 , 100 , 340 , 100)
button.clicked.connect(h)

window.show()

app.exec()