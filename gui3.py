from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
app = QApplication([])

def q(qort):
    print(qort)

layoutr = QHBoxLayout()

layout = QVBoxLayout()

window = QWidget()
window.setWindowTitle("test")
window.setFixedSize(1280 , 720)
window.setLayout(layout)

lab = QLabel("noob" , window)
layout.addWidget(lab)

layout.addLayout(layoutr)

b = QPushButton("hello" , window)
layoutr.addWidget(b)
b.clicked.connect(lambda:q("hello") )

d = QPushButton("goodbye" , window)
layoutr.addWidget(d)
d.clicked.connect(lambda:q("goodbye") )
window.show()

app.exec()