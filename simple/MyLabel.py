from PyQt5.QtWidgets import QLabel

class myLabel(QLabel): 
    def __init__(self):
        super().__init__()
        self.setText('хало')