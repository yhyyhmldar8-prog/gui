from PySide6.QtWidgets import * 
from PySide6.QtCore import Qt

q = QHBoxLayout()
w = QHBoxLayout()
e = QHBoxLayout()
r = QHBoxLayout()
t = QHBoxLayout()
layout = QVBoxLayout()
a = ""
def nu(nu):
    global a 
    a += nu
    line.setText(a)

def equal():
    global a
    line.setText(str(int(eval(a))))

def cle():
    global a
    line.clear()
    a = ""

app = QApplication([])

window = QWidget()
window.setWindowTitle("second project")
window.setFixedSize(480 , 240)
window.setLayout(layout)
label = QLabel("coucletor")
layout.addWidget(label)

layout.addLayout(t)
line = QLineEdit(window)
line.setReadOnly(True)
t.addWidget(line)

layout.addLayout(q)
noh = QPushButton("9" , window)
noh.clicked.connect(lambda: nu("9"))
q.addWidget(noh)

hasht = QPushButton("8" , window)
hasht.clicked.connect(lambda: nu("8"))
q.addWidget(hasht)

haft = QPushButton("7" , window)
haft.clicked.connect(lambda: nu("7"))
q.addWidget(haft)

#تفریق
menha = QPushButton("-", window)
menha.clicked.connect(lambda: nu("-"))
q.addWidget(menha)

layout.addLayout(w)
shish = QPushButton("6" , window)
shish.clicked.connect(lambda: nu("6"))
w.addWidget(shish)

pang = QPushButton("5" , window)
pang.clicked.connect(lambda: nu("5"))
w.addWidget(pang)

four = QPushButton("4" , window)
four.clicked.connect(lambda: nu("4"))
w.addWidget(four)

#تقسیم
tagsim = QPushButton("/", window)
tagsim.clicked.connect(lambda: nu("/"))
w.addWidget(tagsim)

layout.addLayout(e)
se = QPushButton("3" , window)
se.clicked.connect(lambda: nu("3"))
e.addWidget(se)

do = QPushButton("2" , window)
do.clicked.connect(lambda: nu("2"))
e.addWidget(do)

yek = QPushButton("1" , window)
yek.clicked.connect(lambda: nu("1"))
e.addWidget(yek)

#ضرب
zarb = QPushButton("*", window)
zarb.clicked.connect(lambda: nu("*"))
e.addWidget(zarb)

layout.addLayout(r)
o = QPushButton("0" , window)
o.clicked.connect(lambda: nu("0"))
r.addWidget(o)

qe = QPushButton("=" , window)
qe.clicked.connect(equal)
r.addWidget(qe)

c = QPushButton("C" , window)
c.clicked.connect(cle)
r.addWidget(c)

#جمع
plus = QPushButton("+", window)
plus.clicked.connect(lambda: nu("+"))
r.addWidget(plus)

window.show()

app.exec()