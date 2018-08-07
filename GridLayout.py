from PyQt5.QtWidgets import (QGridLayout, QComboBox, QPushButton, QHBoxLayout, QLineEdit, QApplication, QWidget)
import qtawesome as qta
import sys


class GridLayout(QWidget):

    def __init__(self):
        super().__init__()
        try:
            self._init_ui()
        except Exception as e:
            print(str(e))

    def _init_ui(self):
        self.grid_layout = QGridLayout()
        index = 0
        for i in range(5):
            self.combobox_selection_list = ['NA', 'Intermediate', 'Curve']
            self.combobox_for_selection = QComboBox()
            self.combobox_for_selection.addItems(self.combobox_selection_list)
            self.combobox_for_selection.currentIndexChanged.connect(self.get_current_index)
            self.grid_layout.addWidget(self.combobox_for_selection, index, 0)
            self.line_edit = QLineEdit()
            self.line_edit.setPlaceholderText('Enter here')
            self.grid_layout.addWidget(self.line_edit, index, 1)
            self.delete_icon = qta.icon('fa.trash')
            self.delete_button = QPushButton(self.delete_icon, "Delete")
            self.delete_button.clicked.connect(self.get_row_column_from_grid_layout)
            self.edit_icon = qta.icon('fa.edit')
            self.edit_button = QPushButton(self.edit_icon, "Edit")
            self.edit_button.clicked.connect(self.get_row_column_from_grid_layout)
            self.grid_layout.addWidget(self.delete_button, index, 2)
            self.grid_layout.addWidget(self.edit_button, index, 3)
            index += 1
        self.setLayout(self.grid_layout)
        self.show()

    def get_row_column_from_grid_layout(self):
        try:
            button = self.sender()
            idx = self.grid_layout.indexOf(button)
            location = self.grid_layout.getItemPosition(idx)
            combo_box = self.grid_layout.indexOf(self.combobox_for_selection)
            print(self.combobox_for_selection.itemText(combo_box))
            # print("Button", button, "at row/col", location[:2])
            print('')
        except Exception as e:
            print(str(e))

    def get_current_index(self):
        print(self.combobox_for_selection.currentText())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    grid_layout_obj = GridLayout()
    sys.exit(app.exec_())

