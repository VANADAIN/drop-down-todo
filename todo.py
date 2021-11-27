from PyQt5.QtWidgets import   QWidget, QShortcut, QLabel, QVBoxLayout, QHBoxLayout, QScrollArea, QLineEdit, QPushButton, QListView
from PyQt5.QtGui import QKeySequence, QFont, QCursor, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

from config import Config
from db import Database

config = Config()
db = Database()

class TodoApp(QWidget):
    def __init__(self):
        super().__init__()

        # label
        label = QLabel("VanLaviva Todos | version: 0.1")
        label.setFont(QFont('Roboto', 14))
        label.setObjectName('name_and_version')
        label.setStyleSheet(f'border: 0px; color: white; padding-top: 8px; padding-left: 60px')

        # widget for scroll area CHNAGE TO ??
        self.todo_stack = QWidget()
        self.todo_stack.setFixedWidth(370)
        lay = QVBoxLayout()
        lay.setContentsMargins(0, 0, 0, 0)
        self.todo_stack.setStyleSheet(f'color: white; border: 1px;')

        #### bottom to top stacking
        # self.lay.addStretch()

        ### top to bottom stacking
        lay.setAlignment(Qt.AlignTop)
        self.todo_stack.setLayout(lay)

        # scroll area for todos
        scroll = QScrollArea(widgetResizable=True)
        scroll.setWidget(self.todo_stack)

        # text input for new todo
        self.textbox = QLineEdit(self)
        self.textbox.setMaxLength(100)
        self.textbox.setStyleSheet(f"padding-left: 10px; color: {config.border_color}; height: 50px; font: 16px")

        # main button
        main_button = QPushButton("Add")
        main_button.clicked.connect(self.add)
        main_button.setAutoDefault(True)
        main_button.setCursor(QCursor(Qt.PointingHandCursor))

        clean_button = QPushButton("Clean")
        # self.clean_button.clicked.connect(self.add)
        clean_button.setAutoDefault(True)
        clean_button.setCursor(QCursor(Qt.PointingHandCursor))
        clean_button.clicked.connect(self.clean)

        # do something on enter press
        self.textbox.returnPressed.connect(main_button.click)

        buttons_widget = QWidget()
        buttons_widget.setStyleSheet(f"color: {config.border_color}; height: 40px; font: 12px;")
        hbox = QHBoxLayout()
        hbox.addWidget(main_button)
        hbox.addWidget(clean_button)
        buttons_widget.setLayout(hbox)
        buttons_widget.setStyleSheet(f"padding-left: 10px; color: {config.border_color}; height: 50px; font: 16px")

        # main layout
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(scroll)
        vbox.addWidget(self.textbox)
        vbox.addWidget(buttons_widget)
        vbox.setContentsMargins(0, 0, 0, 0)
        self.setLayout(vbox)

    def add(self):
        text = self.textbox.text()
        todo = QWidget()

        label = QLabel(text)
        label.setFont(QFont('Monospace', 12))
        label.setWordWrap(True);
        label.setStyleSheet(f'padding-left: 3px; color: white; max-width: 400;')

        done_button = QPushButton("✓")
        done_button.clicked.connect(lambda: self.done(label))
        done_button.setStyleSheet("color: white; height:30px; Font: 14px;")
        done_button.setFixedWidth(30)
        done_button.setCursor(QCursor(Qt.PointingHandCursor))

        delete_button = QPushButton("x")
        
        delete_button.setStyleSheet("color: white; height:30px; Font: 14px")
        delete_button.setFixedWidth(30)
        delete_button.setCursor(QCursor(Qt.PointingHandCursor))

        hbox = QHBoxLayout()
        hbox.addWidget(label)
        hbox.addWidget(done_button)
        hbox.addWidget(delete_button)

        todo.setLayout(hbox)

        self.todo_stack.layout().addWidget(todo)

        del_parent = delete_button.parentWidget()
        delete_button.clicked.connect(lambda: self.delete(del_parent))

        self.textbox.clear()

        db.add(text, False)

    def add_from_db(self):
        todos = db.get_all()
        print(todos)
        for item in todos:
            todo = QWidget()
            label = QLabel(item[0]) # text
            label.setFont(QFont('Monospace', 12))
            label.setWordWrap(True);
            label.setStyleSheet(f'padding-left: 3px; color: white; max-width: 400;')

            done_button = QPushButton("✓")
            done_button.clicked.connect(lambda: self.done(label))
            done_button.setStyleSheet("color: white; height:30px; Font: 14px;")
            done_button.setFixedWidth(30)
            done_button.setCursor(QCursor(Qt.PointingHandCursor))

            delete_button = QPushButton("x")
            
            delete_button.setStyleSheet("color: white; height:30px; Font: 14px")
            delete_button.setFixedWidth(30)
            delete_button.setCursor(QCursor(Qt.PointingHandCursor))

            hbox = QHBoxLayout()
            hbox.addWidget(label)
            hbox.addWidget(done_button)
            hbox.addWidget(delete_button)

            todo.setLayout(hbox)

            self.todo_stack.layout().addWidget(todo)

            del_parent = delete_button.parentWidget()
            delete_button.clicked.connect(lambda: self.delete(del_parent))

            if item[1] == 1:
                done_button.click()


    def done(self, instance):
        f = instance.font()
        text = instance.text()

        if f.strikeOut():
            f.setStrikeOut(False)
            db.change_status(text, False)
        else:
            f.setStrikeOut(True)
            db.change_status(text, True)

        instance.setFont(f)

    def delete(self, parent):
        parent.setParent(None)
        todo_text = parent.layout().itemAt(0).widget().text()
        db.delete(todo_text)

    def clean(self):
        for i in reversed(range(self.todo_stack.layout().count())): 
            self.todo_stack.layout().itemAt(i).widget().setParent(None)



