# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/relationship_configuration.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RelationshipConfigFrame(object):
    def setupUi(self, RelationshipConfigFrame):
        RelationshipConfigFrame.setObjectName("RelationshipConfigFrame")
        RelationshipConfigFrame.resize(624, 361)
        RelationshipConfigFrame.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        RelationshipConfigFrame.setFont(font)
        RelationshipConfigFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        RelationshipConfigFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.verticalLayout = QtWidgets.QVBoxLayout(RelationshipConfigFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.RelationshipTableWidget = QtWidgets.QTableWidget(RelationshipConfigFrame)
        self.RelationshipTableWidget.setMinimumSize(QtCore.QSize(600, 300))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        self.RelationshipTableWidget.setFont(font)
        self.RelationshipTableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.RelationshipTableWidget.setColumnCount(4)
        self.RelationshipTableWidget.setObjectName("RelationshipTableWidget")
        self.RelationshipTableWidget.setRowCount(15)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        item.setFont(font)
        self.RelationshipTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        item.setFont(font)
        self.RelationshipTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(9)
        item.setFont(font)
        self.RelationshipTableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        item.setFont(font)
        self.RelationshipTableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        self.RelationshipTableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(7, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(8, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(9, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(10, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(11, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(12, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(13, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setCheckState(QtCore.Qt.Unchecked)
        self.RelationshipTableWidget.setItem(14, 0, item)
        self.RelationshipTableWidget.horizontalHeader().setStretchLastSection(True)
        self.RelationshipTableWidget.verticalHeader().setVisible(True)
        self.RelationshipTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.RelationshipTableWidget.verticalHeader().setDefaultSectionSize(30)
        self.RelationshipTableWidget.verticalHeader().setHighlightSections(False)
        self.RelationshipTableWidget.verticalHeader().setSortIndicatorShown(False)
        self.RelationshipTableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.RelationshipTableWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addRelationPushButton = QtWidgets.QPushButton(RelationshipConfigFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRelationPushButton.sizePolicy().hasHeightForWidth())
        self.addRelationPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.addRelationPushButton.setFont(font)
        self.addRelationPushButton.setObjectName("addRelationPushButton")
        self.horizontalLayout.addWidget(self.addRelationPushButton)
        self.editRelationPushButton = QtWidgets.QPushButton(RelationshipConfigFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editRelationPushButton.sizePolicy().hasHeightForWidth())
        self.editRelationPushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.editRelationPushButton.setFont(font)
        self.editRelationPushButton.setObjectName("editRelationPushButton")
        self.horizontalLayout.addWidget(self.editRelationPushButton)
        self.deleteRelationPushButton = QtWidgets.QPushButton(RelationshipConfigFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.deleteRelationPushButton.sizePolicy().hasHeightForWidth())
        self.deleteRelationPushButton.setSizePolicy(sizePolicy)
        self.deleteRelationPushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.deleteRelationPushButton.setSizeIncrement(QtCore.QSize(0, 2))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.deleteRelationPushButton.setFont(font)
        self.deleteRelationPushButton.setObjectName("deleteRelationPushButton")
        self.horizontalLayout.addWidget(self.deleteRelationPushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(RelationshipConfigFrame)
        QtCore.QMetaObject.connectSlotsByName(RelationshipConfigFrame)

    def retranslateUi(self, RelationshipConfigFrame):
        _translate = QtCore.QCoreApplication.translate
        RelationshipConfigFrame.setWindowTitle(_translate("RelationshipConfigFrame", "Relationships"))
        item = self.RelationshipTableWidget.verticalHeaderItem(0)
        item.setText(_translate("RelationshipConfigFrame", "1"))
        item = self.RelationshipTableWidget.verticalHeaderItem(1)
        item.setText(_translate("RelationshipConfigFrame", "2"))
        item = self.RelationshipTableWidget.verticalHeaderItem(2)
        item.setText(_translate("RelationshipConfigFrame", "3"))
        item = self.RelationshipTableWidget.verticalHeaderItem(3)
        item.setText(_translate("RelationshipConfigFrame", "4"))
        item = self.RelationshipTableWidget.verticalHeaderItem(4)
        item.setText(_translate("RelationshipConfigFrame", "5"))
        item = self.RelationshipTableWidget.verticalHeaderItem(5)
        item.setText(_translate("RelationshipConfigFrame", "6"))
        item = self.RelationshipTableWidget.verticalHeaderItem(6)
        item.setText(_translate("RelationshipConfigFrame", "7"))
        item = self.RelationshipTableWidget.verticalHeaderItem(7)
        item.setText(_translate("RelationshipConfigFrame", "8"))
        item = self.RelationshipTableWidget.verticalHeaderItem(8)
        item.setText(_translate("RelationshipConfigFrame", "9"))
        item = self.RelationshipTableWidget.verticalHeaderItem(9)
        item.setText(_translate("RelationshipConfigFrame", "10"))
        item = self.RelationshipTableWidget.verticalHeaderItem(10)
        item.setText(_translate("RelationshipConfigFrame", "11"))
        item = self.RelationshipTableWidget.verticalHeaderItem(11)
        item.setText(_translate("RelationshipConfigFrame", "12"))
        item = self.RelationshipTableWidget.verticalHeaderItem(12)
        item.setText(_translate("RelationshipConfigFrame", "13"))
        item = self.RelationshipTableWidget.verticalHeaderItem(13)
        item.setText(_translate("RelationshipConfigFrame", "14"))
        item = self.RelationshipTableWidget.verticalHeaderItem(14)
        item.setText(_translate("RelationshipConfigFrame", "15"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("RelationshipConfigFrame", "Relationship ID"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("RelationshipConfigFrame", "Parent"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("RelationshipConfigFrame", "Child"))
        item = self.RelationshipTableWidget.horizontalHeaderItem(3)
        item.setText(_translate("RelationshipConfigFrame", "Label"))
        __sortingEnabled = self.RelationshipTableWidget.isSortingEnabled()
        self.RelationshipTableWidget.setSortingEnabled(False)
        self.RelationshipTableWidget.setSortingEnabled(__sortingEnabled)
        self.addRelationPushButton.setText(_translate("RelationshipConfigFrame", "Add relationship"))
        self.editRelationPushButton.setText(_translate("RelationshipConfigFrame", "Edit relationship"))
        self.deleteRelationPushButton.setText(_translate("RelationshipConfigFrame", "Delete relationship"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RelationshipConfigFrame = QtWidgets.QFrame()
    ui = Ui_RelationshipConfigFrame()
    ui.setupUi(RelationshipConfigFrame)
    RelationshipConfigFrame.show()
    sys.exit(app.exec_())
