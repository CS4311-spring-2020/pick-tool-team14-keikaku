# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/directory_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_directoryConfigDialog(object):
    def setupUi(self, directoryConfigDialog):
        directoryConfigDialog.setObjectName("directoryConfigDialog")
        directoryConfigDialog.resize(422, 274)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(directoryConfigDialog.sizePolicy().hasHeightForWidth())
        directoryConfigDialog.setSizePolicy(sizePolicy)
        directoryConfigDialog.setMinimumSize(QtCore.QSize(0, 0))
        directoryConfigDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        directoryConfigDialog.setFont(font)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(directoryConfigDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rootDirectoryLabel = QtWidgets.QLabel(directoryConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rootDirectoryLabel.sizePolicy().hasHeightForWidth())
        self.rootDirectoryLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.rootDirectoryLabel.setFont(font)
        self.rootDirectoryLabel.setObjectName("rootDirectoryLabel")
        self.verticalLayout_2.addWidget(self.rootDirectoryLabel)
        self.rootDirectoryTextLine = QtWidgets.QLineEdit(directoryConfigDialog)
        self.rootDirectoryTextLine.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.rootDirectoryTextLine.setFont(font)
        self.rootDirectoryTextLine.setObjectName("rootDirectoryTextLine")
        self.verticalLayout_2.addWidget(self.rootDirectoryTextLine)
        self.redTeamLabel = QtWidgets.QLabel(directoryConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.redTeamLabel.sizePolicy().hasHeightForWidth())
        self.redTeamLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.redTeamLabel.setFont(font)
        self.redTeamLabel.setObjectName("redTeamLabel")
        self.verticalLayout_2.addWidget(self.redTeamLabel)
        self.redTeamTextLine = QtWidgets.QLineEdit(directoryConfigDialog)
        self.redTeamTextLine.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.redTeamTextLine.setFont(font)
        self.redTeamTextLine.setObjectName("redTeamTextLine")
        self.verticalLayout_2.addWidget(self.redTeamTextLine)
        self.blueTeamLabel = QtWidgets.QLabel(directoryConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueTeamLabel.sizePolicy().hasHeightForWidth())
        self.blueTeamLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.blueTeamLabel.setFont(font)
        self.blueTeamLabel.setObjectName("blueTeamLabel")
        self.verticalLayout_2.addWidget(self.blueTeamLabel)
        self.blueTeamTextLine = QtWidgets.QLineEdit(directoryConfigDialog)
        self.blueTeamTextLine.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.blueTeamTextLine.setFont(font)
        self.blueTeamTextLine.setObjectName("blueTeamTextLine")
        self.verticalLayout_2.addWidget(self.blueTeamTextLine)
        self.whiteTeamLabel = QtWidgets.QLabel(directoryConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whiteTeamLabel.sizePolicy().hasHeightForWidth())
        self.whiteTeamLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.whiteTeamLabel.setFont(font)
        self.whiteTeamLabel.setObjectName("whiteTeamLabel")
        self.verticalLayout_2.addWidget(self.whiteTeamLabel)
        self.whiteTeamTextLine = QtWidgets.QLineEdit(directoryConfigDialog)
        self.whiteTeamTextLine.setMinimumSize(QtCore.QSize(400, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.whiteTeamTextLine.setFont(font)
        self.whiteTeamTextLine.setObjectName("whiteTeamTextLine")
        self.verticalLayout_2.addWidget(self.whiteTeamTextLine)
        self.startDataIngestionButton = QtWidgets.QPushButton(directoryConfigDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startDataIngestionButton.sizePolicy().hasHeightForWidth())
        self.startDataIngestionButton.setSizePolicy(sizePolicy)
        self.startDataIngestionButton.setMinimumSize(QtCore.QSize(60, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.startDataIngestionButton.setFont(font)
        self.startDataIngestionButton.setObjectName("startDataIngestionButton")
        self.verticalLayout_2.addWidget(self.startDataIngestionButton, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(directoryConfigDialog)
        QtCore.QMetaObject.connectSlotsByName(directoryConfigDialog)

    def retranslateUi(self, directoryConfigDialog):
        _translate = QtCore.QCoreApplication.translate
        directoryConfigDialog.setWindowTitle(_translate("directoryConfigDialog", "Directory Configuration"))
        self.rootDirectoryLabel.setText(_translate("directoryConfigDialog", "Root Directory:"))
        self.redTeamLabel.setText(_translate("directoryConfigDialog", "Red Team Folder:"))
        self.blueTeamLabel.setText(_translate("directoryConfigDialog", "Blue Team Folder:"))
        self.whiteTeamLabel.setText(_translate("directoryConfigDialog", "White Team Folder:"))
        self.startDataIngestionButton.setText(_translate("directoryConfigDialog", "Start Data Ingestion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    directoryConfigDialog = QtWidgets.QDialog()
    ui = Ui_directoryConfigDialog()
    ui.setupUi(directoryConfigDialog)
    directoryConfigDialog.show()
    sys.exit(app.exec_())
