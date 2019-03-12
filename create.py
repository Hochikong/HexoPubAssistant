# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\ckhoi\PycharmProjects\HexoPubAssistant\create.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Create_Dialog(object):
    def setupUi(self, Create_Dialog):
        Create_Dialog.setObjectName("Create_Dialog")
        Create_Dialog.resize(400, 183)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ICON/hexo logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Create_Dialog.setWindowIcon(icon)
        Create_Dialog.setStyleSheet("background-color: rgb(233, 233, 225);\n"
"selection-background-color: rgb(199, 197, 184);\n"
"font: 57 10pt \"GenWanMin TW TTF Medium\";")
        self.buttonBox = QtWidgets.QDialogButtonBox(Create_Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 140, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(Create_Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 112))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.blog_file_name = QtWidgets.QLabel(self.formLayoutWidget)
        self.blog_file_name.setObjectName("blog_file_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.blog_file_name)
        self.blog_file_name_space = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.blog_file_name_space.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.blog_file_name_space.setInputMask("")
        self.blog_file_name_space.setObjectName("blog_file_name_space")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.blog_file_name_space)
        self.blog_title = QtWidgets.QLabel(self.formLayoutWidget)
        self.blog_title.setObjectName("blog_title")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.blog_title)
        self.blog_title_space = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.blog_title_space.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.blog_title_space.setObjectName("blog_title_space")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.blog_title_space)
        self.blog_categories = QtWidgets.QLabel(self.formLayoutWidget)
        self.blog_categories.setObjectName("blog_categories")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.blog_categories)
        self.blog_tags = QtWidgets.QLabel(self.formLayoutWidget)
        self.blog_tags.setObjectName("blog_tags")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.blog_tags)
        self.blog_tags_space = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.blog_tags_space.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.blog_tags_space.setObjectName("blog_tags_space")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.blog_tags_space)
        self.blog_categories_space = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.blog_categories_space.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.blog_categories_space.setObjectName("blog_categories_space")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.blog_categories_space)

        self.retranslateUi(Create_Dialog)
        self.buttonBox.accepted.connect(Create_Dialog.accept)
        self.buttonBox.rejected.connect(Create_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Create_Dialog)

    def retranslateUi(self, Create_Dialog):
        _translate = QtCore.QCoreApplication.translate
        Create_Dialog.setWindowTitle(_translate("Create_Dialog", "博文创建向导"))
        self.blog_file_name.setText(_translate("Create_Dialog", "文章文件名"))
        self.blog_file_name_space.setPlaceholderText(_translate("Create_Dialog", "此处输入什么都只会记录为一个值"))
        self.blog_title.setText(_translate("Create_Dialog", "文章标题"))
        self.blog_title_space.setPlaceholderText(_translate("Create_Dialog", "此处输入什么都只会记录为一个值"))
        self.blog_categories.setText(_translate("Create_Dialog", "文章分类"))
        self.blog_tags.setText(_translate("Create_Dialog", "博客标签"))
        self.blog_tags_space.setPlaceholderText(_translate("Create_Dialog", "此处输入什么都只会记录为一个值"))
        self.blog_categories_space.setPlaceholderText(_translate("Create_Dialog", "此处输入什么都只会记录为一个值"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Create_Dialog = QtWidgets.QDialog()
    ui = Ui_Create_Dialog()
    ui.setupUi(Create_Dialog)
    Create_Dialog.show()
    sys.exit(app.exec_())

