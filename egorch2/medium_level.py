from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
GRID_SIZE = (10, 10)
default_le_style = """
           QLineEdit {
               margin: 1px;
               padding: 20px;
               background-color: white;
               font-size: 30px;
               font-weight: bold;
               color: #555;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           QLineEdit:read-only {
               background-color: #f0f0f0;
           }
       """
def setup_medium(scanword_instance):
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
    scanword_instance.get_question(position=(0, 0), num_elements=5, direction='horizontal',
                      question="Рогач \n из\n Зодиака", answer='телец',
                      start_x=1, start_y=0)
    scanword_instance.get_question(position=(2, 0), num_elements=5, direction='horizontal',
                      question="Время \n для\n смелого\n гулянья",
                      answer='досуг',
                      start_x=3, start_y=0)
    scanword_instance.get_question(position=(9, 1), num_elements=4, direction='horizontal',
                      question="...\nГосподня",
                      answer='риза',
                      start_x=8, start_y=0)
    scanword_instance.get_question(position=(9, 3), num_elements=6, direction='horizontal',
                      question="Оперетта \nЛегара\n<<...\nулыбок>>",
                      answer='страна',
                      start_x=9, start_y=4)
    scanword_instance.get_question(position=(8, 4), num_elements=5, direction='horizontal',
                      question="Звездный \n накопи-\nтель\n офицера",
                      answer='погон',
                      start_x=8, start_y=5)
    scanword_instance.get_question(position=(7, 3), num_elements=6, direction='horizontal',
                      question="Раздра-\nжение \nна себя",
                      answer='досада',
                      start_x=7, start_y=4)
    scanword_instance.get_question(position=(5, 3), num_elements=6, direction='horizontal',
                      question="Меди-\nцинская \nстекло-\nтара",
                      answer='ампула',
                      start_x=5, start_y=4)
    scanword_instance.get_question(position=(3, 5), num_elements=5, direction='horizontal',
                      question="Поворот, \nкоторый \nзакла-\nдывают",
                      answer='вираж',
                      start_x=2, start_y=5)
    scanword_instance.get_question(position=(1, 5), num_elements=5, direction='horizontal',
                      question="Суть \nрефе-\nрендума",
                      answer='опрос',
                      start_x=0, start_y=5)
    scanword_instance.get_question(position=(4, 5), num_elements=4, direction='horizontal',
                      question="Травма,\nне для\n своего\n локтя",
                      answer='укус',
                      start_x=4, start_y=6)
    scanword_instance.get_question(position=(7, 1), num_elements=5, direction='horizontal',
                      question="Птица\n ухарь и \nхохотун",
                      answer='филин',
                      start_x=6, start_y=0)
    scanword_instance.get_question(position=(5, 1), num_elements=4, direction='horizontal',
                      question="Облег-\nчитель \n Буренок",
                      answer='дояр',
                      start_x=4, start_y=1)
    scanword_instance.get_question(position=(0, 2), num_elements=5, direction='vertical',
                      question="Снасть \n на\n Золотую\n Рыбку",
                      answer='невод',
                      start_x=0, start_y=1)
    scanword_instance.get_question(position=(4, 0), num_elements=5, direction='vertical',
                      question="Область \n влияния",
                      answer='сфера',
                      start_x=5, start_y=0)
    scanword_instance.get_question(position=(2, 2), num_elements=7, direction='vertical',
                      question="Повод к \n греху",
                      answer='соблазн',
                      start_x=3, start_y=2)
    scanword_instance.get_question(position=(6, 5), num_elements=3, direction='vertical',
                      question="'Пар-\nтийная'\n про-\nдажа",
                      answer='опт',
                      start_x=7, start_y=5)
    scanword_instance.get_question(position=(6, 6), num_elements=3, direction='vertical',
                      question="Его из\n избы не\n выносят",
                      answer='сор',
                      start_x=7, start_y=6)
    scanword_instance.get_question(position=(3, 7), num_elements=6, direction='vertical',
                      question="Абрикос,\n давший \n себе за-\nсохнуть ",
                      answer='курага',
                      start_x=4, start_y=7)
    scanword_instance.get_question(position=(0, 4), num_elements=5, direction='vertical',
                      question="Что у \nрыбки \nбыло \nзолотым?",
                      answer='чешуя',
                      start_x=0, start_y=3)
    scanword_instance.get_question(position=(2, 4), num_elements=5, direction='vertical',
                      question="'Титул'\nбольших \nотелей",
                      answer='гранд',
                      start_x=3, start_y=4)
    scanword_instance.get_question(position=(1, 7), num_elements=6, direction='vertical',
                      question="'Знал бы\n ...-жил\n бы в\n Сочи'",
                      answer='прикуп',
                      start_x=0, start_y=6)
    scanword_instance.get_question(position=(1, 9), num_elements=6, direction='vertical',
                      question="Преду-\nпреди-\nтельный\n жрец",
                      answer='оракул',
                      start_x=0, start_y=8)
    scanword_instance.get_question(position=(3, 9), num_elements=6, direction='vertical',
                      question="Царь \nада",
                      answer='сатана',
                      start_x=4, start_y=9)
    scanword_instance.get_question(position=(6, 8), num_elements=3, direction='vertical',
                      question="Какую\n реку\n назвали\n Танаис?",
                      answer='дон',
                      start_x=7, start_y=8)