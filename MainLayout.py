from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtCore import Qt
from MyLable import myLabel

class mainLayout(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.myLable = myLabel
        self.addWidget(self.myLable)