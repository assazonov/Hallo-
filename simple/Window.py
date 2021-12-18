from PyQt5.QtWidgets import QWidget

from MainLayout import mainLayout 


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(400,400)
        self.mainLayout = mainLayout()
        self.setLayout(self.mainLayout)
        self.show()