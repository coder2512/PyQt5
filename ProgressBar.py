from PyQt5.QtWidgets import QProgressBar, QApplication, QVBoxLayout, QScrollArea, QGroupBox, QHBoxLayout, QPushButton, QLabel, QWidget
# from PyQt5 import QtGui

class ProgressBar(QGroupBox):

    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.setFixedWidth(500)
        self.setFixedHeight(500)
        self.style = """
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #37DA7E;
                    width: 20px;
                }"""

        self._init_ui()
        self.main_layout.addWidget(self.scroll_bar)
        self._create_button()

        self.main_layout.addLayout(self.horizontal_layout)
        self.setLayout(self.main_layout)

    def _init_ui(self):
        self.group_box = QGroupBox()
        # self.group_box.setFixedHeight(500)
        # self.group_box.setFixedWidth(500)
        vertical_layout = QVBoxLayout()

        self.scroll_bar = QScrollArea()
        for i in range(150):
            self.label = QLabel('Project ' + str(i) + '.')
            self.progress_bar_label = QLabel('Syncing ' + str(i) + '.')
            self.bottom_border = QWidget()
            self.bottom_border.setStyleSheet("""
                        background: palette(shadow);
                    """)
            # self.bottom_border.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed))
            self.bottom_border.setMinimumHeight(1)
            self.progress_bar = QProgressBar()
            self.progress_bar.setFixedWidth(440)
            self.progress_bar.setMaximum(100)
            self.progress_bar.setValue(0)
            self.progress_bar.setStyleSheet(self.style)
            vertical_layout.addWidget(self.label)
            vertical_layout.addWidget(self.progress_bar)
            vertical_layout.addWidget(self.progress_bar_label)
            vertical_layout.addWidget(self.bottom_border)
        self.group_box.setLayout(vertical_layout)
        self.scroll_bar.horizontalScrollBar().setVisible(False)
        self.scroll_bar.setWidget(self.group_box)

    def _create_button(self):
        self.horizontal_layout = QHBoxLayout()
        cancel_button = QPushButton("Cancel")
        ok_button = QPushButton("Ok")
        self.horizontal_layout.addWidget(ok_button)
        self.horizontal_layout.addWidget(cancel_button)
        cancel_button.clicked.connect(self.cancel_button_clicked)
        ok_button.clicked.connect(self.ok_button_clicked)

    def cancel_button_clicked(self):
        self.close()

    def ok_button_clicked(self):
        data = self.sender().parent()
        self.progress_bar.show()
        self.project_list = []
        for i in range(20):
            self.project_list.append('p{}'.format(i))
        for i, project_name in enumerate(self.project_list):
            self.progress_bar.setValue(0)
            self.progress_bar.setMaximum(100)
            self.progress_bar.setFormat(project_name)
        self.progress_bar.hide()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    grid_layout_obj = ProgressBar()
    grid_layout_obj.show()
    sys.exit(app.exec_())
