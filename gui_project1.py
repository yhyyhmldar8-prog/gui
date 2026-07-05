from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
def r():
    print(log.text())
    print(pas.text())
def c():
    log.clear()
    pas.clear()
app = QApplication([])

layout1 = QVBoxLayout()

layout2 = QHBoxLayout()

window = QWidget()
window.setWindowTitle("first real project with pyside6")
window.setBaseSize(1080 , 1080)
window.setLayout(layout1)

txt = QLabel("Login" , window)
layout1.addWidget(txt)

log = QLineEdit(window)
log.setPlaceholderText("User Name")
layout1.addWidget(log)

pas = QLineEdit(window)
pas.setPlaceholderText("Password")
pas.setEchoMode(QLineEdit.EchoMode.Password)
layout1.addWidget(pas)

layout1.addLayout(layout2)

b1 = QPushButton("Login" , window)
b1.clicked.connect(r)
layout2.addWidget(b1)

b2 = QPushButton("clear" , window)
b2.clicked.connect(c)
layout2.addWidget(b2)
window.show()

app.exec()