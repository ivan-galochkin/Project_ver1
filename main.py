# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart, QtTest
import sys
import sqlite3
from source import resource1
import random
from dialog6 import train_end_dialog
import transliterate
from PyQt5 import QtCore, QtGui, QtWidgets
from ui import Ui_MainWindow


class Ultest(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.stackedWidget.setCurrentIndex(0)
        # стиль кнопок для режима тренировки и не только (чтобы не копировать)
        self.default_btn_style = 'QPushButton {border: 0px;background-color: rgb(253, 150, 59);}' \
                                 'QPushButton:hover {background-color: rgb(245, 255, 60);}'
        # стили для правильной и неправильной кнопки
        self.green_btn = 'QPushButton {background-color: rgb(0, 255, 0); border: 0px;}'
        self.red_btn = 'QPushButton {background-color: rgb(255, 0, 0); border: 0px;}'
        # заранее подключаем бд
        self.connection = sqlite3.connect('ultest.db')
        self.cur = self.connection.cursor()
        # анимация менюшки
        self.animation = QtCore.QPropertyAnimation(self.menu_frame_2, b'minimumHeight')
        self.animation.setDuration(800)
        # подключаем кнопку меню в левом углу
        self.menu_btn.clicked.connect(self.clicked_menu)
        # подключаем кнопки стартовой страницы
        self.train_btn.clicked.connect(self.clicked_menu_btns)
        # подключаем кнопки менюшки
        self.start_menu_btn.clicked.connect(self.clicked_menu_btns)
        self.train_menu_btn.clicked.connect(self.clicked_menu_btns)
        self.addtest_menu_btn.clicked.connect(self.create_test_page_prepare)
        # подключаем кнопки со страницы, где предлагаются темы для тренировки
        # не забудем подключить эту же кнопку к подготовке задания по теме и к функции активации секундомера и счетчика
        # подключаем кнопки страницы тренировки (ударения)
        self.left_btn.clicked.connect(self.clicked_ans_btn_train)
        self.right_btn.clicked.connect(self.clicked_ans_btn_train)
        self.right_d_btn.clicked.connect(self.clicked_ans_btn_train)
        self.left_d_btn.clicked.connect(self.clicked_ans_btn_train)
        self.next_btn.clicked.connect(self.prepare_custom_train)
        self.end_btn.clicked.connect(self.finish_test)

        # список для хранения неправильных слов (выдаем в конце тренировки)
        self.fails = []
        # таймер
        self.timer_core = QtCore.QTimer()
        # количество пройденных заданий
        self.count_right = 0
        self.count_all = 0
        # переменная, которая помогает анимировать проценты в окне результатов
        self.i = 1
        # был ли ответ на вопрос (необходимо для подсчета процентов
        self.answered = False

        # Если False, то создается тест с двумя вариантами ответов, если true - 4
        self.option = False
        # списки для хранения вопросов и ответов на тест (перед добавлением в БД)
        self.questions = []
        self.answers = []
        self.names = []
        self.alert = QtWidgets.QMessageBox()

        self.add_question_btn.clicked.connect(self.add_row_clicked)
        self.delete_question_btn.clicked.connect(self.delete_row_clicked)
        self.create_test_btn.clicked.connect(self.create_edit_test_clicked)

        self.comboBox.currentTextChanged.connect(self.combobox_changed)

        self.delete_test_btn.clicked.connect(self.delete_test_clicked)
        self.start_custom_test_btn.clicked.connect(self.clicked_start_custom_train)

        self.add_test_tablewidget.itemChanged.connect(self.table_train_changed)

    def prepare_custom_train(self):
        """главная функция подготовки вопроса теста"""
        self.stackedWidget.setCurrentIndex(2)

        def create_with_two_btns(right_answer, table):
            """создает страницу с вопросом с двумя кнопками ответа"""
            self.right_d_btn.hide()
            self.left_d_btn.hide()
            self.counter.setText(f'{self.count_right}/{self.count_all}')

            false_answer = self.cur.execute(f"SELECT answer FROM {table} WHERE answer != ? ORDER BY RANDOM() LIMIT 1",
                                            (right_answer,)).fetchone()[0]
            if random.randint(0, 1):
                self.left_btn.setText(str(right_answer))
                self.correct_ans_udarenia = self.left_btn
                self.right_btn.setText(str(false_answer))
            else:
                self.right_btn.setText(str(right_answer))
                self.correct_ans_udarenia = self.right_btn
                self.left_btn.setText(str(false_answer))

        def create_with_four_btns(right_answer, table):
            """создает страницу с вопросом с четырьмя кнопками ответа"""
            self.right_d_btn.show()
            self.left_d_btn.show()

            self.counter.setText(f'{self.count_right}/{self.count_all}')

            false_answers = self.cur.execute(f"SELECT answer from {table} WHERE answer != ? ORDER BY RANDOM() LIMIT 3",
                                             (right_answer,)).fetchall()

            random_int = random.randint(1, 4)
            if random_int == 4:
                self.left_btn.setText(str(right_answer))
                self.correct_ans_udarenia = self.left_btn
                self.right_btn.setText(str(false_answers[0][0]))
                self.left_d_btn.setText(str(false_answers[1][0]))
                self.right_d_btn.setText(str(false_answers[2][0]))
            elif random_int == 3:
                self.right_btn.setText(str(right_answer))
                self.correct_ans_udarenia = self.right_btn
                self.left_btn.setText(str(false_answers[0][0]))
                self.left_d_btn.setText(str(false_answers[1][0]))
                self.right_d_btn.setText(str(false_answers[2][0]))
            elif random_int == 2:
                self.left_d_btn.setText(str(right_answer))
                self.correct_ans_udarenia = self.left_d_btn
                self.right_btn.setText(str(false_answers[0][0]))
                self.left_btn.setText(str(false_answers[1][0]))
                self.right_d_btn.setText(str(false_answers[2][0]))
            else:
                self.right_d_btn.setText(str(right_answer))
                self.correct_ans_udarenia = self.right_d_btn
                self.right_btn.setText(str(false_answers[0][0]))
                self.left_d_btn.setText(str(false_answers[1][0]))
                self.left_btn.setText(str(false_answers[2][0]))

        def to_default():
            """возваращает кнопкам на странице вопроса теста """
            self.right_btn.setDisabled(False)
            self.right_btn.setStyleSheet(self.default_btn_style)
            self.right_d_btn.setStyleSheet(self.default_btn_style)
            self.left_btn.setStyleSheet(self.default_btn_style)
            self.left_d_btn.setStyleSheet(self.default_btn_style)

            self.right_btn.blockSignals(False)
            self.right_d_btn.blockSignals(False)
            self.left_d_btn.blockSignals(False)
            self.left_btn.blockSignals(False)

            self.answer_text.setText('')

        to_default()

        table = self.current_table

        self.question, self.right_answer = \
            self.cur.execute(f"SELECT question, answer FROM {table} ORDER BY RANDOM() LIMIT 1").fetchall()[0]

        if self.option:
            self.count_all += 1
            create_with_four_btns(self.right_answer, table)
        else:
            self.count_all += 1
            create_with_two_btns(self.right_answer, table)
        self.task_text.setFontPointSize(19)
        self.task_text.setText(str(self.question))
        self.task_text.setAlignment(QtCore.Qt.AlignCenter)
        self.next_btn.blockSignals(True)

    def table_train_changed(self):
        """костыль для решения проблемы с невлезающим текстом в ячейку таблицы"""
        self.add_test_tablewidget.resizeColumnsToContents()

    def clicked_start_custom_train(self):
        """когда тыкнули начать тренировку, устанавливает тест с которым мы работаем, запускает функцию
        подготовки страницы с вопросом и функцию старта отсчета времени"""
        table = self.custom_tests_combobox.currentText()

        self.current_table = self.cur.execute('SELECT name_en FROM names WHERE name_ru = ?', (table,)).fetchone()[0]
        if self.count_answers_combobox.currentText() == '2':
            self.option = False
            self.train_started()
            self.prepare_custom_train()

        else:
            if len(self.cur.execute(f"SELECT * FROM {self.current_table}").fetchall()) < 4:
                self.alert.about(self, 'error', 'количество вопросов данного теста меньше 4!')
            else:
                self.option = True
                self.train_started()
                self.prepare_custom_train()

    def train_started(self):
        """активируется при начале теста, ставит секундомер и счетчик ответов на ноль"""
        # обнуляем счетчик
        self.count_all = 0
        self.count_right = 0
        self.i = 1
        # обнуляем время
        self.my_time = QtCore.QTime(00, 00, 00)

        # обнуляем срок Путина, стоп, что?

        def time():
            self.my_time = self.my_time.addSecs(1)
            self.timer.setTime(self.my_time)

        self.timer_core.timeout.connect(time)
        self.timer_core.start(1000)

        # вылючаем кнопки менюшки
        self.addtest_menu_btn.setDisabled(True)
        self.train_menu_btn.setDisabled(True)
        self.start_menu_btn.setDisabled(True)

    def clicked_menu(self):
        """анимирует менюшку, когда кликнули на кнопку"""
        height = self.menu_frame_2.height()
        if height == 0:
            start_height = 0
            finish_height = 300
        else:
            start_height = 300
            finish_height = 0

        self.animation.setStartValue(start_height)
        self.animation.setEndValue(finish_height)
        self.animation.start()

    def clicked_menu_btns(self):
        """переводит на нужную страницу, когда тыкнули на кнопку из менюшки"""
        sender = self.sender()
        if sender == self.train_menu_btn or sender == self.train_btn:
            self.stackedWidget.setCurrentIndex(1)
            self.name_of_page_label.setText('Тренировка')
            self.prepare_custom_tests_box()
        elif sender == self.start_menu_btn:
            self.stackedWidget.setCurrentIndex(0)
            self.name_of_page_label.setText('Начальная страница')
        elif sender == self.addtest_menu_btn:
            self.stackedWidget.setCurrentIndex(3)
            self.name_of_page_label.setText('Добавить тест')

    def clicked_train_page(self):
        """переводит на страницу с темой, на которую кликнули (со страницы выбора темы сhoose_mode_page)"""
        sender = self.sender()
        self.prepare_custom_tests_box()
        if sender == self.udarenia_choose_mode_btn:
            self.stackedWidget.setCurrentIndex(2)
        elif sender == self.start_custom_test_btn:
            self.stackedWidget.setCurrentIndex(2)

    def prepare_train(self, database, count='1'):
        """меняет задание в режиме тренировки"""
        # блокируем выход в меню, чтобы не было ошибок, оно разблокируется после конца тренировки
        if self.menu_frame_2.minimumHeight() != 0:
            self.clicked_menu()
        self.menu_btn.blockSignals(True)
        self.answer_text.setText('')
        data = list(self.cur.execute(f"SELECT correct, incorrect FROM {database} ORDER BY RANDOM() LIMIT 1"))

        self.name_of_page_label.setText('Тренировка')

        # рандомно выбирает положение правильного ответа (левая или правая кнопка)
        first_int = random.randint(0, 1)
        if first_int == 0:
            second_int = 1
        else:
            second_int = 0

        first_name = data[0][first_int]
        second_name = data[0][second_int]

        # делаем текст на кнопках в соответствии с словами
        self.left_btn.setText(first_name)
        self.right_btn.setText(second_name)

        # ставим дефолтный стиль
        self.left_btn.setStyleSheet(self.default_btn_style)
        self.right_btn.setStyleSheet(self.default_btn_style)

        # активируем кнопки
        self.left_btn.blockSignals(False)
        self.right_btn.blockSignals(False)

        # нам нужно знать, где все таки правильный ответ: на правой или левой кнопке
        # однако в таблице правильный ответ всегда первый (data[0][0])
        if self.left_btn.text() == data[0][0]:
            self.correct_ans_udarenia = self.left_btn
        else:
            self.correct_ans_udarenia = self.right_btn
        # еще не ответили на наш вопрос
        self.answered = False

    def clicked_ans_btn_train(self):
        """проверяет правильный ли ответ выбрали, меняет цвета кнопок и т.д."""
        sender = self.sender()
        self.next_btn.blockSignals(False)
        # меняем стили кнопок в соответствии с правильностью
        self.answer_text.setFontPointSize(25)
        self.answer_text.setAlignment(QtCore.Qt.AlignCenter)
        if sender == self.correct_ans_udarenia:
            self.count_right += 1
            self.counter.setText(f'{self.count_right}/{self.count_all}')
            sender.setStyleSheet(self.green_btn)
            self.answer_text.setStyleSheet('QTextEdit {color: rgb(0, 255, 0);}')
            self.answer_text.setText('Верно!')
            self.answer_text.show()
        else:
            sender.setStyleSheet(self.red_btn)
            self.correct_ans_udarenia.setStyleSheet(self.green_btn)
            self.answer_text.setStyleSheet('QTextEdit {color: rgb(255, 0, 0);}')
            self.answer_text.setText('Неверно!')
            self.fails.append((str(self.question), str(sender.text()), str(self.correct_ans_udarenia.text())))
            self.answer_text.show()

        self.answer_text.setAlignment(QtCore.Qt.AlignCenter)
        # чтобы не тыкали лишний раз на ответ :)
        self.left_btn.blockSignals(True)
        self.right_btn.blockSignals(True)
        self.left_d_btn.blockSignals(True)
        self.right_btn.blockSignals(True)
        self.end_btn.show()
        # ответили на вопрос
        self.answered = True

    def finish_test(self):
        """когда тыкнули завершить тест"""

        def create_chart(percent):
            """Создает диаграмму"""
            # ядро диаграммы
            series = QtChart.QPieSeries()
            series.append("Верные", percent)
            series.append('Неверные', 100 - percent)
            series.setPieSize(30)

            # анимация диаграммы
            chart = QtChart.QChart()
            chart.addSeries(series)
            chart.setAnimationOptions(QtChart.QChart.SeriesAnimations)
            chart.setAnimationDuration(3000)
            chart.setTitle('Соотношение ответов')

            # шрифт диаграммы
            font = QtGui.QFont()
            font.setFamily('PT Sans')
            font.setPointSize(18)
            chart.setFont(font)
            chart.setTitleFont(font)

            # виджет диаграммы
            chartview = QtChart.QChartView(chart)
            chartview.setRenderHint(QtGui.QPainter.Antialiasing)
            dialog.fails_table.setMinimumWidth(434)
            dialog.diagram_frame.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
            dialog.verticalLayout_7.addWidget(chartview)

        def create_animation_percentage(dialog2, percent):
            """анимирует проценты (эффект увеличения)"""

            def set_percentage():
                """меняет процент"""
                self.i += 1
                dialog2.percent_text.setText(f'{self.i} %')

            timeline = QtCore.QTimeLine(percent * 75, dialog2.percent_text)
            timeline.setFrameRange(0, percent)
            timeline.frameChanged.connect(set_percentage)
            dialog2.percent_text.setText("0 %")
            timeline.start()

        # если при завершении теста пользователь не успел ответить на вопрос, то мы отнимаем его
        if not self.answered:
            self.count_all -= 1
        self.timer_core.stop()
        self.timer_core.disconnect()
        # подготавливаем диалоговое окно к запуску (добавляем инфу)
        dialog = train_end_dialog()
        dialog.ok_btn.clicked.connect(dialog.close)
        # меняем цвет процентов в зависимости от значения
        if not self.count_all:
            self.count_all = 1
        percent = round(self.count_right / self.count_all * 100)
        if percent > 90:
            color = '{color: rgb(0, 255, 0);}'
        elif percent > 80:
            color = '{color rgb(109, 252, 0);}'
        elif percent > 65:
            color = '{color: rgb(212, 162, 0);}'
        else:
            color = '{color: rgb(255, 0, 0);}'
        dialog.percent_text.setStyleSheet(f"QLabel {color}")

        # чтобы не повторялись ошибки при их выводе в таблицу
        self.fails = set(self.fails)
        i = 0
        # добавляем информацию в таблицу
        for row in self.fails:
            first = QtWidgets.QTableWidgetItem(row[0])
            second = QtWidgets.QTableWidgetItem(row[1])
            third = QtWidgets.QTableWidgetItem(row[2])
            dialog.fails_table.insertRow(i)
            dialog.fails_table.setItem(i, 0, first)
            dialog.fails_table.setItem(i, 1, second)
            dialog.fails_table.setItem(i, 2, third)
            i += 1
        # adjust to content
        dialog.fails_table.resizeColumnsToContents()
        # анимируем проценты
        create_animation_percentage(dialog, percent)
        # создаем диаграмму
        create_chart(percent)
        # запускаем диалоговое окно
        dialog.exec()
        # переключаем на начальную страницу
        self.stackedWidget.setCurrentIndex(0)
        self.fails = []
        self.menu_btn.blockSignals(False)
        # ставим счетчик для процентов на начальное значение
        self.i = 1
        # меняем название
        self.name_of_page_label.setText('Начальная страница')

        self.count_all = 0
        self.count_right = 0
        # включаем кнопки менюшки
        self.addtest_menu_btn.setDisabled(False)
        self.train_menu_btn.setDisabled(False)
        self.start_menu_btn.setDisabled(False)

    def add_row_clicked(self):
        """добавляет строку в таблицу на странице создания теста"""
        self.add_test_tablewidget.insertRow(self.add_test_tablewidget.rowCount())

    def delete_row_clicked(self):
        """функция для удаления строк в таблице на странице создания теста"""
        if self.add_test_tablewidget.selectionModel().selectedIndexes():
            index = self.add_test_tablewidget.selectionModel().currentIndex().row()
            self.add_test_tablewidget.removeRow(index)
        else:
            self.add_test_tablewidget.removeRow(self.add_test_tablewidget.rowCount() - 1)

    def create_test_page_prepare(self):
        """когда тыкнули в меню создать или изменить тест подготавливает страницу"""
        self.stackedWidget.setCurrentIndex(3)
        self.prepare_combobox_test()
        self.comboBox.setCurrentIndex(0)

    def combobox_changed(self):
        """Заполняет таблицу с тестом, когда пользователь выбрал тест из выпадающего
        списка на странице создания"""
        if self.comboBox.currentText() != 'Новый тест':
            name = self.comboBox.currentText()
            self.test_name_lineedit.setText(name)
            self.create_test_btn.setText('Изменить тест')
            name_eng = self.cur.execute("SELECT name_en FROM names WHERE name_ru = ?", (name,)).fetchall()
            name_eng = name_eng[0][0]
            questions = self.cur.execute(f"SELECT question FROM {name_eng}").fetchall()
            answers = self.cur.execute(f'SELECT answer FROM {name_eng}').fetchall()
            self.add_test_tablewidget.setRowCount(0)
            for i in range(len(questions)):
                self.add_test_tablewidget.insertRow(i)
                self.add_test_tablewidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(questions[i][0])))
                self.add_test_tablewidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(answers[i][0])))
        else:
            self.add_test_tablewidget.setRowCount(0)
            self.add_test_tablewidget.insertRow(0)
            self.create_test_btn.setText('Создать тест')
            self.test_name_lineedit.setText('')

    def create_edit_test_clicked(self):
        """Когда пользователь тыкает кнопку создать или изменить тест
        на странице создания теста, определяет пользователь хочет создать или изменить тест
        запускает функцию создания теста"""
        if self.comboBox.currentText() == 'Новый тест':
            self.create_test()
        else:
            self.create_test(self.comboBox.currentText())

    def prepare_combobox_test(self):
        """подготавливает выпадающий список с именами тестов на страницу создания тестов"""
        self.comboBox.disconnect()
        self.comboBox.clear()
        pre_names = list(self.cur.execute('SELECT name_ru FROM names'))
        names = []
        for name in pre_names:
            names.append(str(name[0]))
        names.insert(0, 'Новый тест')
        self.comboBox.addItems(names)
        self.comboBox.currentTextChanged.connect(self.combobox_changed)
        self.comboBox.setCurrentIndex(0)

    def delete_test_clicked(self):
        """Меняет выпадающий список с тестами на странице создания теста"""
        name = self.test_name_lineedit.text()
        if name == "Новый тест":
            self.alert(self, 'error', 'невозможно удалить еще несозданный тест')
        else:
            name_en = str(self.cur.execute('SELECT name_en FROM names WHERE name_ru = ?', (name,)).fetchone()[0])
            self.cur.execute(f'DROP TABLE {name_en}')
            self.cur.execute(f'DELETE FROM names where name_en LIKE ?', (name_en,))
            self.prepare_combobox_test()
            self.comboBox.setCurrentIndex(0)
            self.test_name_lineedit.setText('')
            self.combobox_changed()

    def create_test(self, edit=False):
        name_ru = str(self.test_name_lineedit.text())
        if not name_ru:
            self.alert.about(self, 'Error', 'Название не может быть пустым!')
        else:
            name_eng = ''
            name = transliterate.translit(name_ru, 'ru', reversed=True)
            name = name.split()
            name = ''.join(name)
            for letter in name:
                if letter.isalnum():
                    name_eng += letter
            name_eng = 'table_' + name_eng
            pre_other_names = list(self.cur.execute('SELECT name_ru FROM names'))
            other_names = []
            for word in pre_other_names:
                other_names.append(word[0])
            if edit:
                try:
                    other_names.remove(name_ru)
                except ValueError:
                    pass
            if name_ru in other_names or name_ru == 'Новый тест':
                self.alert.about(self, 'Ошибка', 'Имя занято')
            else:
                questions = []
                answers = []
                try:
                    for i in range(self.add_test_tablewidget.rowCount()):
                        question = self.add_test_tablewidget.item(i, 0).text()
                        answer = self.add_test_tablewidget.item(i, 1).text()
                        if question.isspace() or not question:
                            raise EmptyItem
                        if answer.isspace() or not answer:
                            raise EmptyItem
                        questions.append(str(question))
                        answers.append(str(answer))
                    if len(questions) < 2:
                        self.alert.about(self, 'Error', "Длина теста не может быть меньше двух!")
                        return 1
                    if edit:
                        edit_eng = list(*self.cur.execute(f"SELECT name_en FROM names WHERE name_ru = ?", (edit,)))[0]
                        self.cur.execute(f'DROP TABLE {edit_eng}')
                        self.cur.execute('DELETE FROM names WHERE name_ru = ?', (edit,))
                    self.cur.execute('INSERT INTO names (name_en, name_ru) VALUES (?, ?)', (name_eng, name_ru))
                    self.connection.commit()
                    self.cur.execute(f"CREATE TABLE IF NOT EXISTS {name_eng} ("
                                     "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                                     "question STRING, "
                                     "answer STRING)")
                    self.connection.commit()
                    for i in range(len(questions)):
                        self.cur.execute(f"INSERT INTO {name_eng} (question, answer) VALUES (?, ?)",
                                         (questions[i], answers[i]))
                        self.connection.commit()
                    self.create_test_btn.setStyleSheet(self.green_btn)
                    self.create_test_btn.setText('Тест успешно создан!')
                    QtTest.QTest.qWait(1000)
                    self.create_test_btn.setText('Изменить тест')
                    self.create_test_btn.setStyleSheet(self.default_btn_style)
                    self.prepare_combobox_test()
                    self.combobox_changed()
                except (AttributeError, EmptyItem):
                    self.alert.about(self, 'Ошибка', 'Пустые ячейки в тесте недопустимы!')

    def prepare_custom_tests_box(self):
        """Подготавливает содержимое выпадающего списка с названиями тестов"""
        pre_names = list(self.cur.execute('SELECT name_ru FROM names'))
        names = []
        self.custom_tests_combobox.clear()
        for name in pre_names:
            names.append(str(name[0]))
        if not names:
            names = ['Пользовательских тестов нет, создайте их!']
        self.custom_tests_combobox.addItems(names)


class EmptyItem(BaseException):
    pass


class LowCountOfItems(BaseException):
    pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Ultest()
    window.show()
    app.exec_()
