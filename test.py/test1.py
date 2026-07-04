from PySide6.QtWidgets import *

app = QApplication([])

def change_color(color):
    label.setStyleSheet(f"color: {color}")

window = QWidget()

label = QLabel("Hello", window)

red_button = QPushButton("Red", window)
green_button = QPushButton("Green", window)

red_button.clicked.connect(lambda: change_color("red"))
green_button.clicked.connect(lambda: change_color("green"))

layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(red_button)
layout.addWidget(green_button)

window.setLayout(layout)

window.show()
app.exec()