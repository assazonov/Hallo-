from PyQt5.QtWidgets import  QApplication,QWidget

from Window import MyWindow

if __name__ == '__main__':
    app = QApplication([]) #создание объекта приложения
    mainWindow = MyWindow()
    #mainWindow.show()
    app.exec_() #ожидание закрытие программы