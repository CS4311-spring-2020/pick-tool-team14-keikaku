"""icon_config.py: Handles the icon window.

    Classes
    ----------
    UiIconConfig(QDialog)
        Initialize the icon window and set all signals and slots
        associated with it.

    @DEPRECIATED
"""

__author__ = "Team Keikaku"
__version__ = "0.5"

import os

from PyQt5.Qt import QLabel, QPixmap
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidget, QPushButton, QTableWidgetItem, QFileDialog
from PyQt5.uic import loadUi

from definitions import UI_PATH, ICON_PATH
from src.model.id_dictionary import IDDict


class UiIconConfig(QDialog):
    """The icon window which handles icon settings for the system."""

    row_position: int
    icon_dictionary: IDDict

    def __init__(self):
        """Initialize the icon window and set all signals and slots
        associated with it.
        """

        super(UiIconConfig, self).__init__()
        loadUi(os.path.join(UI_PATH, 'icon_config.ui'), self)

        self.dialog = QFileDialog()

        self.icon_dictionary = IDDict()
        self.iconTable = self.findChild(QTableWidget, 'iconTable')
        self.iconTable.setColumnWidth(0, 30)
        self.iconTable.setColumnHidden(0, True)
        self.iconTable.setColumnWidth(1, 120)
        self.iconTable.setColumnWidth(2, 260)

        self.row_position = self.iconTable.rowCount()

        self.addIconButton = self.findChild(QPushButton, 'addIconButton')
        self.addIconButton.clicked.connect(self.__add_icon)
        self.deleteIconButton = self.findChild(QPushButton, 'deleteIconButton')
        self.deleteIconButton.clicked.connect(self.__remove_icon)
        self.selectIconButton = self.findChild(QPushButton, 'selectIconButton')
        self.selectIconButton.clicked.connect(self.__select_icon)

        self.iconTable.itemChanged.connect(self.__update_cell)

        self.show()

    def __add_icon(self):
        """Adds a icon to the icon table and to the icon dictionary."""

        self.iconTable.blockSignals(True)
        self.iconTable.insertRow(self.row_position)
        uid = self.icon_dictionary.add(Icon('New Icon', os.path.join(ICON_PATH, 'circle.png')))
        source_item = QTableWidgetItem(os.path.join(ICON_PATH, 'circle.png'))
        self.iconTable.setItem(self.row_position, 0, QTableWidgetItem(uid))
        self.iconTable.setItem(self.row_position, 1, QTableWidgetItem('New Icon'))
        self.iconTable.setItem(self.row_position, 2, source_item)
        source_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.__insert_icon(self.row_position, 3, os.path.join(ICON_PATH, 'circle.png'), self.iconTable)

        self.row_position += 1
        self.iconTable.blockSignals(False)

    def __remove_icon(self):
        """Removes the selected icon from the icon table and from the icon dictionary."""

        self.iconTable.blockSignals(True)
        if self.iconTable.selectionModel().hasSelection():
            rows = self.iconTable.selectionModel().selectedRows()
            indexes = []
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                print(rowid)
                self.icon_dictionary.delete(self.iconTable.item(rowid, 0).text())
                self.iconTable.removeRow(rowid)
                self.row_position -= 1
        self.iconTable.blockSignals(False)

    def __select_icon(self):
        """Assigns the selected icon to the table cell."""

        self.iconTable.blockSignals(True)
        if self.iconTable.selectionModel().hasSelection():
            indexes = []
            rows = self.iconTable.selectionModel().selectedRows()
            for row in rows:
                indexes.append(row.row())
            indexes = sorted(indexes, reverse=True)
            for rowid in indexes:
                icon_file_path = self.dialog.getOpenFileName()[0]
                if icon_file_path:
                    file = os.path.basename(icon_file_path)
                    file_name = file.split('.')
                    if file_name[1] == 'jpg' or file_name[1] == 'png':
                        source_item = QTableWidgetItem(icon_file_path)
                        source_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable)
                        self.iconTable.setItem(rowid, 2, source_item)
                        source_item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
                        self.__insert_icon(rowid, 3, icon_file_path, self.iconTable)
                        self.__update_cell(source_item)
        self.iconTable.blockSignals(False)

    def __update_cell(self, item: QTableWidgetItem):
        """Updates the icon information from the cell that was just edited.

        :param item: QTableWidgetItem
            The item in the table cell which contains the information to update.
        """
        icon = self.icon_dictionary.get(self.iconTable.item(item.row(), 0).text())
        if item.column() == 1:
            print("here")
            icon.edit_name(item.text())
        elif item.column() == 2:
            print("here")
            print(item.text())
            icon.edit_source(item.text())
        else:
            print('Invalid column')
            return

        self.icon_dictionary.edit()

    @staticmethod
    def __insert_icon(row: int, col: int, icon_path: str, table: QTableWidget):
        """Inserts an icon into a table cell.

        :param row: int
            The row of the cell.
        :param col: int
            The col of the cell.
        :param icon_path: str
            The file path directory of the icon.
        :param table: QTableWidget
            The table containing the cell.
        """

        icon = QPixmap(icon_path).scaledToHeight(25).scaledToWidth(25)
        cell_widget = QLabel()
        cell_widget.setAlignment(Qt.AlignCenter)
        cell_widget.setPixmap(icon)
        table.setCellWidget(row, col, cell_widget)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = UiIconConfig()
    app.exec_()
