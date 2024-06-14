from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
default_le_style = """
           QLineEdit {
               margin: 1px;
               padding: 20px;
               background-color: white;
               font-size: 11px;
               font-weight: bold;
               color: #555;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           QLineEdit:read-only {
               background-color: #f0f0f0;
           }
       """
GRID_SIZE = (8, 8)

def setup_easy(scanword_instance):
    for i in range(GRID_SIZE[0]):
        row = []
        for j in range(GRID_SIZE[1]):
            boxedit = QLineEdit()
            boxedit.setFixedSize(75, 75)
            boxedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            boxedit.setReadOnly(True)
            boxedit.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Отключаем фокусировку на виджете
            boxedit.setMaxLength(1)
            boxedit.setStyleSheet(default_le_style)
            scanword_instance.grid_layout.addWidget(boxedit, i, j)
            row.append(boxedit)  # Добавляем boxedit в строку
        scanword_instance.boxedits.append(row)
    scanword_instance.get_question(position=(1, 0), num_elements=8, direction='horizontal',
                      question="Мозговая\n кривая", answer='извилина',
                      start_x=0, start_y=0)
    scanword_instance.get_question(position=(3, 0), num_elements=7, direction='horizontal',
                      question="Ответное\n действие", answer='реакция',
                      start_x=2, start_y=0)
    scanword_instance.get_question(position=(4, 0), num_elements=3, direction='horizontal',
                      question="... Рот,\n актер", answer='тим',
                      start_x=5, start_y=1)
    scanword_instance.get_question(position=(5, 0), num_elements=3, direction='horizontal',
                      question="Бык,на\n котором \n пишут", answer='вол',
                      start_x=6, start_y=1)
    scanword_instance.get_question(position=(6, 0), num_elements=8, direction='horizontal',
                      question="Гибкие\n доспехи\n из колец", answer='кольчуга',
                      start_x=7, start_y=0)
    scanword_instance.get_question(position=(4, 2), num_elements=5, direction='horizontal',
                      question="Казак в \nзвании\n офицера", answer='есаул',
                      start_x=4, start_y=3)
    scanword_instance.get_question(position=(1, 2), num_elements=8, direction='vertical',
                      question="Свирепая\n жесто-\nкость",
                      answer='зверство',
                      start_x=0, start_y=1)
    scanword_instance.get_question(position=(1, 3), num_elements=5, direction='vertical',
                      question="Советский\n вело-\nсипед",
                      answer='лацис',
                      start_x=0, start_y=4)
    scanword_instance.get_question(position=(3, 2), num_elements=6, direction='vertical',
                      question="На \nрисунке?",
                      answer='кремль',
                      start_x=2, start_y=3)
    scanword_instance.get_question(position=(1, 5), num_elements=3, direction='vertical',
                      question="Наивыс-\nшая\n точка\n Крита?",
                      answer='ида',
                      start_x=2, start_y=5)
    scanword_instance.get_question(position=(1, 7), num_elements=3, direction='vertical',
                      question="Город в\n Костром-\nской\n области?",
                      answer='нея',
                      start_x=0, start_y=6)
    scanword_instance.get_question(position=(2, 7), num_elements=5, direction='vertical',
                      question="Греческая \nбуква",
                      answer='альфа',
                      start_x=3, start_y=7)
    scanword_instance.get_question(position=(3, 6), num_elements=4, direction='vertical',
                      question="Ездок по \nгладиль-\nной доске",
                      answer='утюг',
                      start_x=4, start_y=6)
