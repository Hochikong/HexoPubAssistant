# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'preview.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Preview_Dialog(object):
    def setupUi(self, Preview_Dialog):
        Preview_Dialog.setObjectName("Preview_Dialog")
        Preview_Dialog.resize(400, 136)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON/hexo logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Preview_Dialog.setWindowIcon(icon)
        Preview_Dialog.setStyleSheet("background-color: rgb(243, 242, 238);\n"
"selection-background-color: rgb(199, 197, 184);\n"
"font: 57 10pt \"GenWanMin TW TTF Medium\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Preview_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 90, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Preview_Dialog)
        self.label.setGeometry(QtCore.QRect(20, 40, 251, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Preview_Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 361, 20))
        self.lineEdit.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Preview_Dialog)
        self.buttonBox.accepted.connect(Preview_Dialog.accept)
        self.buttonBox.rejected.connect(Preview_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Preview_Dialog)

    def retranslateUi(self, Preview_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Preview_Dialog.setWindowTitle(_translate("Preview_Dialog", "博客预览"))
        self.label.setText(_translate("Preview_Dialog", "预览地址：(请稍等直到地址显示）"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Preview_Dialog = QtWidgets.QDialog()
    ui = Ui_Preview_Dialog()
    ui.setupUi(Preview_Dialog)
    Preview_Dialog.show()
    sys.exit(app.exec_())

