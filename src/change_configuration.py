# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/change_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_changeConfigDialog(object):
    def setupUi(self, changeConfigDialog):
        changeConfigDialog.setObjectName("changeConfigDialog")
        changeConfigDialog.resize(472, 283)
        self.verticalLayout = QtWidgets.QVBoxLayout(changeConfigDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.changeListLabel = QtWidgets.QLabel(changeConfigDialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.changeListLabel.setFont(font)
        self.changeListLabel.setObjectName("changeListLabel")
        self.verticalLayout.addWidget(self.changeListLabel, 0, QtCore.Qt.AlignHCenter)
        self.changeListText = QtWidgets.QTextEdit(changeConfigDialog)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.changeListText.setFont(font)
        self.changeListText.setObjectName("changeListText")
        self.verticalLayout.addWidget(self.changeListText)
        self.buttonsHL = QtWidgets.QHBoxLayout()
        self.buttonsHL.setObjectName("buttonsHL")
        self.undoButton = QtWidgets.QPushButton(changeConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undoButton.sizePolicy().hasHeightForWidth())
        self.undoButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.undoButton.setFont(font)
        self.undoButton.setObjectName("undoButton")
        self.buttonsHL.addWidget(self.undoButton)
        self.commitButton = QtWidgets.QPushButton(changeConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commitButton.sizePolicy().hasHeightForWidth())
        self.commitButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.commitButton.setFont(font)
        self.commitButton.setObjectName("commitButton")
        self.buttonsHL.addWidget(self.commitButton)
        self.verticalLayout.addLayout(self.buttonsHL)

        self.retranslateUi(changeConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(changeConfigDialog)

    def retranslateUi(self, changeConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        changeConfigDialog.setWindowTitle(_translate("changeConfigDialog", "Commit"))
        self.changeListLabel.setText(_translate("changeConfigDialog", "Change List"))
        self.undoButton.setText(_translate("changeConfigDialog", "Undo"))
        self.commitButton.setText(_translate("changeConfigDialog", "Commit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    changeConfigDialog = QtWidgets.QDialog()
    ui = Ui_changeConfigDialog()
    ui.setupUi(changeConfigDialog)
    changeConfigDialog.show()
    sys.exit(app.exec_())
