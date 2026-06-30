from PySide6.QtWidgets import *
def h():
    label.setText("connected")

app = QApplication([])

window = QWidget()
window.setWindowTitle("first project")
window.resize( 720 , 500 )

label = QLabel ("hello world" , window)
label.move(360, 250)

button = QPushButton("click me" , window)
button.move(360 , 270)
button.clicked.connect(h)

window.show()

app.exec()