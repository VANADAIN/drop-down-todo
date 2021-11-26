# from PyQt5.QtWidgets import  QWidget, QPushButton, QLabel, QHBoxLayout
# from PyQt5.QtGui import QCursor, QFont
# from PyQt5.QtCore import Qt

# from todo import TodoApp 

# class TodoWidget(QWidget, TodoApp):
#     def __init__(self, text):
#         super().__init__()

        
#         done_button = QPushButton("✓")
#         done_button.clicked.connect(self.done)
#         done_button.setStyleSheet("color: white; height:30px; Font: 14px;")
#         done_button.setFixedWidth(30)
#         done_button.setCursor(QCursor(Qt.PointingHandCursor))

#         delete_button = QPushButton("x")
#         delete_button.setStyleSheet("color: white; height:30px; Font: 14px")
#         delete_button.setFixedWidth(30)
#         delete_button.setCursor(QCursor(Qt.PointingHandCursor))

#         label = QLabel(text)
#         label.setFont(QFont('Monospace', 12))
#         label.setWordWrap(True);
#         label.setStyleSheet(f'padding-left: 3px; color: white; max-width: 400;')


#         hbox = QHBoxLayout()
#         hbox.addWidget(label)
#         hbox.addWidget(done_button)
#         hbox.addWidget(delete_button)

#         self.setLayout(hbox)

        
