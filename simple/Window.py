from PyQt5.QtWidgets import QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        someVar = 6
        self.resize(400,400)
        self.show()