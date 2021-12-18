from PyQt5.QtWidgets import QApplication,QWidget

from Window import MyWindow
if __name__ == '__main__':
    app = QApplication([]) #создание объекта приложения
    window = MyWindow() #создание объекта главного окна
    #window.show()
    app.exec_()# ОЖИДАНИЕ ЗАКРЫТИЯ программы
    
