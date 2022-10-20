# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceXIcVUg.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1040)
        # MainWindow.setStyleSheet(u"background: url(J:/Program_Development/Python/Python_Projects/Projects/Virtual_AI_Assistant/Mark_5/static/icons/WIN_20201220_09_30_38_Pro.jpg);")
        MainWindow.setStyleSheet(u"background: black; background-repeat: no-repeat")
        QFontDatabase.addApplicationFont("static/fonts/Orbitron/Orbitron-VariableFont_wght.ttf")
        self.centralwidget = QLabel(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.centralwidget.setStyleSheet(u"background: black; background-repeat: no-repeat")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setLayoutDirection(Qt.RightToLeft)
        self.background.setStyleSheet(u"background: url(J:/Program_Development/Python/Python_Projects/Projects/Virtual_AI_Assistant/Mark_5/static/icons/interface3.png);")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.title = QLabel(self.background)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(730, 10, 461, 31))
        self.title.setStyleSheet(u"background: none; color: rgb(255, 255, 255); font: 16pt \"Orbitron\";")
        self.title.setAlignment(Qt.AlignCenter)
        self.option_menu = QFrame(self.background)
        self.option_menu.setObjectName(u"option_menu")
        self.option_menu.setGeometry(QRect(1610, 190, 281, 701))
        self.option_menu.setStyleSheet(u"background:none;")
        self.option_menu.setFrameShape(QFrame.StyledPanel)
        self.option_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.option_menu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.option_1 = QLabel(self.option_menu)
        self.option_1.setObjectName(u"option_1")
        self.option_1.setStyleSheet(u"color: rgb(250, 223, 113); background: none; font: 16pt \"Orbitron\"; margin-top: 20px; margin-bottom: 20px; padding: 20px;")
        self.option_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.option_1)

        self.option_2 = QLabel(self.option_menu)
        self.option_2.setObjectName(u"option_2")
        self.option_2.setStyleSheet(u"color: rgb(250, 223, 113);  font: 16pt \"Orbitron\"; margin-top: 20px; margin-bottom: 20px; padding: 20px;")
        self.option_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.option_2)

        self.option_3 = QLabel(self.option_menu)
        self.option_3.setObjectName(u"option_3")
        self.option_3.setStyleSheet(u"color: rgb(250, 223, 113);  font: 16pt \"Orbitron\"; margin-top: 20px; margin-bottom: 20px; padding: 20px;")

        self.verticalLayout.addWidget(self.option_3)

        self.option_4 = QLabel(self.option_menu)
        self.option_4.setObjectName(u"option_4")
        self.option_4.setStyleSheet(u"color: rgb(250, 223, 113);  font: 16pt \"Orbitron\"; margin-top: 20px; margin-bottom: 20px; padding: 20px;")

        self.verticalLayout.addWidget(self.option_4)

        self.option_5 = QLabel(self.option_menu)
        self.option_5.setObjectName(u"option_5")
        self.option_5.setStyleSheet(u"color: rgb(250, 223, 113); font: 16pt \"Orbitron\"; margin-top: 20px; margin-bottom: 20px; padding: 20px;")

        self.verticalLayout.addWidget(self.option_5)

        self.ip_label = QLabel(self.background)
        self.ip_label.setObjectName(u"ip_label")
        self.ip_label.setGeometry(QRect(1120, 970, 271, 41))
        self.ip_label.setStyleSheet(u"background: none; color: rgb(255, 255, 255); font: 14pt \"Orbitron\";\n"
"")
        self.ip_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.command_menu = QFrame(self.background)
        self.command_menu.setObjectName(u"command_menu")
        self.command_menu.setGeometry(QRect(50, 225, 351, 421))
        self.command_menu.setStyleSheet(u"background: none;")
        self.command_menu.setFrameShape(QFrame.StyledPanel)
        self.command_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.command_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.command_title = QLabel(self.command_menu)
        self.command_title.setObjectName(u"command_title")
        self.command_title.setMinimumSize(QSize(50, 0))
        self.command_title.setStyleSheet(u"color: rgb(250, 223, 113); font: 16pt \"Orbitron\"; padding-left: 20px;")

        self.verticalLayout_2.addWidget(self.command_title)

        self.command_list = QListWidget(self.command_menu)
        self.command_list.setObjectName(u"command_list")
        self.command_list.setFixedSize(QSize(327, 360))
        self.command_list.setStyleSheet(u"QListWidget{background-color: rgba(34, 224, 239, 0); border: none; border-top-right-radius: 30px; color: rgb(255, 255, 255); font: 14pt \"Orbitron\"; text-align:left; padding: 20px;} QListWidget::item:selected{background: rgba(250, 223, 113, 100); border-left: 7px solid rgb(250, 223, 113); border-top: 2px solid rgb(250, 223, 113)} QListWidget::item{padding: 10px; padding-left: 10px; border-bottom: 2px solid rgb(250, 223, 113);}")
        self.command_list.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_2.addWidget(self.command_list)

        self.prompt_box = QFrame(self.background)
        self.prompt_box.setObjectName(u"prompt_box")
        self.prompt_box.setGeometry(QRect(570, 820, 800, 100))
        self.prompt_box.setStyleSheet(u"background: none; background-color:  rgba(250, 223, 113, 100); border: 5px solid rgb(250, 223, 113); border-radius: 20px;")
        self.prompt_box.setFrameShape(QFrame.StyledPanel)
        self.prompt_box.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.prompt_box)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.prompt_label = QLabel(self.prompt_box)
        self.prompt_label.setObjectName(u"prompt_label")
        self.prompt_label.setStyleSheet(u"background:none; border:none; color: rgb(255, 255, 255); font: 28pt \"Orbitron\";")
        self.prompt_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.prompt_label)

        self.progress_frame = QFrame(self.background)
        self.progress_frame.setObjectName(u"progress_frame")
        self.progress_frame.setGeometry(QRect(1350, 22, 428, 61))
        self.progress_frame.setStyleSheet(u"background:none;")
        self.progress_frame.setFrameShape(QFrame.StyledPanel)
        self.progress_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.progress_frame)
        self.gridLayout.setObjectName(u"gridLayout")

        self.cpu_progressBar = QProgressBar(self.progress_frame)
        self.cpu_progressBar.setObjectName(u"cpu_progressBar")
        self.cpu_progressBar.setStyleSheet(u"QProgressBar::chunk{background-color: rgb(18, 234, 108); border-radius:2px;} QProgressBar{border-radius:2px; background-color: rgba(18, 234, 108, 100); margin-left:20px;}\n"
"")
        self.cpu_progressBar.setFormat("")

        self.gridLayout.addWidget(self.cpu_progressBar, 1, 3, 1, 1)

        self.ram_progressBar = QProgressBar(self.progress_frame)
        self.ram_progressBar.setObjectName(u"ram_progressBar")
        self.ram_progressBar.setStyleSheet(u"QProgressBar::chunk{background-color: rgb(236, 77, 89); border-radius:2px;} QProgressBar{border-radius:2px; background-color: rgba(236, 77, 89, 100); margin-left:20px;}\n"
"")
        self.ram_progressBar.setFormat("")

        self.gridLayout.addWidget(self.ram_progressBar, 1, 2, 1, 1)

        self.cpu_label = QLabel(self.progress_frame)
        self.disk_progressBar = QProgressBar(self.progress_frame)
        self.disk_progressBar.setObjectName(u"ram_progressBar")
        self.disk_progressBar.setStyleSheet(u"QProgressBar::chunk{background-color: rgb(18, 234, 108); border-radius:2px;} QProgressBar{border-radius:2px; background-color: rgba(18, 234, 108, 100); margin-left:20px;}\n"
"")
        self.disk_progressBar.setFormat("")

        self.gridLayout.addWidget(self.disk_progressBar, 1, 1, 1, 1)
        self.cpu_label.setObjectName(u"cpu_label")
        self.cpu_label.setStyleSheet(u"color: rgb(250, 223, 113);  font: 8pt \"Orbitron\";")
        self.cpu_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.cpu_label, 0, 3, 1, 1)

        self.ram_label = QLabel(self.progress_frame)
        self.ram_label.setObjectName(u"ram_label")
        self.ram_label.setStyleSheet(u"color: rgb(250, 223, 113);  font: 8pt \"Orbitron\";")
        self.ram_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.ram_label, 0, 2, 1, 1)

        self.disk_label = QLabel(self.progress_frame)
        self.disk_label.setObjectName(u"disk_label")
        self.disk_label.setStyleSheet(u"color: rgb(250, 223, 113);  font: 8pt \"Orbitron\";")
        self.disk_label.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.disk_label, 0, 1, 1, 1)

        self.control_menu = QFrame(self.background)
        self.control_menu.setObjectName(u"control_menu")
        self.control_menu.setGeometry(QRect(119, 35, 461, 50))
        self.control_menu.setStyleSheet(u"background: none;")
        self.control_menu.setFrameShape(QFrame.StyledPanel)
        self.control_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.control_menu)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.settings_menu = QToolButton(self.control_menu)
        self.settings_menu.setObjectName(u"settings_menu")
        self.settings_menu.setMinimumSize(QSize(120, 30))
        self.settings_menu.setStyleSheet(u"QToolButton{background: rgba(34, 224, 239, 100); color: rgb(34, 224, 239); border-radius: 5px;  font: 8pt \"Orbitron\";}\n"
"QToolButton::hover{background: rgba(34, 224, 239, 200); color: rgb(250, 223, 113)}")

        self.horizontalLayout_2.addWidget(self.settings_menu)

        self.network_menu = QToolButton(self.control_menu)
        self.network_menu.setObjectName(u"network_menu")
        self.network_menu.setMinimumSize(QSize(120, 30))
        self.network_menu.setStyleSheet(u"QToolButton{background: rgba(34, 224, 239, 100); color: rgb(34, 224, 239); border-radius: 5px;  font: 8pt \"Orbitron\";}\n"
"QToolButton::hover{background: rgba(34, 224, 239, 200); color: rgb(250, 223, 113)}")

        self.horizontalLayout_2.addWidget(self.network_menu)

        self.home_menu = QToolButton(self.control_menu)
        self.home_menu.setObjectName(u"home_menu")
        self.home_menu.setMinimumSize(QSize(120, 30))
        self.home_menu.setStyleSheet(u"QToolButton{background: rgba(34, 224, 239, 100); color: rgb(34, 224, 239); border-radius: 5px;  font: 8pt \"Orbitron\";}\n"
"QToolButton::hover{background: rgba(34, 224, 239, 200); color: rgb(250, 223, 113)}")

        self.horizontalLayout_2.addWidget(self.home_menu)

        self.close_button = QToolButton(self.background)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(1620, 960, 60, 60))
        self.close_button.setStyleSheet(u"QToolButton{background: rgba(236, 77, 89, 230); border-radius: 30px; color: white; border: 10px solid rgba(236, 77, 89, 100); font-size: 20pt;}\n"
"QToolButton::hover{background: rgba(211, 52, 64, 230); border: 10px solid rgba(211, 52, 64, 100)}")
        self.close_button.setIconSize(QSize(1024, 1024))
        self.close_button.setPopupMode(QToolButton.DelayedPopup)
        self.close_button.setToolButtonStyle(Qt.ToolButtonFollowStyle)
        self.close_button.setAutoRaise(False)
        self.close_button.setArrowType(Qt.NoArrow)
        self.animated_label = QLabel(self.background)
        self.animated_label.setObjectName(u"animated_label")
        self.animated_label.setGeometry(QRect(1610, 215, 260, 100))
        self.animated_label.setStyleSheet(u"background: none; border-top: 5px solid rgb(34, 224, 239); border-right: 5px solid rgb(34, 224, 239); border-bottom: 5px solid rgb(34, 224, 239); border-top-right-radius: 10px; border-bottom-right-radius: 10px;")
        self.ping_label = QLabel(self.background)
        self.ping_label.setObjectName(u"ping_label")
        self.ping_label.setGeometry(QRect(1477, 1002, 60, 30))
        self.ping_label.setStyleSheet(u"background: none; color: rgb(255, 255, 255); font: 14pt \"Orbitron\";")
        self.ping_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText(QCoreApplication.translate("MainWindow", u"JESSICA MONITOR", None))
        self.option_1.setText(QCoreApplication.translate("MainWindow", u"1 | Input", None))
        self.option_2.setText(QCoreApplication.translate("MainWindow", u"2 | Process", None))
        self.option_3.setText(QCoreApplication.translate("MainWindow", u"3 | Output", None))
        self.option_4.setText(QCoreApplication.translate("MainWindow", u"4 | Control", None))
        self.option_5.setText(QCoreApplication.translate("MainWindow", u"5 | Settings", None))
        self.ip_label.setText(QCoreApplication.translate("MainWindow", u"0.0.0.0", None))
        self.command_title.setText(QCoreApplication.translate("MainWindow", u"MEMORY DATA", None))
        self.prompt_label.setText(QCoreApplication.translate("MainWindow", u"MSG PROMPT", None))
        self.cpu_label.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.ram_label.setText(QCoreApplication.translate("MainWindow", u"Memory", None))
        self.disk_label.setText(QCoreApplication.translate("MainWindow", u"Disk", None))
        self.home_menu.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.network_menu.setText(QCoreApplication.translate("MainWindow", u"NETWORK", None))
        self.settings_menu.setText(QCoreApplication.translate("MainWindow", u"SETTINGS", None))
        self.close_button.setText(QCoreApplication.translate("MainWindow", u"\u2715", None))
        self.animated_label.setText("")
        self.ping_label.setText(QCoreApplication.translate("MainWindow", u"999", None))
    # retranslateUi

