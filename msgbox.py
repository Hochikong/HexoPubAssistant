# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'msgbox.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Gen_Dialog(object):
    def setupUi(self, Gen_Dialog):
        Gen_Dialog.setObjectName("Gen_Dialog")
        Gen_Dialog.resize(396, 118)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON/hexo logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Gen_Dialog.setWindowIcon(icon)
        Gen_Dialog.setStyleSheet("background-color: rgb(243, 242, 238);\n"
"selection-background-color: rgb(199, 197, 184);\n"
"font: 57 10pt \"GenWanMin TW TTF Medium\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Gen_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.attention = QtWidgets.QLabel(Gen_Dialog)
        self.attention.setGeometry(QtCore.QRect(20, 20, 361, 51))
        self.attention.setStyleSheet("font: 57 10pt \"GenWanMin TW TTF Medium\";")
        self.attention.setText("")
        self.attention.setObjectName("attention")

        self.retranslateUi(Gen_Dialog)
        self.buttonBox.accepted.connect(Gen_Dialog.accept)
        self.buttonBox.rejected.connect(Gen_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Gen_Dialog)

    def retranslateUi(self, Gen_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Gen_Dialog.setWindowTitle(_translate("Gen_Dialog", "注意"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Gen_Dialog = QtWidgets.QDialog()
    ui = Ui_Gen_Dialog()
    ui.setupUi(Gen_Dialog)
    Gen_Dialog.show()
    sys.exit(app.exec_())

