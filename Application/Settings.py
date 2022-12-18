from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *


class Settings(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Settings")
        self.setWindowTitle("Settings")
        self.move(300, 300)
        self.resize(760, 572)
        self.setStyleSheet(
            '''
            background-color: rgb(73,93,120)
            '''
        )
        title = QLabel("Настройки",self)
        title.move(300,25)
        title.setFont(QFont("Times", 14, QFont.Bold))
        title.setStyleSheet('''color: rgb(255, 255, 255);''')
        title.adjustSize()

        label1 = QLabel("Всплывающие уведомления:",self)
        label1.resize(230,50)
        label1.move(25,225)
        label1.setFont(QFont("Times", 10))
        label1.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch1 = QCheckBox(self)
        switch1.resize(100, 50)
        switch1.move(275, 225)
        switch1.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch1.setStyleSheet('''
            QCheckBox::indicator:unchecked {
                image: url(./Application/polsoff.png);
            }
            QCheckBox::indicator:checked {
                image: url(./Application/polson.png);
            }
        ''')

        label2 = QLabel("Напоминания о разминке:", self)
        label2.resize(210, 50)
        label2.move(25, 300)
        label2.setFont(QFont("Times", 10))
        label2.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch2 = QCheckBox(self)
        switch2.resize(100, 50)
        switch2.move(275, 300)
        label2.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch2.setStyleSheet('''
                    QCheckBox::indicator:unchecked {
                        image: url(./Application/polsoff.png);
                    }
                    QCheckBox::indicator:checked {
                        image: url(./Application/polson.png);
                    }
                ''')

        label3 = QLabel("Расстояние от глаз\nдо экрана:", self)
        label3.resize(210, 50)
        label3.setFont(QFont("Times", 10))
        label3.move(25, 375)
        label3.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch3 = QCheckBox(self)
        switch3.resize(100, 50)
        switch3.move(275, 375)
        switch3.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch3.setStyleSheet('''
                            QCheckBox::indicator:unchecked {
                                image: url(./Application/polsoff.png);
                            }
                            QCheckBox::indicator:checked {
                                image: url(./Application/polson.png);
                            }
                        ''')

        label4 = QLabel("Определение усталости \nглаз:", self)
        label4.setStyleSheet('''color: rgb(255, 255, 255);''')
        label4.resize(200, 50)
        label4.move(25, 450)
        label4.setFont(QFont("Times", 10))
        switch4 = QCheckBox(self)
        switch4.resize(100, 50)
        switch4.move(275, 450)
        switch4.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch4.setStyleSheet('''
                                    QCheckBox::indicator:unchecked {
                                        image: url(./Application/polsoff.png);
                                    }
                                    QCheckBox::indicator:checked {
                                        image: url(./Application/polson.png);
                                    }
                                ''')

        label5 = QLabel("Аудио уведомления:", self)
        label5.resize(200, 50)
        label5.move(425, 225)
        label5.setFont(QFont("Times", 10))
        label5.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch5 = QCheckBox(self)
        switch5.resize(100, 50)
        switch5.move(650, 225)
        switch5.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch5.setStyleSheet('''
                                            QCheckBox::indicator:unchecked {
                                                image: url(./Application/polsoff.png);
                                            }
                                            QCheckBox::indicator:checked {
                                                image: url(./Application/polson.png);
                                            }
                                        ''')

        label6 = QLabel("Проверка сщуренности \nглаз:", self)
        label6.resize(200, 50)
        label6.move(425, 300)
        label6.setFont(QFont("Times", 10))
        label6.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch6 = QCheckBox(self)
        switch6.resize(100, 50)
        switch6.move(650, 300)
        switch6.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch6.setStyleSheet('''
                                                    QCheckBox::indicator:unchecked {
                                                        image: url(./Application/polsoff.png);
                                                    }
                                                    QCheckBox::indicator:checked {
                                                        image: url(./Application/polson.png);
                                                    }
                                                ''')

        label7 = QLabel("Определение осанки:", self)
        label7.resize(200, 50)
        label7.move(425, 375)
        label7.setFont(QFont("Times", 10))
        label7.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch7 = QCheckBox(self)
        switch7.resize(100, 50)
        switch7.move(650, 375)
        switch7.setStyleSheet('''color: rgb(255, 255, 255);''')
        switch7.setStyleSheet('''
                                                            QCheckBox::indicator:unchecked {
                                                                image: url(./Application/polsoff.png);
                                                            }
                                                            QCheckBox::indicator:checked {
                                                                image: url(./Application/polson.png);
                                                            }
                                                        ''')

        buttonback = QPushButton("Отмена",self)
        buttonback.resize(125,50)
        buttonback.move(415,475)
        buttonback.setFont(QFont("Times", 10))
        buttonback.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                                "QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        buttonto = QPushButton("Подтвердить", self)
        buttonto.resize(125, 50)
        buttonto.move(615, 475)
        buttonto.setFont(QFont("Times", 10))
        buttonto.setStyleSheet("QPushButton {background-color: rgb(51,122,183); color: White; border-radius: 4px;}"
                                 "QPushButton:pressed {background-color:rgb(31,101,163) ; }")

        slider = QSlider(Qt.Horizontal,self)
        slider.setValue(20)
        slider.move(50,100)
        slider.setRange(0, 4)
        slider.setPageStep(1)
        slider.resize(250,55)
        slider.setFocusPolicy(Qt.StrongFocus)
        slider.setStyleSheet('''
            QSlider::groove:horizontal {  
                height: 45px;
                margin: 0px;
                border-radius: 5px;
                background: #cccccc;
            }
            QSlider::handle:horizontal {
                background: #808080;
                width: 50px;
                margin: -5px 0; 
                border-radius: 5px;
            }
        ''')
        slider.setTickInterval(1)
        slider.setTickPosition(QSlider.TicksBothSides)


