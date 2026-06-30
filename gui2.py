from PySide6.QtWidgets import *
def h():
    label.setText("connected")

app = QApplication([])

window = QWidget()
window.setWindowTitle("first project")
window.resize( 720 , 500 )

label = QLabel ("hello world" , window)
label.setGeometry(100 , 10 , 200 , 200)

button = QPushButton("click me" , window)
button.setGeometry(340 , 100 , 340 , 100)
button.clicked.connect(h)

window.show()

app.exec()