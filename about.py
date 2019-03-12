# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ckhoi\PycharmProjects\HexoPubAssistant\about.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_About_Dialog(object):
    def setupUi(self, About_Dialog):
        About_Dialog.setObjectName("About_Dialog")
        About_Dialog.resize(396, 178)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON/hexo logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        About_Dialog.setWindowIcon(icon)
        About_Dialog.setStyleSheet("background-color: rgb(233, 233, 225);\n"
"selection-background-color: rgb(199, 197, 184);\n"
"font: 57 10pt \"GenWanMin TW TTF Medium\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(About_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.about_page = QtWidgets.QLabel(About_Dialog)
        self.about_page.setGeometry(QtCore.QRect(20, 20, 361, 111))
        self.about_page.setStyleSheet("font: 57 10pt \"GenWanMin TW TTF Medium\";")
        self.about_page.setText("")
        self.about_page.setObjectName("about_page")

        self.retranslateUi(About_Dialog)
        self.buttonBox.accepted.connect(About_Dialog.accept)
        self.buttonBox.rejected.connect(About_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(About_Dialog)

    def retranslateUi(self, About_Dialog):
        _translate = QtCore.QCoreApplication.translate
        About_Dialog.setWindowTitle(_translate("About_Dialog", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    About_Dialog = QtWidgets.QDialog()
    ui = Ui_About_Dialog()
    ui.setupUi(About_Dialog)
    About_Dialog.show()
    sys.exit(app.exec_())

