# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/icon_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_iconConfigDialog(object):
    def setupUi(self, iconConfigDialog):
        iconConfigDialog.setObjectName("iconConfigDialog")
        iconConfigDialog.resize(547, 237)
        self.verticalLayout = QtWidgets.QVBoxLayout(iconConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.iconTableWidget = QtWidgets.QTableWidget(iconConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.iconTableWidget.sizePolicy().hasHeightForWidth())
        self.iconTableWidget.setSizePolicy(sizePolicy)
        self.iconTableWidget.setMinimumSize(QtCore.QSize(525, 178))
        self.iconTableWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.iconTableWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setUnderline(False)
        font.setStrikeOut(False)
        self.iconTableWidget.setFont(font)
        self.iconTableWidget.setMouseTracking(False)
        self.iconTableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.iconTableWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.iconTableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.iconTableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.iconTableWidget.setLineWidth(1)
        self.iconTableWidget.setMidLineWidth(0)
        self.iconTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.iconTableWidget.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.iconTableWidget.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.iconTableWidget.setAlternatingRowColors(False)
        self.iconTableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.iconTableWidget.setIconSize(QtCore.QSize(0, 0))
        self.iconTableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.iconTableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.iconTableWidget.setRowCount(4)
        self.iconTableWidget.setObjectName("iconTableWidget")
        self.iconTableWidget.setColumnCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.iconTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.iconTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.iconTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.iconTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.iconTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.iconTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.iconTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.iconTableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.iconTableWidget.setItem(3, 0, item)
        self.iconTableWidget.horizontalHeader().setVisible(False)
        self.iconTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.iconTableWidget.horizontalHeader().setMinimumSectionSize(21)
        self.iconTableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.iconTableWidget.horizontalHeader().setStretchLastSection(True)
        self.iconTableWidget.verticalHeader().setSortIndicatorShown(True)
        self.iconTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.iconTableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addIconButton = QtWidgets.QPushButton(iconConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addIconButton.sizePolicy().hasHeightForWidth())
        self.addIconButton.setSizePolicy(sizePolicy)
        self.addIconButton.setMinimumSize(QtCore.QSize(0, 0))
        self.addIconButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(8)
        self.addIconButton.setFont(font)
        self.addIconButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.addIconButton.setIconSize(QtCore.QSize(16, 16))
        self.addIconButton.setCheckable(False)
        self.addIconButton.setAutoRepeatInterval(300)
        self.addIconButton.setObjectName("addIconButton")
        self.horizontalLayout.addWidget(self.addIconButton)
        self.editIconButton = QtWidgets.QPushButton(iconConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editIconButton.sizePolicy().hasHeightForWidth())
        self.editIconButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.editIconButton.setFont(font)
        self.editIconButton.setObjectName("editIconButton")
        self.horizontalLayout.addWidget(self.editIconButton)
        self.deleteIconButton = QtWidgets.QPushButton(iconConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteIconButton.sizePolicy().hasHeightForWidth())
        self.deleteIconButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.deleteIconButton.setFont(font)
        self.deleteIconButton.setObjectName("deleteIconButton")
        self.horizontalLayout.addWidget(self.deleteIconButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(iconConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(iconConfigDialog)

    def retranslateUi(self, iconConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        iconConfigDialog.setWindowTitle(_translate("iconConfigDialog", "Icon Configuration"))
        self.iconTableWidget.setSortingEnabled(True)
        item = self.iconTableWidget.verticalHeaderItem(0)
        item.setText(_translate("iconConfigDialog", "1"))
        item = self.iconTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("iconConfigDialog", "Select"))
        item = self.iconTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("iconConfigDialog", "Icon Name"))
        item = self.iconTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("iconConfigDialog", "Icon Source"))
        item = self.iconTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("iconConfigDialog", "Icon Preview"))
        __sortingEnabled = self.iconTableWidget.isSortingEnabled()
        self.iconTableWidget.setSortingEnabled(False)
        self.iconTableWidget.setSortingEnabled(__sortingEnabled)
        self.addIconButton.setText(_translate("iconConfigDialog", "Add Icon"))
        self.editIconButton.setText(_translate("iconConfigDialog", "Delete Icon"))
        self.deleteIconButton.setText(_translate("iconConfigDialog", "Edit Icon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    iconConfigDialog = QtWidgets.QDialog()
    ui = Ui_iconConfigDialog()
    ui.setupUi(iconConfigDialog)
    iconConfigDialog.show()
    sys.exit(app.exec_())
