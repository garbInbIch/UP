from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from easy_level import setup_easy, GRID_SIZE as EASY_GRID_SIZE
from medium_level import setup_medium, GRID_SIZE as MED_GRID_SIZE
from hard_level import setup_hard, GRID_SIZE as HARD_GRID_SIZE
import sys, random

default_le_style = """
           QLineEdit {
               margin: 1px;
               padding: 20px;
               background-color: white;
               font-size: 26px;
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
        super().__init__()
        self.title = 'Сканворды'
        self.left = 0
        self.top = 0
        self.width = 1650
        self.height = 800
        self.icon = ""
        self.boxedits = []
        self.now_levels = 1
        self.current_word_edits = []
        self.active_position = None
        self.current_word = ""
        self.question_buttons = {}
        self.grid_widget = None
        self.questions = []
        self.grid_size = (0, 0)

        self.initUI()

    def change_level(self, level_func, grid_size, level):
        self.clear_questions()
        self.adjust_grid_size(grid_size)
        self.central_label.hide()

        # Очистка предыдущей сетки
        while self.grid_layout.count():
            child = self.grid_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        self.grid_size = grid_size
        level_func(self)

        if level == 1:
            self.now_levels = 1
            self.set_large_image_at_position('images/1.jpg', 5, 4, 2, 2)
        elif level == 2:
            self.now_levels = 2
        else:
            self.now_levels = 3

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon(self.icon))
        self.setGeometry(0, 0, self.width, self.height)
        central_widget = QWidget()
        self.central_label = QLabel("Добро пожаловать в сканворды!\nВыберите уровень сложности в левом верхнем углу.")
        self.central_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.central_label.setStyleSheet("""
                QLabel {
                    font-size: 40px;
                    color: #333;
                    padding: 20px;
                }
            """)

        # Устанавливаем QLabel как центральный виджет QMainWindow

        menu_bar = self.menuBar()
        levels_menu = menu_bar.addMenu("Сложность")
        levels_menu4 = levels_menu.addAction(QIcon('images/1.png'), "1 уровень")
        levels_menu4.triggered.connect(lambda: self.change_level(setup_easy, EASY_GRID_SIZE, 1))

        levels_menu5 = levels_menu.addAction(QIcon('images/2.png'), "2 уровень")
        levels_menu5.triggered.connect(lambda: self.change_level(setup_medium, MED_GRID_SIZE, 2))

        levels_menu6 = levels_menu.addAction(QIcon('images/3.png'), "3 уровень")
        levels_menu6.triggered.connect(lambda: self.change_level(setup_hard, HARD_GRID_SIZE, 3))

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

        self.setStatusBar(QStatusBar(self))

        main_layout = QHBoxLayout(central_widget)

        self.questions_answers = {}
        left_widget = QWidget()
        left_widget.setStyleSheet("""
            background-color: #fff;
        """)

        left_layout = QVBoxLayout(left_widget)
        left_layout.addWidget(self.central_label)
        left_layout.setContentsMargins(0, 0, 0, 0)

        # Правая часть layout
        right_widget = QWidget()
        right_widget.setStyleSheet("""
            background-color: #f0f0f0;
        """)

        self.right_layout = QVBoxLayout(right_widget)
        self.right_layout.setContentsMargins(0, 0, 0, 0)

        exit_button = QPushButton("X")
        exit_button.setStyleSheet("""
            QPushButton {
                font-weight: bold;
                font-size: 16px;
                color: white;
                background-color: #e74c3c;
                border: none;
                border-radius: 15px;
                min-width: 30px;
                min-height: 30px;
                padding: 0;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        # Устанавливаем максимальный размер, чтобы она не занимала много места
        exit_button.setMaximumSize(30, 30)
        # Сигнал на закрытие приложения при нажатии
        exit_button.clicked.connect(self.close)

        # Добавляем кнопку выхода в правый верхний угол правого layout
        self.right_layout.addWidget(exit_button, alignment=Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignRight)
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
        right_line_edit.setFocusPolicy(Qt.FocusPolicy.NoFocus)  # Отключаем фокусировку на виджете
        right_line_edit.setStyleSheet("""
            font-size: 20px;
            padding: 10px;
            font-weight:bold;
            margin-bottom: 15px;
            border: 1px solid #cccccc;
            border-radius: 5px;
        """)
        delete_button = QPushButton("Удалить")
        delete_button.clicked.connect(self.delete_last_character)

        # Добавляем стили для кнопки
        delete_button.setStyleSheet("""
                  QPushButton {
                      font-size: 16px;
                      padding: 5px;
                      font-weight:bold;
                      background-color: #e74c3c;
                      color: white;
                      margin-bottom: 15px;
                      border: none;
                      border-radius: 5px;
                  }
                  QPushButton:hover {
                      background-color: #c0392b;
                  }
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

        self.WordsBox = []
        for _ in range(3):
            self.WordsBox.append([])
        self.positions = []
        for i in range(3):
            for j in range(4):
                self.positions.append((i + 1, j + 1))
        self.array = ['a', 'б', 'в', 'г', 'д', 'е', 'a', 'б', 'в', 'г', 'д', 'е']
        self.generate_blocks(self.array)

        self.right_layout.addWidget(self.matrix_widget)
        self.right_layout.addWidget(delete_button)

        # Правильный порядок
        self.grid_widget = QWidget()
        self.grid_layout = QGridLayout()
        self.grid_widget.setLayout(self.grid_layout)
        self.grid_layout.setSpacing(0)

        left_layout.addWidget(self.grid_widget)
        left_widget.setLayout(left_layout)

        main_layout.addWidget(left_widget, 75)
        main_layout.addWidget(right_widget, 25)

        left_layout.addWidget(left_widget)
        left_layout.setAlignment(self.grid_widget, Qt.AlignmentFlag.AlignCenter)
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

        main_layout.addWidget(left_widget, 75)
        main_layout.addWidget(right_widget, 25)
        self.setCentralWidget(central_widget)
        central_widget.setStyleSheet("""
                   QWidget {
                       background-color: #f8f8f8;
                       border: none;
                   }
               """)
        left_layout.setContentsMargins(10, 10, 10, 10)
        left_layout.setSpacing(10)

        self.grid_layout.setContentsMargins(5, 5, 5, 5)
        self.grid_layout.setSpacing(5)
        self.grid_widget.setStyleSheet("""
                   background: #ffffff; 
                   border-radius: 10px; 
                   box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
               """)

    def adjust_grid_size(self, new_grid_size):
        # Удаляем виджеты и очищаем сетку
        self.clear_layout(self.grid_layout)
        self.boxedits = []

    def set_large_image_at_position(self, image_path, start_row, start_column, row_span, column_span):
        # Пройти по всем ячейкам, которые займет изображение
        for i in range(row_span):
            for j in range(column_span):
                row = start_row + i
                column = start_column + j
                item = self.grid_layout.itemAtPosition(row, column)
                # Удалить существующий виджет из сетки и очистить ссылку в boxedits
                if item is not None:
                    widget_to_remove = item.widget()
                    if widget_to_remove is not None:
                        self.grid_layout.removeWidget(widget_to_remove)
                        widget_to_remove.deleteLater()
                    # Обновить массив boxedits
                    if 0 <= row < len(self.boxedits) and 0 <= column < len(self.boxedits[row]):
                        self.boxedits[row][column] = None

        # Загрузить изображение и добавить его на сетку
        label = QLabel()
        pixmap = QPixmap(image_path)
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Добавить QLabel с картинкой на сетку, объединив ячейки
        self.grid_layout.addWidget(label, start_row, start_column, row_span, column_span)

    def update_scanword(self):
        # Актуализация клеток сканворда в соответствии с `self.current_word`
        for i, edit in enumerate(self.current_word_edits):
            char = self.current_word[i] if i < len(self.current_word) else ''
            edit.setText(char.upper())  # Устанавливаем текст в каждой клетке

    def clear_questions(self):
        # Удалить все Button виджеты соответствующие вопросам
        for button in self.question_buttons.values():
            button.deleteLater()
        self.question_buttons.clear()

    def clear_layout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()

    def generate_blocks(self, letters_list):
        # Очистка старых кнопок
        for row_boxes in self.WordsBox:
            for button in row_boxes:
                if button is not None:  # Мы должны проверить, существует ли кнопка
                    button.deleteLater()

        # Переинициализация WordsBox
        self.WordsBox = [[None for _ in range(4)] for _ in range(3)]

        # Создание новых кнопок
        for i in range(3):
            for j in range(4):
                pos = i * 4 + j
                letter = letters_list[pos].upper()
                button = QPushButton(letter)
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
                self.matrix_layout.addWidget(button, i + 1, j + 1)
                button.clicked.connect(lambda checked, temp_letter=letter: self.set_letter(temp_letter))
                self.WordsBox[i][j] = button

    def dad(self):
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
        self.grid_layout.addWidget(question_button, *position)
        self.question_buttons[question] = question_button

    def activate_linked_edits(self, start_x, start_y, num_elements, direction, question, answer):
        self.current_word_edits = []
        self.right_line_edit.setText("")
        self.current_word = ''

        self.reset_edits()
        activated_color = """
        background-color: lightblue;
        font-size:25px;
        font-weight: bold;

        """

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

        # Сохраняем текущую активную позицию и направление для проверки слова.
        self.right_label.setText(question.replace('\n', '').replace('-', ''))
        self.generate_random_letters(answer)
        self.generate_random_letters(answer)
        self.active_position = (start_x, start_y)
        self.active_direction = direction
        self.active_num_elements = num_elements

    def check_all_answers(self):
        if all(not button.isEnabled() for button in self.question_buttons.values()):
            QMessageBox.information(self, 'Поздравляем!', 'Все слова отгаданы! Вы прошли сканворд!',
                                    QMessageBox.StandardButton.Ok)

    def check_word(self, question, start_x, start_y, num_elements, direction):
        self.current_word = ''

        correct_answer_style = """
            QLineEdit {
                background-color: #A9A9A9;
                color: #FFFFFF;
                font-size: 20px;
            }
        """

        if direction == 'vertical':
            for i in range(num_elements):
                current_edit = self.boxedits[start_x + i][start_y]
                self.current_word += current_edit.text()
        elif direction == 'horizontal':
            for i in range(num_elements):
                current_edit = self.boxedits[start_x][start_y + i]
                self.current_word += current_edit.text()

        correct_answer = self.questions_answers.get(question, '')
        if self.current_word.lower() == correct_answer:
            for edit in self.current_word_edits:
                edit.setStyleSheet(correct_answer_style)
                edit.setReadOnly(True)
            question_button = self.find_question_button(question)
            if question_button:
                question_button.setEnabled(False)
            QMessageBox.information(self, 'Успех', f'Правильно!', QMessageBox.StandardButton.Ok)
            self.reset_edits()
            self.check_all_answers()
        else:
            QMessageBox.warning(self, 'Ошибка', f'Слово неверно!', QMessageBox.StandardButton.Ok)
            self.reset_edits()

    def delete_last_character(self):
        cursor_pos = self.right_line_edit.cursorPosition()
        if cursor_pos > 0:  # Удаляем символ только если курсор находится не в начале строки
            # Учет позиции курсора для корректного удаления символов
            self.current_word = self.current_word[:cursor_pos - 1] + self.current_word[cursor_pos:]
            self.right_line_edit.setText(self.current_word)  # Обновляем текст в QLineEdit
            self.right_line_edit.setCursorPosition(cursor_pos - 1)  # Восстанавливаем позицию курсора
            self.update_scanword()  # Отражаем изменения в клетках сканворда

    def find_question_button(self, question_text):
        for question, button in self.question_buttons.items():
            if question == question_text:
                return button
        return None

    def reset_edits(self):
        for row in self.boxedits:
            for boxedit in row:
                if boxedit is not None and isinstance(boxedit, QLineEdit):
                    boxedit.setReadOnly(True)
                    boxedit.setStyleSheet(default_le_style)
                    boxedit.setFocusPolicy(Qt.FocusPolicy.NoFocus)

    def generate_random_letters(self, word):
        letters_list = list(word)
        alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

        while len(letters_list) < 12:
            random_letter = random.choice(alphabet)
            letters_list.append(random_letter)

        random.shuffle(letters_list)

        self.generate_blocks(letters_list)

    def set_letter(self, letter):
        cursor_pos = self.right_line_edit.cursorPosition()
        self.current_word = (self.current_word[:cursor_pos] + letter + self.current_word[cursor_pos:]).lower()
        self.right_line_edit.setText(self.current_word)
        self.update_scanword()

    def get_current_word(self):
        return ''.join(edit.text() for edit in self.current_word_edits if edit is not None)

    def on_right_line_edit_text_changed(self, text):
        self.current_word = text.lower()  # Обновляем текущее слово
        self.update_scanword()  # Переносим изменения в клетки сканворда


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Scanwords()
    ex.show()
    app.exec()
