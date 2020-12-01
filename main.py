# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets, QtChart, QtTest
import sys
import sqlite3
from source import resource1
import random
from dialog6 import train_end_dialog
import transliterate
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 700)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 700))
        MainWindow.setMaximumSize(QtCore.QSize(2400, 1400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1200, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.topbar = QtWidgets.QFrame(self.centralwidget)
        self.topbar.setMaximumSize(QtCore.QSize(10000, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        self.topbar.setFont(font)
        self.topbar.setStyleSheet("background-color: rgb(253, 150, 59);")
        self.topbar.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topbar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar.setObjectName("topbar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.topbar)
        self.horizontalLayout.setContentsMargins(2, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.topbar_left = QtWidgets.QFrame(self.topbar)
        self.topbar_left.setMinimumSize(QtCore.QSize(120, 40))
        self.topbar_left.setMaximumSize(QtCore.QSize(80, 10000))
        self.topbar_left.setStyleSheet("background-color: rgb(233, 112, 38);")
        self.topbar_left.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.topbar_left.setFrameShadow(QtWidgets.QFrame.Plain)
        self.topbar_left.setObjectName("topbar_left")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.topbar_left)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.menu_btn = QtWidgets.QPushButton(self.topbar_left)
        self.menu_btn.setMinimumSize(QtCore.QSize(80, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        self.menu_btn.setFont(font)
        self.menu_btn.setStyleSheet(" QPushButton {\n"
                                    "    background-color: rgb(223, 110, 30);\n"
                                    " }\n"
                                    " QPushButton:hover {\n"
                                    "     background-color: rgb(255, 209, 9);\n"
                                    " }")
        self.menu_btn.setObjectName("menu_btn")
        self.verticalLayout_2.addWidget(self.menu_btn)
        self.horizontalLayout.addWidget(self.topbar_left, 0, QtCore.Qt.AlignLeft)
        self.topbar_right = QtWidgets.QFrame(self.topbar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.topbar_right.sizePolicy().hasHeightForWidth())
        self.topbar_right.setSizePolicy(sizePolicy)
        self.topbar_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.topbar_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.topbar_right.setObjectName("topbar_right")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.topbar_right)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.name_of_page_label = QtWidgets.QLabel(self.topbar_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name_of_page_label.sizePolicy().hasHeightForWidth())
        self.name_of_page_label.setSizePolicy(sizePolicy)
        self.name_of_page_label.setMinimumSize(QtCore.QSize(0, 0))
        self.name_of_page_label.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name_of_page_label.setFont(font)
        self.name_of_page_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_of_page_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_of_page_label.setObjectName("name_of_page_label")
        self.horizontalLayout_3.addWidget(self.name_of_page_label)
        self.horizontalLayout.addWidget(self.topbar_right)
        self.verticalLayout.addWidget(self.topbar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.content.sizePolicy().hasHeightForWidth())
        self.content.setSizePolicy(sizePolicy)
        self.content.setMinimumSize(QtCore.QSize(80, 100))
        self.content.setMaximumSize(QtCore.QSize(10000, 10000))
        self.content.setStyleSheet("background-color: rgb(254, 255, 255);")
        self.content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Plain)
        self.content.setLineWidth(0)
        self.content.setMidLineWidth(0)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.left_line_frame = QtWidgets.QFrame(self.content)
        self.left_line_frame.setMinimumSize(QtCore.QSize(120, 0))
        self.left_line_frame.setMaximumSize(QtCore.QSize(120, 16777215))
        self.left_line_frame.setStyleSheet(
            "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(253, 119, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.left_line_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.left_line_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_line_frame.setObjectName("left_line_frame")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.left_line_frame)
        self.verticalLayout_8.setContentsMargins(10, 0, 10, 10000)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.menu_frame_2 = QtWidgets.QFrame(self.left_line_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menu_frame_2.sizePolicy().hasHeightForWidth())
        self.menu_frame_2.setSizePolicy(sizePolicy)
        self.menu_frame_2.setMinimumSize(QtCore.QSize(0, 300))
        self.menu_frame_2.setMaximumSize(QtCore.QSize(200, 400))
        self.menu_frame_2.setSizeIncrement(QtCore.QSize(0, 0))
        self.menu_frame_2.setBaseSize(QtCore.QSize(0, 0))
        self.menu_frame_2.setStyleSheet("background-color: rgb(253, 150, 59);")
        self.menu_frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.menu_frame_2.setLineWidth(0)
        self.menu_frame_2.setObjectName("menu_frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.menu_frame_2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.start_menu_btn = QtWidgets.QPushButton(self.menu_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_menu_btn.sizePolicy().hasHeightForWidth())
        self.start_menu_btn.setSizePolicy(sizePolicy)
        self.start_menu_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        self.start_menu_btn.setFont(font)
        self.start_menu_btn.setStyleSheet("QPushButton {\n"
                                          "    background-color: rgb(255, 246, 47);\n"
                                          "    border: 0px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(250, 255, 111);\n"
                                          "}")
        self.start_menu_btn.setObjectName("start_menu_btn")
        self.verticalLayout_5.addWidget(self.start_menu_btn)
        self.train_menu_btn = QtWidgets.QPushButton(self.menu_frame_2)
        self.train_menu_btn.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.train_menu_btn.sizePolicy().hasHeightForWidth())
        self.train_menu_btn.setSizePolicy(sizePolicy)
        self.train_menu_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        self.train_menu_btn.setFont(font)
        self.train_menu_btn.setStyleSheet("QPushButton {\n"
                                          "    background-color: rgb(255, 246, 47);\n"
                                          "    border: 0px;\n"
                                          "}\n"
                                          "\n"
                                          "QPushButton:hover {\n"
                                          "    background-color: rgb(250, 255, 111);\n"
                                          "}")
        self.train_menu_btn.setObjectName("train_menu_btn")
        self.verticalLayout_5.addWidget(self.train_menu_btn)
        self.addtest_menu_btn = QtWidgets.QPushButton(self.menu_frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addtest_menu_btn.sizePolicy().hasHeightForWidth())
        self.addtest_menu_btn.setSizePolicy(sizePolicy)
        self.addtest_menu_btn.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        self.addtest_menu_btn.setFont(font)
        self.addtest_menu_btn.setStyleSheet("QPushButton {\n"
                                            "    background-color: rgb(255, 246, 47);\n"
                                            "    border: 0px;\n"
                                            "}\n"
                                            "\n"
                                            "QPushButton:hover {\n"
                                            "    background-color: rgb(250, 255, 111);\n"
                                            "}")
        self.addtest_menu_btn.setObjectName("addtest_menu_btn")
        self.verticalLayout_5.addWidget(self.addtest_menu_btn)
        self.verticalLayout_8.addWidget(self.menu_frame_2)
        self.horizontalLayout_2.addWidget(self.left_line_frame)
        self.main_frame = QtWidgets.QFrame(self.content)
        self.main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.main_frame)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_frame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.start_page = QtWidgets.QWidget()
        self.start_page.setObjectName("start_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.start_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.start_page_text = QtWidgets.QTextBrowser(self.start_page)
        self.start_page_text.setMaximumSize(QtCore.QSize(16777215, 170))
        self.start_page_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.start_page_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.start_page_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.start_page_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.start_page_text.setObjectName("start_page_text")
        self.verticalLayout_3.addWidget(self.start_page_text)
        self.start_btns_frame = QtWidgets.QFrame(self.start_page)
        self.start_btns_frame.setMinimumSize(QtCore.QSize(0, 475))
        self.start_btns_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.start_btns_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.start_btns_frame.setLineWidth(0)
        self.start_btns_frame.setObjectName("start_btns_frame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.start_btns_frame)
        self.horizontalLayout_5.setContentsMargins(100, -1, 100, 0)
        self.horizontalLayout_5.setSpacing(100)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.train_btn = QtWidgets.QPushButton(self.start_btns_frame)
        self.train_btn.setMinimumSize(QtCore.QSize(0, 200))
        self.train_btn.setStyleSheet("QPushButton {\n"
                                     "    border: 0px;\n"
                                     "    image: url(:/start_page/lamp_off.png);\n"
                                     "}\n"
                                     "\n"
                                     "QPushButton:hover {\n"
                                     "    image: url(:/start_page/lamp_on.png);\n"
                                     "}")
        self.train_btn.setText("")
        self.train_btn.setObjectName("train_btn")
        self.horizontalLayout_5.addWidget(self.train_btn)
        self.verticalLayout_3.addWidget(self.start_btns_frame)
        self.stackedWidget.addWidget(self.start_page)
        self.choose_mode_page = QtWidgets.QWidget()
        self.choose_mode_page.setObjectName("choose_mode_page")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.choose_mode_page)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.choose_mode_text = QtWidgets.QTextEdit(self.choose_mode_page)
        self.choose_mode_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.choose_mode_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.choose_mode_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.choose_mode_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.choose_mode_text.setObjectName("choose_mode_text")
        self.verticalLayout_4.addWidget(self.choose_mode_text)
        self.choose_mode_frame = QtWidgets.QFrame(self.choose_mode_page)
        self.choose_mode_frame.setMinimumSize(QtCore.QSize(0, 550))
        self.choose_mode_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.choose_mode_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.choose_mode_frame.setObjectName("choose_mode_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.choose_mode_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 100)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.custom_test_frame = QtWidgets.QFrame(self.choose_mode_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custom_test_frame.sizePolicy().hasHeightForWidth())
        self.custom_test_frame.setSizePolicy(sizePolicy)
        self.custom_test_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.custom_test_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.custom_test_frame.setObjectName("custom_test_frame")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.custom_test_frame)
        self.verticalLayout_13.setContentsMargins(300, 0, 300, 0)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.your_tests_text = QtWidgets.QLabel(self.custom_test_frame)
        self.your_tests_text.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.your_tests_text.setFont(font)
        self.your_tests_text.setAlignment(QtCore.Qt.AlignCenter)
        self.your_tests_text.setObjectName("your_tests_text")
        self.verticalLayout_13.addWidget(self.your_tests_text)
        self.custom_tests_combobox = QtWidgets.QComboBox(self.custom_test_frame)
        self.custom_tests_combobox.setMinimumSize(QtCore.QSize(400, 0))
        self.custom_tests_combobox.setMaximumSize(QtCore.QSize(1000000, 16777215))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(18)
        self.custom_tests_combobox.setFont(font)
        self.custom_tests_combobox.setObjectName("custom_tests_combobox")
        self.verticalLayout_13.addWidget(self.custom_tests_combobox)
        self.label_2 = QtWidgets.QLabel(self.custom_test_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_13.addWidget(self.label_2)
        self.count_answers_combobox = QtWidgets.QComboBox(self.custom_test_frame)
        self.count_answers_combobox.setMinimumSize(QtCore.QSize(0, 23))
        self.count_answers_combobox.setObjectName("count_answers_combobox")
        self.count_answers_combobox.addItem("")
        self.count_answers_combobox.addItem("")
        self.verticalLayout_13.addWidget(self.count_answers_combobox)
        self.start_custom_test_btn = QtWidgets.QPushButton(self.custom_test_frame)
        self.start_custom_test_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.start_custom_test_btn.setFont(font)
        self.start_custom_test_btn.setStyleSheet("QPushButton {\n"
                                                 "    border: 0px;\n"
                                                 "    background-color: rgb(253, 150, 59);\n"
                                                 "\n"
                                                 "}\n"
                                                 "QPushButton:hover {\n"
                                                 "    \n"
                                                 "    background-color: rgb(245, 255, 60);\n"
                                                 "}")
        self.start_custom_test_btn.setObjectName("start_custom_test_btn")
        self.verticalLayout_13.addWidget(self.start_custom_test_btn)
        self.verticalLayout_6.addWidget(self.custom_test_frame)
        self.verticalLayout_4.addWidget(self.choose_mode_frame)
        self.stackedWidget.addWidget(self.choose_mode_page)
        self.udarenia_training_page = QtWidgets.QWidget()
        self.udarenia_training_page.setObjectName("udarenia_training_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.udarenia_training_page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.top_frame = QtWidgets.QFrame(self.udarenia_training_page)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.top_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.top_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.task_text = QtWidgets.QTextEdit(self.top_frame)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        self.task_text.setFont(font)
        self.task_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.task_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.task_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.task_text.setAutoFormatting(QtWidgets.QTextEdit.AutoNone)
        self.task_text.setTabChangesFocus(False)
        self.task_text.setReadOnly(True)
        self.task_text.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.task_text.setObjectName("task_text")
        self.horizontalLayout_6.addWidget(self.task_text)
        self.verticalLayout_7.addWidget(self.top_frame)
        self.right_false_frame = QtWidgets.QFrame(self.udarenia_training_page)
        self.right_false_frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.right_false_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.right_false_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_false_frame.setObjectName("right_false_frame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.right_false_frame)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.answer_text = QtWidgets.QTextEdit(self.right_false_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.answer_text.sizePolicy().hasHeightForWidth())
        self.answer_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        self.answer_text.setFont(font)
        self.answer_text.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.answer_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.answer_text.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.answer_text.setReadOnly(True)
        self.answer_text.setObjectName("answer_text")
        self.horizontalLayout_7.addWidget(self.answer_text)
        self.verticalLayout_7.addWidget(self.right_false_frame)
        self.central_frame = QtWidgets.QFrame(self.udarenia_training_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.central_frame.sizePolicy().hasHeightForWidth())
        self.central_frame.setSizePolicy(sizePolicy)
        self.central_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.central_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.central_frame.setObjectName("central_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.central_frame)
        self.gridLayout.setContentsMargins(50, 0, 50, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.right_btn = QtWidgets.QPushButton(self.central_frame)
        self.right_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("PT Sans Narrow")
        font.setPointSize(20)
        self.right_btn.setFont(font)
        self.right_btn.setStyleSheet("QPushButton {\n"
                                     "    border: 0px;\n"
                                     "    background-color: rgb(253, 150, 59);\n"
                                     "\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    \n"
                                     "    background-color: rgb(245, 255, 60);\n"
                                     "}")
        self.right_btn.setObjectName("right_btn")
        self.gridLayout.addWidget(self.right_btn, 0, 1, 1, 1)
        self.left_btn = QtWidgets.QPushButton(self.central_frame)
        self.left_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("PT Sans Narrow")
        font.setPointSize(20)
        self.left_btn.setFont(font)
        self.left_btn.setStyleSheet("QPushButton {\n"
                                    "    border: 0px;\n"
                                    "    background-color: rgb(253, 150, 59);\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(245, 255, 60);\n"
                                    "}")
        self.left_btn.setObjectName("left_btn")
        self.gridLayout.addWidget(self.left_btn, 0, 0, 1, 1)
        self.left_d_btn = QtWidgets.QPushButton(self.central_frame)
        self.left_d_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("PT Sans Narrow")
        font.setPointSize(20)
        self.left_d_btn.setFont(font)
        self.left_d_btn.setStyleSheet("QPushButton {\n"
                                      "    border: 0px;\n"
                                      "    background-color: rgb(253, 150, 59);\n"
                                      "\n"
                                      "}\n"
                                      "QPushButton:hover {\n"
                                      "    \n"
                                      "    background-color: rgb(245, 255, 60);\n"
                                      "}")
        self.left_d_btn.setObjectName("left_d_btn")
        self.gridLayout.addWidget(self.left_d_btn, 1, 0, 1, 1)
        self.right_d_btn = QtWidgets.QPushButton(self.central_frame)
        self.right_d_btn.setEnabled(True)
        self.right_d_btn.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setFamily("PT Sans Narrow")
        font.setPointSize(20)
        self.right_d_btn.setFont(font)
        self.right_d_btn.setStyleSheet("QPushButton {\n"
                                       "    border: 0px;\n"
                                       "    background-color: rgb(253, 150, 59);\n"
                                       "\n"
                                       "}\n"
                                       "QPushButton:hover {\n"
                                       "    \n"
                                       "    background-color: rgb(245, 255, 60);\n"
                                       "}")
        self.right_d_btn.setObjectName("right_d_btn")
        self.gridLayout.addWidget(self.right_d_btn, 1, 1, 1, 1)
        self.verticalLayout_7.addWidget(self.central_frame)
        self.bottom_frame = QtWidgets.QFrame(self.udarenia_training_page)
        self.bottom_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.bottom_frame.setMaximumSize(QtCore.QSize(16777215, 400))
        self.bottom_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_frame.setObjectName("bottom_frame")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.bottom_frame)
        self.verticalLayout_9.setContentsMargins(0, 15, 0, 70)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.next_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.next_btn.setMinimumSize(QtCore.QSize(200, 75))
        self.next_btn.setMaximumSize(QtCore.QSize(1000000, 16777215))
        font = QtGui.QFont()
        font.setFamily("PT Sans Narrow")
        font.setPointSize(22)
        self.next_btn.setFont(font)
        self.next_btn.setStyleSheet("QPushButton {\n"
                                    "    border: 0px;\n"
                                    "    background-color: rgb(253, 150, 59);\n"
                                    "\n"
                                    "}\n"
                                    "QPushButton:hover {\n"
                                    "    \n"
                                    "    background-color: rgb(245, 255, 60);\n"
                                    "}")
        self.next_btn.setObjectName("next_btn")
        self.verticalLayout_9.addWidget(self.next_btn)
        self.end_btn = QtWidgets.QPushButton(self.bottom_frame)
        self.end_btn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("PT Sans Narrow")
        font.setPointSize(20)
        self.end_btn.setFont(font)
        self.end_btn.setStyleSheet("QPushButton {\n"
                                   "    border: 0px;\n"
                                   "    background-color: rgb(252, 27, 24);\n"
                                   "\n"
                                   "}\n"
                                   "QPushButton:hover {\n"
                                   "    background-color: rgb(245, 255, 60);\n"
                                   "}")
        self.end_btn.setObjectName("end_btn")
        self.verticalLayout_9.addWidget(self.end_btn)
        self.verticalLayout_7.addWidget(self.bottom_frame, 0, QtCore.Qt.AlignHCenter)
        self.bottom_udareniya_frame = QtWidgets.QFrame(self.udarenia_training_page)
        self.bottom_udareniya_frame.setMaximumSize(QtCore.QSize(16777215, 75))
        self.bottom_udareniya_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.bottom_udareniya_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bottom_udareniya_frame.setObjectName("bottom_udareniya_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.bottom_udareniya_frame)
        self.horizontalLayout_9.setContentsMargins(10, 0, 10, 3)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.timer = QtWidgets.QTimeEdit(self.bottom_udareniya_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.timer.sizePolicy().hasHeightForWidth())
        self.timer.setSizePolicy(sizePolicy)
        self.timer.setMinimumSize(QtCore.QSize(0, 30))
        self.timer.setMaximumSize(QtCore.QSize(100, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.timer.setFont(font)
        self.timer.setStyleSheet("border: 0px;")
        self.timer.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.timer.setReadOnly(True)
        self.timer.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.timer.setAccelerated(False)
        self.timer.setKeyboardTracking(False)
        self.timer.setObjectName("timer")
        self.horizontalLayout_9.addWidget(self.timer, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.counter = QtWidgets.QLabel(self.bottom_udareniya_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.counter.sizePolicy().hasHeightForWidth())
        self.counter.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(19)
        self.counter.setFont(font)
        self.counter.setObjectName("counter")
        self.horizontalLayout_9.addWidget(self.counter, 0, QtCore.Qt.AlignRight | QtCore.Qt.AlignBottom)
        self.verticalLayout_7.addWidget(self.bottom_udareniya_frame)
        self.stackedWidget.addWidget(self.udarenia_training_page)
        self.add_test_page = QtWidgets.QWidget()
        self.add_test_page.setObjectName("add_test_page")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.add_test_page)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.add_list_left_frame = QtWidgets.QFrame(self.add_test_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_list_left_frame.sizePolicy().hasHeightForWidth())
        self.add_list_left_frame.setSizePolicy(sizePolicy)
        self.add_list_left_frame.setMinimumSize(QtCore.QSize(0, 0))
        self.add_list_left_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.add_list_left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_list_left_frame.setObjectName("add_list_left_frame")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.add_list_left_frame)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.add_test_tablewidget = QtWidgets.QTableWidget(self.add_list_left_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_test_tablewidget.sizePolicy().hasHeightForWidth())
        self.add_test_tablewidget.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(15)
        self.add_test_tablewidget.setFont(font)
        self.add_test_tablewidget.setLineWidth(1)
        self.add_test_tablewidget.setMidLineWidth(1)
        self.add_test_tablewidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.add_test_tablewidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.add_test_tablewidget.setGridStyle(QtCore.Qt.SolidLine)
        self.add_test_tablewidget.setObjectName("add_test_tablewidget")
        self.add_test_tablewidget.setColumnCount(2)
        self.add_test_tablewidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.add_test_tablewidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("PT Mono")
        item.setFont(font)
        self.add_test_tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.add_test_tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        item.setFont(font)
        self.add_test_tablewidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.add_test_tablewidget.setItem(0, 1, item)
        self.add_test_tablewidget.horizontalHeader().setVisible(False)
        self.add_test_tablewidget.horizontalHeader().setCascadingSectionResizes(True)
        self.add_test_tablewidget.horizontalHeader().setDefaultSectionSize(100)
        self.add_test_tablewidget.horizontalHeader().setHighlightSections(True)
        self.add_test_tablewidget.horizontalHeader().setMinimumSectionSize(30)
        self.add_test_tablewidget.horizontalHeader().setSortIndicatorShown(False)
        self.add_test_tablewidget.horizontalHeader().setStretchLastSection(True)
        self.add_test_tablewidget.verticalHeader().setVisible(False)
        self.add_test_tablewidget.verticalHeader().setCascadingSectionResizes(False)
        self.add_test_tablewidget.verticalHeader().setMinimumSectionSize(20)
        self.add_test_tablewidget.verticalHeader().setSortIndicatorShown(False)
        self.add_test_tablewidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_11.addWidget(self.add_test_tablewidget)
        self.add_question_btn = QtWidgets.QPushButton(self.add_list_left_frame)
        self.add_question_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(18)
        self.add_question_btn.setFont(font)
        self.add_question_btn.setStyleSheet("QPushButton {\n"
                                            "    border: 0px;\n"
                                            "    background-color: rgb(253, 150, 59);\n"
                                            "\n"
                                            "}\n"
                                            "QPushButton:hover {\n"
                                            "    \n"
                                            "    background-color: rgb(245, 255, 60);\n"
                                            "}")
        self.add_question_btn.setObjectName("add_question_btn")
        self.verticalLayout_11.addWidget(self.add_question_btn)
        self.delete_question_btn = QtWidgets.QPushButton(self.add_list_left_frame)
        self.delete_question_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(18)
        self.delete_question_btn.setFont(font)
        self.delete_question_btn.setStyleSheet("QPushButton {\n"
                                               "    border: 0px;\n"
                                               "    background-color: rgb(255, 0, 0);\n"
                                               "\n"
                                               "}\n"
                                               "QPushButton:hover {\n"
                                               "    \n"
                                               "    background-color: rgb(245, 255, 60);\n"
                                               "}")
        self.delete_question_btn.setObjectName("delete_question_btn")
        self.verticalLayout_11.addWidget(self.delete_question_btn)
        self.horizontalLayout_8.addWidget(self.add_list_left_frame)
        self.add_list_right_frame = QtWidgets.QFrame(self.add_test_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_list_right_frame.sizePolicy().hasHeightForWidth())
        self.add_list_right_frame.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(19)
        self.add_list_right_frame.setFont(font)
        self.add_list_right_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.add_list_right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.add_list_right_frame.setObjectName("add_list_right_frame")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.add_list_right_frame)
        self.verticalLayout_12.setContentsMargins(0, 180, 30, 180)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.add_list_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.add_list_right_frame)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_12.addWidget(self.comboBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem)
        self.test_name_text = QtWidgets.QLabel(self.add_list_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_name_text.sizePolicy().hasHeightForWidth())
        self.test_name_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(21)
        self.test_name_text.setFont(font)
        self.test_name_text.setAlignment(QtCore.Qt.AlignCenter)
        self.test_name_text.setObjectName("test_name_text")
        self.verticalLayout_12.addWidget(self.test_name_text)
        self.test_name_lineedit = QtWidgets.QLineEdit(self.add_list_right_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.test_name_lineedit.sizePolicy().hasHeightForWidth())
        self.test_name_lineedit.setSizePolicy(sizePolicy)
        self.test_name_lineedit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(16)
        self.test_name_lineedit.setFont(font)
        self.test_name_lineedit.setMaxLength(40)
        self.test_name_lineedit.setObjectName("test_name_lineedit")
        self.verticalLayout_12.addWidget(self.test_name_lineedit)
        self.create_test_btn = QtWidgets.QPushButton(self.add_list_right_frame)
        self.create_test_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.create_test_btn.setFont(font)
        self.create_test_btn.setStyleSheet("QPushButton {\n"
                                           "    border: 0px;\n"
                                           "    background-color: rgb(253, 150, 59);\n"
                                           "\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    \n"
                                           "    background-color: rgb(245, 255, 60);\n"
                                           "}")
        self.create_test_btn.setObjectName("create_test_btn")
        self.verticalLayout_12.addWidget(self.create_test_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_12.addItem(spacerItem1)
        self.delete_test_btn = QtWidgets.QPushButton(self.add_list_right_frame)
        self.delete_test_btn.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("PT Sans")
        font.setPointSize(20)
        self.delete_test_btn.setFont(font)
        self.delete_test_btn.setStyleSheet("QPushButton {\n"
                                           "    border: 0px;\n"
                                           "    background-color: rgb(255, 0, 0);\n"
                                           "\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    \n"
                                           "    background-color: rgb(245, 255, 60);\n"
                                           "}")
        self.delete_test_btn.setObjectName("delete_test_btn")
        self.verticalLayout_12.addWidget(self.delete_test_btn)
        self.horizontalLayout_8.addWidget(self.add_list_right_frame)
        self.stackedWidget.addWidget(self.add_test_page)
        self.horizontalLayout_4.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.main_frame)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ударный заряд ударений"))
        self.menu_btn.setText(_translate("MainWindow", "Меню"))
        self.name_of_page_label.setText(_translate("MainWindow", "Начальный экран   "))
        self.start_menu_btn.setText(_translate("MainWindow", "Начальная\n"
                                                             "страница🔄"))
        self.train_menu_btn.setText(_translate("MainWindow", "Тренировка\n"
                                                             "🏋"))
        self.addtest_menu_btn.setText(_translate("MainWindow", "Добавить\n"
                                                               " или изменить\n"
                                                               "тест‍💻 "))
        self.start_page_text.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Добро пожаловать в ULTests!</span></p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Это приложение поможет вам закрепить знания с помощью тестов.</span></p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Для создания своего первого теста используйте кнопку &quot;Добавить тест&quot; в левом верхнем меню.</span></p>\n"
                                                "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Приятного пользования!</span></p></body></html>"))
        self.choose_mode_text.setHtml(_translate("MainWindow",
                                                 "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                 "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                 "p, li { white-space: pre-wrap; }\n"
                                                 "</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                 "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                 "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Добро пожаловать в режим тренировки!</span></p>\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Здесь вы сможете подготовиться к тесту, решая бесконечно повторяющиеся задания.</span></p>\n"
                                                 "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Чтобы начать тренировку, выберите тему.</span></p></body></html>"))
        self.your_tests_text.setText(_translate("MainWindow", "Ваши тесты"))
        self.label_2.setText(_translate("MainWindow", "Количество вариантов ответов"))
        self.count_answers_combobox.setItemText(0, _translate("MainWindow", "2"))
        self.count_answers_combobox.setItemText(1, _translate("MainWindow", "4"))
        self.start_custom_test_btn.setText(_translate("MainWindow", "Начать"))
        self.task_text.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                          "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                          "p, li { white-space: pre-wrap; }\n"
                                          "</style></head><body style=\" font-family:\'PT Sans\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                          "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
                                          "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:24pt;\">Выберите правильное ударениеfdnsfhjldshlfdsjlkfds;fdsjfdsjfsdlfjldsjfldfjlsdjfjdsfjdsjklfdsklfjsdkfjldsjfjdslfjdsljfkdsfksdjflsfdfdsfdsf</span></p></body></html>"))
        self.answer_text.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'PT Sans\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'.AppleSystemUIFont\';\"><br /></p>\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'.AppleSystemUIFont\'; font-size:36pt; color:#25ff06;\">Верно!</span></p></body></html>"))
        self.right_btn.setText(_translate("MainWindow", "PushButton"))
        self.left_btn.setText(_translate("MainWindow", "name"))
        self.left_d_btn.setText(_translate("MainWindow", "PushButton"))
        self.right_d_btn.setText(_translate("MainWindow", "PushButton"))
        self.next_btn.setText(_translate("MainWindow", "Следующее"))
        self.end_btn.setText(_translate("MainWindow", "Закончить"))
        self.timer.setDisplayFormat(_translate("MainWindow", "hh:mm:ss"))
        self.counter.setText(_translate("MainWindow", "name"))
        self.add_test_tablewidget.setSortingEnabled(False)
        item = self.add_test_tablewidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.add_test_tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Вопрос"))
        item = self.add_test_tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Правильный ответ"))
        __sortingEnabled = self.add_test_tablewidget.isSortingEnabled()
        self.add_test_tablewidget.setSortingEnabled(False)
        self.add_test_tablewidget.setSortingEnabled(__sortingEnabled)
        self.add_question_btn.setText(_translate("MainWindow", "Добавить строку для вопроса"))
        self.delete_question_btn.setText(_translate("MainWindow", "Удалить строку"))
        self.label.setText(_translate("MainWindow", "Выберите существующий тест для редактирования\n"
                                                    "или создайте новый"))
        self.test_name_text.setText(_translate("MainWindow", "Название теста"))
        self.create_test_btn.setText(_translate("MainWindow", "Создать тест"))
        self.delete_test_btn.setText(_translate("MainWindow", "Удалить тест"))


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

        def create_animation_percentage(dialog, percent):
            """анимирует проценты (эффект увеличения)"""

            def set_percentage():
                """меняет процент"""
                self.i += 1
                print(self.i)

            timeline = QtCore.QTimeLine(percent * 75, dialog.percent_text)
            timeline.setFrameRange(1, percent)
            timeline.frameChanged.connect(set_percentage)
            dialog.percent_text.setText("0 %")
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
        create_chart(percent)
        # создаем диаграмму

        create_animation_percentage(dialog, percent)
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
