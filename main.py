# from db import db
from config import Config
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow,  QShortcut
from PyQt5.QtGui import QKeySequence
from PyQt5.QtCore import QRect, QPropertyAnimation, Qt

from todo import TodoApp


config = Config()

# TODO: 

#---------------- UTILS
# код бд 
# кнопка задвигания около лэйбла
# кнопка смены стороны около лейбла
# анимация смены стороны
# создать файл screens
# анимации todo
# выдвинуть если окно становиться активным и задвинуто

# ---------------- STYLE 
# scrollbar and main buttons styles 
 

# ---------- CONFIG 
# add all colors to config


# app

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # base size
        self.offset = 1521

        # size
        self.rect = QRect(self.offset, 150, 400, 800)
        self.setGeometry(self.rect)


        # style
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet(f"background-color: {config.bg_color}; border: {config.border} solid {config.border_color};")

        #### main toggle shortcut
        self.shortcut = QShortcut(QKeySequence(config.toggle_key), self)
        self.shortcut.activated.connect(self.toggle)


        # logic 
        self.internal = TodoApp()
        self.internal.setMinimumWidth(350)
        self.setCentralWidget(self.internal)
        self.show()

        self.internal.add_from_db()


    def toggle(self):

        current_offset = self.pos().x()
        # set offset x
        if current_offset == 1521:
            self.offset = 1521 + 400
        else: 
            self.offset = 1521

        # animate 
        self.animation = QPropertyAnimation(self, b'geometry')
        self.animation.setDuration(200)
        self.animation.setStartValue(QRect(current_offset, 150, 400, 800))
        self.animation.setEndValue(QRect(self.offset, 150, 400, 800))
        self.animation.start()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    ####  working with screen parameters
    # screen = app.primaryScreen()
    # print(screen.size())

    # general style
    app.setStyle('Breeze')

    # app entry 
    ex = Window()


    sys.exit(app.exec_())




