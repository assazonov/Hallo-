from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QListWidget,
QPushButton, QLineEdit, QTextEdit, QVBoxLayout, QHBoxLayout)

app = QApplication([])
notes_win = QWidget()
notes_win.setWindowsTitle('Умные заметки')

notes_win.resize(900,600)

list_notes = QListWidget()
list_notes_label = QLabel

button_note_create = QPushButton('Создать заметку')
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit() #создаем объект поля для заметок
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметку по тегу')
list_tags = QListWidget()
list_tag_label = QLabel('Список тегов') # создание объекта надписи

#расположение виджетов по лейаутам
layout_notes = QHBoxLayout()
col_1 = QVBoxLayout() #создание направляющей линии 
col_1.addWidget(field_text) #добавляем виджет лейаут

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

row_1 = QHBoxLayout()
row_1.addWidget(button_note_create)
row_1.addWidget(button_note_del)
row_2 = QHBoxLayout()
row_2 = addWidget(button_note_save)
col_2.addLayout(row_1) #добавление одного лейаута на другой для перекрещения
col_2.addLayout(row_2)

col_2.addWidget(list_tag_label)
col_2.addWidget(list_tags)
col_2.addWidget(field_tag)
row_3.QHBoxLayout()
row_3.addWidget(button_tag_add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout()
row_4.addWidget(button_tag_search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)

layout_notes.addLayout(col_1, stretch=2) #добавляем линии на главный лейаут и растягиваем его в ширину
layout_notes.addLayout(col_2, stretch=1)
notes_win.setLayout(layout_notes) # добавление главного лейаута на объект окна
notes_win.show() #отображаем окно
app.exec() #функция которая не позволяет закрываться окну после выполнения кода