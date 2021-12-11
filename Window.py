
from PyQt5.QtWidgets import QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.show()