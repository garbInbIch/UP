from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys, random


default_le_style = """
           QLineEdit {
               margin: 1px;
               padding: 20px;
               background-color: white;
               font-size: 40px;
               font-weight: bold;
               color: #555;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           QLineEdit:read-only {
               background-color: #f0f0f0;
           }
       """


class Scanwords(QMainWindow):
    def __init__(self):
        # Конструктор класса, инициализация главного окна игры.
        # Здесь устанавливаются начальные параметры окна, такие как название, размер, иконка и др.
        super().__init__()
        self.title = 'Сканворды'  # Заголовок главного окна
        self.left = 0  # Координата X левого верхнего угла окна
        self.top = 0  # Координата Y левого верхнего угла окна
        self.width = 1450  # Ширина главного окна
        self.height = 800  # Высота главного окна
        self.icon = ""  # Путь к иконке окна (пустой, значит иконка отсутствует)
        self.boxedits = []  # Список для хранения полей ввода ячеек игроского поля
        self.initUI()  # Вызов метода, который инициализирует графический интерфейс

    def initUI(self):
        # Задаем название окна
        self.setWindowTitle(self.title)

        # Устанавливаем иконку для окна
        self.setWindowIcon(QIcon(self.icon))

        # Задаем начальные размеры и позицию окна
        self.setGeometry(0, 0, self.width, self.height)

        # Создаем центральный виджет для главного окна
        central_widget = QWidget()

        # Настраиваем меню в верхней части окна
        # Создаем меню сложности с тремя уровнями и назначаем им обработчик событий (self.dad)
        menu_bar = self.menuBar()
        levels_menu = menu_bar.addMenu("Сложность")
        levels_menu4 = levels_menu.addAction(QIcon('d195ee82-no-bg-HD (carve.photos).png'), "1 уровень")
        levels_menu4.triggered.connect(self.dad)

        levels_menu5 = levels_menu.addAction(QIcon('2cbe48ba-no-bg-HD (carve.photos).png'), "2 уровень")
        levels_menu5.triggered.connect(self.dad)

        levels_menu6 = levels_menu.addAction(QIcon('5694a029-no-bg-HD (carve.photos).png'), "3 уровень")
        levels_menu6.triggered.connect(self.dad)

        # Настраиваем стили для элементов меню
        menu_bar.setStyleSheet("""
                    QMenuBar {
                        background-color: #2c3e50;
                        color: white;
                        font-weight:bold;
                        border: 1px solid #2c3e50;
                    }
                    QMenuBar::item {
                        background-color: #2c3e50;
                        color: white;
                        padding: 5px 15px;
                        margin: 0px;
                        border: none;
                    }
                    QMenuBar::item:selected { 
                        background-color: rgba(255,255,255,20%);
                    }
                    QMenuBar::item:pressed {
                        background-color: #34495e;
                    }
                    QMenu {
                        background-color: #fff;
                        color: #000;
                        border: 1px solid #2c3e50;
                        margin: 2px;
                    }
                    QMenu::item {
                        padding: 5px 30px;
                    }
                    QMenu::item:selected {
                        background-color: rgba(44, 62, 80, 80%);
                        color: white;
                    }
                    QMenu::item:pressed {
                        background-color: #34495e;
                        color: white;
                    }
                """)

        # Добавляем статус бар в нижнюю часть окна
        self.setStatusBar(QStatusBar(self))

        # Создаем горизонтальный слой для размещения виджетов в центральном виджете
        main_layout = QHBoxLayout(central_widget)

        # Создаем словарь для хранения вопросов и ответов
        self.questions_answers = {}

        # Дальше у процесс идет разбиение интерфейса на две части - левую и правую.

        # Настройки для левой части основного окна
        # Левая часть layout
        left_widget = QWidget()
        left_widget.setStyleSheet("""
            background-color: #fff;
        """)

        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0, 0, 0, 0)

        # Правая часть layout
        right_widget = QWidget()
        right_widget.setStyleSheet("""
            background-color: #f0f0f0;
        """)

        self.right_layout = QVBoxLayout(right_widget)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        # Добавление QLabel и QLineEdit для ввода слова
        self.right_label = QLabel("")
        self.right_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignCenter)
        self.right_label.setStyleSheet("""
            font-size: 24px;
            color: #333333;
            font-weight:bold;
            margin-bottom: 15px;
        """)

        self.right_layout.addWidget(self.right_label)
        right_widget.setStyleSheet("""
            background-color: #f0f0f0;
        """)

        right_line_edit = QLineEdit("Введите слово")
        right_line_edit.setStyleSheet("""
            font-size: 20px;
            padding: 10px;
            font-weight:bold;
            margin-bottom: 15px;
            border: 1px solid #cccccc;
            border-radius: 5px;
        """)
        self.right_layout.addWidget(right_line_edit)
        self.right_line_edit = right_line_edit
        self.right_line_edit.textChanged.connect(self.on_right_line_edit_text_changed)

        # Добавление матрицы кнопок в виджет
        self.matrix_widget = QWidget()
        self.matrix_layout = QGridLayout(self.matrix_widget)
        self.matrix_layout.setSpacing(0)
        self.matrix_widget.setStyleSheet("""
             background-color: #eaeaea;
             padding: 10px;
             border: 1px solid #ccc;
             border-radius: 5px;

         """)

        # Создание матрицы кнопок 4x4
        self.WordsBox = []
        for _ in range(3):
            self.WordsBox.append([])
        self.positions = []
        for i in range(3):
            for j in range(4):
                self.positions.append((i + 1, j + 1))
        self.array = ['a', 'б', 'в', 'г', 'д', 'е', 'a', 'б', 'в', 'г', 'д', 'е']
        self.generate_blocks(self.array)

        self.right_layout.addWidget(self.matrix_widget)  # Добавляем матрицу кнопок в правый layout

        grid_widget = QWidget()
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(0)
        grid_widget.setLayout(self.grid_layout)

        # Здесь проходит создание полей ввода QLineEdit для сканворда
        for i in range(10):
            # Каждая строка сканворда представлена списком полей ввода QLineEdit
            row = []
            for j in range(10):
                boxedit = QLineEdit()
                # Для каждого QLineEdit устанавливаются определенные параметры: размер, выравнивание,
                # ограничение по количеству символов и стилизация
                boxedit.setFixedSize(75, 75)
                boxedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
                boxedit.setReadOnly(True)
                boxedit.setMaxLength(1)
                boxedit.setStyleSheet(default_le_style)
                # Добавляем QLineEdit в сетку и в список
                self.grid_layout.addWidget(boxedit, i, j)
                row.append(boxedit)
            self.boxedits.append(row)

        # Добавляем grid_widget с полями ввода в левый слой интерфейса
        left_layout.addWidget(grid_widget)
        left_widget.setLayout(left_layout)

        # Добавляем левый и правый виджеты в основной слой интерфейса
        main_layout.addWidget(left_widget, 75)
        main_layout.addWidget(right_widget, 25)

        self.get_question(position=(0, 0), num_elements=5, direction='horizontal',
                          question="Рогач \n из\n Зодиака", answer='телец',
                          start_x=1, start_y=0)
        self.get_question(position=(2, 0), num_elements=5, direction='horizontal',
                          question="Время \n для\n смелого\n гулянья",
                          answer='досуг',
                          start_x=3, start_y=0)
        self.get_question(position=(9, 1), num_elements=4, direction='horizontal',
                          question="Цветок \nветров",
                          answer='пион',
                          start_x=8, start_y=0)
        self.get_question(position=(9, 3), num_elements=6, direction='horizontal',
                          question="Оперетта \nЛегара\n<<...\nулыбок>>",
                          answer='страна',
                          start_x=9, start_y=4)
        self.get_question(position=(8, 4), num_elements=5, direction='horizontal',
                          question="Звездный \n накопи-\nтель\n офицера",
                          answer='погон',
                          start_x=8, start_y=5)
        self.get_question(position=(7, 3), num_elements=6, direction='horizontal',
                          question="Раздра-\nжение \nна себя",
                          answer='досада',
                          start_x=7, start_y=4)
        self.get_question(position=(5, 3), num_elements=6, direction='horizontal',
                          question="Меди-\nцинская \nстекло-\nтара",
                          answer='ампула',
                          start_x=5, start_y=4)
        self.get_question(position=(3, 5), num_elements=5, direction='horizontal',
                          question="Поворот, \nкоторый \nзакла-\nдывают",
                          answer='вираж',
                          start_x=2, start_y=5)
        self.get_question(position=(1, 5), num_elements=5, direction='horizontal',
                          question="Суть \nрефе-\nрендума",
                          answer='опрос',
                          start_x=0, start_y=5)
        self.get_question(position=(4, 5), num_elements=4, direction='horizontal',
                          question="Травма,\nне для\n своего\n локтя",
                          answer='укус',
                          start_x=4, start_y=6)
        self.get_question(position=(7, 1), num_elements=5, direction='horizontal',
                          question="Птица\n ухарь и \nхохотун",
                          answer='филин',
                          start_x=6, start_y=0)
        self.get_question(position=(5, 1), num_elements=4, direction='horizontal',
                          question="Облег-\nчитель \n Буренок",
                          answer='дояр',
                          start_x=4, start_y=1)

        self.get_question(position=(0, 2), num_elements=5, direction='vertical',
                          question="Снасть \n на\n Золотую\n Рыбку",
                          answer='невод',
                          start_x=0, start_y=1)
        self.get_question(position=(4, 0), num_elements=5, direction='vertical',
                          question="Область \n влияния",
                          answer='сфера',
                          start_x=5, start_y=0)
        self.get_question(position=(2, 2), num_elements=7, direction='vertical',
                          question="Повод к \n греху",
                          answer='соблазн',
                          start_x=3, start_y=2)
        self.get_question(position=(6, 5), num_elements=3, direction='vertical',
                          question="'Пар-\nтийная'\n про-\nдажа",
                          answer='опт',
                          start_x=7, start_y=5)
        self.get_question(position=(6, 6), num_elements=3, direction='vertical',
                          question="Его из\n избы не\n выносят",
                          answer='мусор',
                          start_x=7, start_y=6)
        self.get_question(position=(3, 7), num_elements=6, direction='vertical',
                          question="Абрикос,\n давший \n себе за-\nсохнуть ",
                          answer='курага',
                          start_x=4, start_y=7)
        self.get_question(position=(0, 4), num_elements=5, direction='vertical',
                          question="Что у \nрыбки \nбыло \nзолотым?",
                          answer='чешуя',
                          start_x=0, start_y=3)
        self.get_question(position=(2, 4), num_elements=5, direction='vertical',
                          question="'Титул'\nбольших \nотелей",
                          answer='гранд',
                          start_x=3, start_y=4)
        self.get_question(position=(1, 7), num_elements=6, direction='vertical',
                          question="'Знал бы\n ...-жил\n бы в\n Сочи'",
                          answer='прикуп',
                          start_x=0, start_y=6)
        self.get_question(position=(1, 9), num_elements=6, direction='vertical',
                          question="Преду-\nпреди-\nтельный\n жрец",
                          answer='оракул',
                          start_x=0, start_y=8)
        self.get_question(position=(3, 9), num_elements=6, direction='vertical',
                          question="Царь \nада",
                          answer='сатана',
                          start_x=4, start_y=9)
        self.get_question(position=(6, 8), num_elements=3, direction='vertical',
                          question="Какую\n реку\n назвали\n Танаис?",
                          answer='дон',
                          start_x=7, start_y=8)

        left_layout.addWidget(left_widget)
        left_layout.setAlignment(grid_widget, Qt.AlignmentFlag.AlignCenter)
        # Добавление кнопки "Проверить слово"
        self.check_word_button = QPushButton("Проверить слово")
        self.check_word_button.setStyleSheet("""
                       QPushButton {
                           font-size: 20px;
                           color: white;
                           font-weight:bold;
                           background-color: #5cb85c;
                           padding: 10px;
                           border: none;
                           border-radius: 5px;
                           margin-top: 15px;
                           margin-bottom: 30px;
                       }
                       QPushButton:hover {
                           background-color: #4cae4c;
                       }
                   """)
        self.check_word_button.clicked.connect(self.dad)
        self.right_layout.addWidget(self.check_word_button)

        # Добавляем левую и правую части в основной layout
        main_layout.addWidget(left_widget, 75)
        main_layout.addWidget(right_widget, 25)
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("""
                   QWidget {
                       background-color: #f8f8f8;
                       border: none;
                   }
               """)
        # Верхний уровень лейаута
        left_layout.setContentsMargins(10, 10, 10, 10)
        left_layout.setSpacing(10)

        # Grid Widget стайлинг
        self.grid_layout.setContentsMargins(5, 5, 5, 5)
        self.grid_layout.setSpacing(5)
        grid_widget.setStyleSheet("""
                   background: #ffffff;   /* Белый цвет фона */
                   border-radius: 10px;   /* Скругление угловы */
                   box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* Тень вокруг виджета */
               """)

    def dad(self):
        # Этот метод вызывается, когда пользователь выбирает уровень сложности
        # из меню, или при нажатии на кнопку "Проверить слово".
        # Если активные позиции (ячейки для ввода ответа) выбраны,
        # метод собирает слово из ячеек и проверяет, верно ли оно.
        if self.active_position and self.active_direction and self.active_num_elements:
            start_x, start_y = self.active_position
            current_word = ''
            if self.active_direction == 'vertical':
                for i in range(self.active_num_elements):
                    current_edit = self.boxedits[start_x + i][start_y]
                    current_word += current_edit.text()
            elif self.active_direction == 'horizontal':
                for i in range(self.active_num_elements):
                    current_edit = self.boxedits[start_x][start_y + i]
                    current_word += current_edit.text()

            # Приверяем соответствует ли введенное слово верному ответу.
            question = next((q for q, a in self.questions_answers.items() if a == current_word.lower()), None)
            if question:
                self.check_word(question, start_x, start_y, self.active_num_elements, self.active_direction)
            else:
                QMessageBox.warning(self, 'Ошибка', 'Введенное слово неверно или не соответствует активному вопросу',
                                    QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self, 'Ошибка', 'Ничего не выбрано для проверки', QMessageBox.StandardButton.Ok)

    def get_question(self, position, num_elements, direction, question, answer, start_x, start_y):
        # Этот метод добавляет новый вопрос в игру, путем создания кнопки вопроса на игровом поле.
        # Затем пользователь может кликнуть на эту кнопку, чтобы активировать ряд ячеек для ввода ответа.
        self.questions_answers[question] = answer.lower()
        question_button = QPushButton(question)
        question_button.setStyleSheet("""
                    QPushButton {
                        font-size: 13px; 
                        color: white; 
                        font-weight: bold; 
                        background-color: #3498db; 
                        border-radius: 8px;
                        padding: 2px; 
                        border: none; 
                        min-width: 70px; 
                        min-height: 70px; 
                    }
                    QPushButton:hover {
                        background-color: #58b2dc; 
                    }
                    QPushButton:pressed {
                        background-color: #2980b9; 
                    }
                """)
        question_button.clicked.connect(
            lambda: self.activate_linked_edits(start_x, start_y, num_elements, direction, question, answer)
        )
        # position используется здесь для размещения кнопки
        self.grid_layout.addWidget(question_button, *position)

    def activate_linked_edits(self, start_x, start_y, num_elements, direction, question, answer):
        # Этот метод активирует связанные поля ввода на основе выбранного вопроса.
        # Поля ввода становятся доступными для изменения и меняют цвет для визуального выделения.
        self.reset_edits()
        activated_color = """
        background-color: lightblue;
        font-size:25px;
        font-weight: bold;
        
        """

        # Активируем ячейки, начиная с start_x и start_y
        self.current_word_edits = []
        if direction == 'vertical':
            for i in range(num_elements):
                current_edit = self.boxedits[start_x + i][start_y]
                current_edit.setReadOnly(False)
                current_edit.setStyleSheet(activated_color)
                self.current_word_edits.append(current_edit)
        elif direction == 'horizontal':
            for i in range(num_elements):
                current_edit = self.boxedits[start_x][start_y + i]
                current_edit.setReadOnly(False)
                current_edit.setStyleSheet(activated_color)
                self.current_word_edits.append(current_edit)
        # Устанавливаем первую ячейку как активное поле ввода
        if self.current_word_edits:
            self.current_edit = self.current_word_edits[0]
            self.current_edit.setFocus()
        # Сохраняем текущую активную позицию и направление для проверки слова.
        self.right_label.setText(question.replace('\n', '').replace('-', ''))
        self.generate_random_letters(answer)
        self.generate_random_letters(answer)
        self.active_position = (start_x, start_y)
        self.active_direction = direction
        self.active_num_elements = num_elements

    def check_word(self, question, start_x, start_y, num_elements, direction):
        # Эта функция проверяет, правильно ли пользователь ввел слово в сканворде.
        # Она собирает буквы из активированных полей ввода и сравнивает с правильным ответом.

        current_word = ''  # Переменная для хранения собранного слова

        # Стиль для поля ввода с правильным ответом
        correct_answer_style = """
            QLineEdit {
                background-color: #A9A9A9;
                color: #FFFFFF;
            }
        """

        # Определяем направление слова (вертикальное или горизонтальное)
        # и собираем текущее слово из полей ввода
        if direction == 'vertical':
            # Если слово вертикальное, собираем буквы сверху вниз
            for i in range(num_elements):
                current_edit = self.boxedits[start_x + i][start_y]
                current_word += current_edit.text()
        elif direction == 'horizontal':
            # Если слово горизонтальное, собираем буквы слева направо
            for i in range(num_elements):
                current_edit = self.boxedits[start_x][start_y + i]
                current_word += current_edit.text()

        # Получаем правильный ответ для сравнения с текущим словом
        correct_answer = self.questions_answers.get(question, '')
        # Сравниваем введенное слово в нижнем регистре с правильным ответом
        if current_word.lower() == correct_answer:
            # Если слово правильное, меняем стиль поля ввода и делаем его доступным только для чтения
            for edit in self.current_word_edits:
                edit.setStyleSheet(correct_answer_style)
                edit.setReadOnly(True)
            # Показываем информационное окно с сообщением об успехе
            QMessageBox.information(self, 'Успех', f'Правильно!', QMessageBox.StandardButton.Ok)
            self.reset_edits()  # Сбрасываем состояние полей ввода
        else:
            # Если слово неправильное, показываем предупреждающее сообщение
            QMessageBox.warning(self, 'Ошибка', f'Слово неверно!', QMessageBox.StandardButton.Ok)
            self.reset_edits()  # Сбрасываем состояние полей ввода

    def reset_edits(self):
        # Метод переводит все поля ввода в начальное состояние, делает их "только для чтения"
        # и возвращает их исходный стиль (как они были до начала ввода ответа).
        for row in self.boxedits:
            for boxedit in row:
                boxedit.setReadOnly(True)
                boxedit.setStyleSheet(default_le_style)

    def generate_random_letters(self, word):
        # Генерирует случайный набор букв для вариантов ответа в игре,
        # который соответствует длине представленного слова плюс случайные буквы для заполнения.
        letters_list = list(word)
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

        while len(letters_list) < 12:
            random_letter = random.choice(alphabet)
            letters_list.append(random_letter)

        random.shuffle(letters_list)

        for i in range(3):
            for j in range(4):
                if self.WordsBox[i]:
                    button = self.WordsBox[i].pop()
                    button.deleteLater()
        self.generate_blocks(letters_list)

    def generate_blocks(self, array):
        # Генерирует блоки с буквами на основе массива букв,
        # создавая кнопки с буквами для игрового поля.
        for i in range(3):
            for j in range(4):
                if self.WordsBox[i]:
                    button = self.WordsBox[i].pop()
                    button.deleteLater()

        # Создание новых кнопок
        for i, position in enumerate(self.positions):
            button = QPushButton(array[i].upper())
            # Устанавливаем связь кнопки с методом set_letter и передаем ей букву
            button.clicked.connect(lambda checked, letter=array[i]: self.set_letter(letter.upper()))
            self.matrix_layout.addWidget(button, *position)
            button.setMaximumHeight(70)
            button.setMaximumWidth(55)
            button.setStyleSheet("""
                QPushButton {
                    font-weight:bold;
                    font-size: 25px;
                    color: #555555;
                    border: 2px solid #cccccc;
                    border-radius: 10px;
                    background-color: white;
                }
                QPushButton:hover {
                    background-color: #e6e6e6;
                }
            """)
            self.WordsBox[position[0] - 1].append(button)

    def set_letter(self, letter):
        if self.current_edit and not self.current_edit.isReadOnly():
            # Вставляем букву в активный QLineEdit
            self.current_edit.setText(letter)
            # Определяем индекс следующей QLineEdit
            next_index = self.current_word_edits.index(self.current_edit) + 1
            if next_index < len(self.current_word_edits):
                # Перемещаем фокус на следующий QLineEdit
                self.current_edit = self.current_word_edits[next_index]
                self.current_edit.setFocus()
            else:
                # Если это последняя ячейка, снимаем фокус
                self.current_edit.clearFocus()
                self.current_edit = None

            # Обновляем содержимое QLineEdit в правой панели
            self.right_line_edit.setText(self.get_current_word())

    def get_current_word(self):
        # Собираем текущее слово из активных QLineEdit ячеек
        return ''.join(edit.text() for edit in self.current_word_edits if edit is not None)

    def on_right_line_edit_text_changed(self, text):
        for i, edit in enumerate(self.current_word_edits):
            if i < len(text):
                edit.setText(text[i])
            else:
                edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scanwords()
    ex.show()
    app.exec()
