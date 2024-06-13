from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
GRID_SIZE = (11, 14)
default_le_style = """
           QLineEdit {
               margin: 1px;
               padding: 20px;
               background-color: white;
               font-size: 10px;
               font-weight: bold;
               color: #555;
               border: 1px solid #ddd;
               border-radius: 5px;
           }
           QLineEdit:read-only {
               background-color: #f0f0f0;
           }
       """
def setup_hard(scanword_instance):
    for i in range(GRID_SIZE[0]):
        row = []
        for j in range(GRID_SIZE[1]):
            boxedit = QLineEdit()
            boxedit.setFixedSize(75, 75)
            boxedit.setAlignment(Qt.AlignmentFlag.AlignCenter)
            boxedit.setReadOnly(True)
            boxedit.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            boxedit.setMaxLength(1)
            boxedit.setStyleSheet(default_le_style)
            scanword_instance.grid_layout.addWidget(boxedit, i, j)
            row.append(boxedit)
        scanword_instance.boxedits.append(row)
    scanword_instance.get_question(position=(0, 0), num_elements=6, direction='vertical',
                                   question="Ряса\n кар-\nдинала",
                                   answer='сутана',
                                   start_x=0, start_y=1)
    scanword_instance.get_question(position=(0, 2), num_elements=4, direction='vertical',
                                   question="Нем\n как\n ...",
                                   answer='рыба',
                                   start_x=0, start_y=3)
    scanword_instance.get_question(position=(0, 4), num_elements=8, direction='vertical',
                                   question="Офор-\n митель\n торта",
                                   answer='кондитер',
                                   start_x=1, start_y=4)
    scanword_instance.get_question(position=(0, 6), num_elements=4, direction='vertical',
                                   question="Косичка-\n от\n булочника",
                                   answer='хала',
                                   start_x=0, start_y=5)
    scanword_instance.get_question(position=(0, 7), num_elements=5, direction='vertical',
                                   question="Крупный\n мужской\n монастырь",
                                   answer='лавра',
                                   start_x=1, start_y=7)
    scanword_instance.get_question(position=(0, 9), num_elements=5, direction='vertical',
                                   question="Испол-\nнение\n арии",
                                   answer='пение',
                                   start_x=0, start_y=8)
    scanword_instance.get_question(position=(0, 11), num_elements=5, direction='vertical',
                                   question="Вид\n фрис-\nтайла",
                                   answer='могул',
                                   start_x=0, start_y=10)
    scanword_instance.get_question(position=(0, 12), num_elements=11, direction='vertical',
                                   question="Вскрытие\n ломиком",
                                   answer='взламывание',
                                   start_x=0, start_y=13)
    scanword_instance.get_question(position=(2, 9), num_elements=4, direction='vertical',
                                   question="Прос-\n тенький\n плуг",
                                   answer='рало',
                                   start_x=3, start_y=9)
    scanword_instance.get_question(position=(3, 12), num_elements=8, direction='vertical',
                                   question="Искусст-\n венный\n утепли-\nтель",
                                   answer='синтепон',
                                   start_x=3, start_y=11)
    scanword_instance.get_question(position=(3, 12), num_elements=8, direction='vertical',
                                   question="Искусст-\n венный\n утепли-\nтель",
                                   answer='синтепон',
                                   start_x=3, start_y=11)
    scanword_instance.get_question(position=(5, 12), num_elements=5, direction='vertical',
                                   question="Перевязь-\n дракона",
                                   answer='орарь',
                                   start_x=6, start_y=12)
    scanword_instance.get_question(position=(5, 10), num_elements=5, direction='vertical',
                                   question="Денежный\n расчет\n к проекту",
                                   answer='платёж',
                                   start_x=6, start_y=10)
    scanword_instance.get_question(position=(5, 8), num_elements=5, direction='vertical',
                                   question="Трава в\n меню\n карпов",
                                   answer='ряска',
                                   start_x=6, start_y=8)
    scanword_instance.get_question(position=(5, 6), num_elements=5, direction='vertical',
                                   question="Избав-\n ление от\n денег",
                                   answer='ряска',
                                   start_x=6, start_y=6)
    scanword_instance.get_question(position=(4, 5), num_elements=6, direction='vertical',
                                   question="Нитки\n хирурга",
                                   answer='кетгут',
                                   start_x=5, start_y=5)
    scanword_instance.get_question(position=(4, 3), num_elements=6, direction='vertical',
                                   question="Город на\n берегах\n Волги",
                                   answer='самара',
                                   start_x=5, start_y=3)
    scanword_instance.get_question(position=(4, 2), num_elements=6, direction='vertical',
                                   question="Отбитый\n кусок\n камня",
                                   answer='сколок',
                                   start_x=5, start_y=2)
    scanword_instance.get_question(position=(2, 0), num_elements=6, direction='horizontal',
                                   question="Любовь\n меломана",
                                   answer='музыка',
                                   start_x=1, start_y=0)
    scanword_instance.get_question(position=(1, 6), num_elements=7, direction='horizontal',
                                   question="Защита\n моста",
                                   answer='ледорез',
                                   start_x=1, start_y=7)
    scanword_instance.get_question(position=(2, 2), num_elements=6, direction='horizontal',
                                   question="Природа\n его умом\n обделила",
                                   answer='болван',
                                   start_x=2, start_y=3)
    scanword_instance.get_question(position=(3, 6), num_elements=5, direction='horizontal',
                                   question="Компью-\n терный\n вреди-\nтель",
                                   answer='вирус',
                                   start_x=3, start_y=7)
    scanword_instance.get_question(position=(4, 6), num_elements=7, direction='horizontal',
                                   question="Трезвая\n оценка\n действи-\nтельности",
                                   answer='реализм',
                                   start_x=4, start_y=7)
    scanword_instance.get_question(position=(4, 0), num_elements=6, direction='horizontal',
                                   question="Самурай-\nский меч",
                                   answer='катана',
                                   start_x=3, start_y=0)
    scanword_instance.get_question(position=(6, 0), num_elements=6, direction='horizontal',
                                   question="Резинка в\nмагнито-\n фоне",
                                   answer='бобина',
                                   start_x=5, start_y=0)
    scanword_instance.get_question(position=(6, 1), num_elements=5, direction='horizontal',
                                   question="Приль-\nнувший к\n гипоте-\nнузе",
                                   answer='катет',
                                   start_x=6, start_y=2)
    scanword_instance.get_question(position=(6, 7), num_elements=6, direction='horizontal',
                                   question="...-на-\nДону",
                                   answer='ростов',
                                   start_x=6, start_y=8)
    scanword_instance.get_question(position=(7, 9), num_elements=4, direction='horizontal',
                                   question="Граница",
                                   answer='межа',
                                   start_x=7, start_y=10)
    scanword_instance.get_question(position=(9, 9), num_elements=4, direction='horizontal',
                                   question="Оппоннен-\nты вигов",
                                   answer='тори',
                                   start_x=9, start_y=10)
    scanword_instance.get_question(position=(8, 7), num_elements=6, direction='horizontal',
                                   question="Старший\nсын Го-\nловлева",
                                   answer='степан',
                                   start_x=8, start_y=8)
    scanword_instance.get_question(position=(10, 7), num_elements=6, direction='horizontal',
                                   question="Вздохи от\n досады",
                                   answer='оханье',
                                   start_x=10, start_y=8)
    scanword_instance.get_question(position=(9, 4), num_elements=4, direction='horizontal',
                                   question="Ткацкий\n термин",
                                   answer='нить',
                                   start_x=9, start_y=5)
    scanword_instance.get_question(position=(8, 0), num_elements=9, direction='horizontal',
                                   question="Школь-\n ный урок",
                                   answer='острастка',
                                   start_x=7, start_y=0)
    scanword_instance.get_question(position=(8, 1), num_elements=5, direction='horizontal',
                                   question="Тюлень в\n Охотском\n море",
                                   answer='ларга',
                                   start_x=8, start_y=2)
    scanword_instance.get_question(position=(10, 0), num_elements=4, direction='horizontal',
                                   question="Ледяной\n рисунок\n на окне",
                                   answer='узор',
                                   start_x=9, start_y=0)
    scanword_instance.get_question(position=(10, 1), num_elements=5, direction='horizontal',
                                   question="Полити-\nческая ...\n мира",
                                   answer='карта',
                                   start_x=10, start_y=2)