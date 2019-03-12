import sys
import yaml
from PyQt5 import QtWidgets, QtCore
from mainwindow import Ui_MainWindow
from create import Ui_Create_Dialog
from preview import Ui_Preview_Dialog
from msgbox import Ui_Gen_Dialog
from about import Ui_About_Dialog
from HPA_agent.funs import *

NEEDLONGER = '输入不允许长度为0。'
PUBLISHDONE = '博客内容已发布。请检查“博文状态”等待到“已发布”。'
OPENDONE = '文件已使用默认程序打开，请检查。'
GENERATING = '正在生成, 请检查“博文状态”等待到“待编辑”。'
EDITALREADY = '已编辑'
WAITFOREDIT = '待编辑'
PUBLISHALREADY = '已发布'
SCANDONE = '已搜索完毕。'
ABOUT = """
        HexoPublishAssistant
        Copyright 2019 Hochikong
        All Rights Reserved

        Email: ckhoidea@hotmail.com
"""


class HPA:
    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)

        self.main_window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_window)
        self.ui.pushButton.setDisabled(True)

        self.create_dialog = QtWidgets.QDialog()
        self.create_dialog_ui = Ui_Create_Dialog()
        self.create_dialog_ui.setupUi(self.create_dialog)

        self.preview_dialog = QtWidgets.QDialog()
        self.preview_dialog_ui = Ui_Preview_Dialog()
        self.preview_dialog_ui.setupUi(self.preview_dialog)

        self.universal_msg_dialog = QtWidgets.QDialog()
        self.universal_msg_dialog_ui = Ui_Gen_Dialog()
        self.universal_msg_dialog_ui.setupUi(self.universal_msg_dialog)

        self.about_dialog = QtWidgets.QDialog()
        self.about_dialog_ui = Ui_About_Dialog()
        self.about_dialog_ui.setupUi(self.about_dialog)
        self.about_dialog_ui.about_page.setText(ABOUT)

        # menu bar signal and slot
        self.ui.action.triggered.connect(self.create_new_post)
        self.ui.action_2.triggered.connect(self.preview_post)
        self.ui.action_3.triggered.connect(self.publish_post)
        self.ui.pushButton.clicked.connect(self.open_post)
        self.ui.scan_categories.triggered.connect(self.scan_categories)
        self.ui.open_config_file.triggered.connect(self.open_config)
        self.ui.help.triggered.connect(self.show_help)
        self.ui.about.triggered.connect(self.show_about)

        # load config
        with open('config.txt', 'r', encoding='utf-8') as configf:
            self.config = yaml.load(configf)
        self.current_path = os.getcwd()

        # Thread
        self.query_result = None
        self.cr_thread = CreatePostThread(self.config, self.query_result)
        self.op_thread = OpenPostThread(self.config, self.query_result)
        self.pr_thread = PreviewPostThread(self.config)
        self.pu_thread = PublishPostThread(self.config)

        # update view

        goto_dir(self.config['blog']['posts_location'])
        self.all_categories = collect_all_categories()
        [self.ui.listWidget.addItem(cat) for cat in self.all_categories]

        # show mainwindow
        self.main_window.show()
        sys.exit(self.app.exec_())

    def alert(self, content):
        self.universal_msg_dialog_ui.attention.setText(content)
        self.universal_msg_dialog.show()
        self.universal_msg_dialog.exec_()

    # create new post

    def cleanup_create_spaces_input(self):
        self.create_dialog_ui.blog_file_name_space.clear()
        self.create_dialog_ui.blog_title_space.clear()
        self.create_dialog_ui.blog_categories_space.clear()
        self.create_dialog_ui.blog_tags_space.clear()

    def cleanup_mainwindow_info_spaces(self):
        self.ui.blog_title_LineEdit.clear()
        self.ui.blog_category_LineEdit.clear()
        self.ui.blog_tag_LineEdit.clear()

    def get_create_spaces_input(self):
        return {'filename': self.create_dialog_ui.blog_file_name_space.text(),
                'title': self.create_dialog_ui.blog_title_space.text(),
                'category': self.create_dialog_ui.blog_categories_space.text(),
                'tag': self.create_dialog_ui.blog_tags_space.text()}

    def check_create_spaces_input(self, query):
        result = length_check(query['filename'], query['title'], query['category'], query['tag'])
        if result is False:
            self.alert(NEEDLONGER)
            self.cleanup_create_spaces_input()
            return False
        else:
            return True

    def update_mainwindow_info_spaces(self):
        self.ui.blog_title_LineEdit.setText(self.query_result['title'])
        self.ui.blog_category_LineEdit.setText(self.query_result['category'])
        self.ui.blog_tag_LineEdit.setText(self.query_result['tag'])

    def create_new_post(self):
        self.create_dialog.show()
        rsp = self.create_dialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            self.query_result = self.get_create_spaces_input()
            if self.check_create_spaces_input(self.query_result):
                self.alert(GENERATING)

                self.cr_thread.update_query(self.query_result)
                self.cr_thread.start()
                self.cr_thread.creating.connect(self.ui.blog_status_label.setText)

                # print(self.query_result)
                self.cleanup_mainwindow_info_spaces()
                self.update_mainwindow_info_spaces()
                self.cleanup_create_spaces_input()
                time.sleep(4)
                self.ui.pushButton.setEnabled(True)
        else:
            self.cleanup_create_spaces_input()

    # preview post

    def preview_post(self):
        self.pr_thread.start()
        self.pr_thread.previewing.connect(self.preview_dialog_ui.lineEdit.setText)
        self.preview_dialog.show()
        rsp = self.preview_dialog.exec_()

        if rsp == QtWidgets.QDialog.Rejected:
            cancel_preview()

    # publish post

    def publish_post(self):
        self.pu_thread.start()
        self.pu_thread.publishing.connect(self.ui.blog_status_label.setText)
        self.alert(PUBLISHDONE)

    # open post with default app

    def open_post(self):
        self.op_thread.update_query(self.query_result)
        self.op_thread.start()
        self.alert(OPENDONE)
        self.ui.blog_status_label.setText(EDITALREADY)

    # update categories by user
    def scan_categories(self):
        goto_dir(self.config['blog']['posts_location'])
        self.all_categories = collect_all_categories()
        self.ui.listWidget.clear()
        [self.ui.listWidget.addItem(cat) for cat in self.all_categories]
        self.alert(SCANDONE)

    # open xxx.txt
    def open_config(self):
        goto_dir(self.current_path)
        open_file('config', '.txt')

    def show_about(self):
        self.about_dialog.show()
        self.about_dialog.exec_()

    def show_help(self):
        goto_dir(self.current_path)
        open_file('help', '.txt')


class CreatePostThread(QtCore.QThread):
    creating = QtCore.pyqtSignal(str)

    def __init__(self, config, query, parent=None):
        super(CreatePostThread, self).__init__(parent)
        self.config = config
        self.query = query

    def run(self):
        goto_dir(self.config['blog']['location'])
        new_page(self.query['filename'])
        goto_dir(self.config['blog']['posts_location'])
        rewrite_blog_head(self.query['filename'], self.query['title'],
                          self.query['category'], self.query['tag'])
        self.creating.emit(WAITFOREDIT)

    def update_query(self, new_query):
        self.query = new_query


class OpenPostThread(QtCore.QThread):
    # opening = QtCore.pyqtSignal(str)

    def __init__(self, config, query, parent=None):
        super(OpenPostThread, self).__init__(parent)
        self.config = config
        self.query = query

    def run(self):
        goto_dir(self.config['blog']['posts_location'])
        open_file(self.query['filename'], '.md')
        # self.opening.emit("已编辑")

    def update_query(self, new_query):
        self.query = new_query


class PreviewPostThread(QtCore.QThread):
    previewing = QtCore.pyqtSignal(str)

    def __init__(self, config, parent=None):
        super(PreviewPostThread, self).__init__(parent)
        self.config = config

    def run(self):
        goto_dir(self.config['blog']['location'])
        addr = preview()
        self.previewing.emit(addr)


class PublishPostThread(QtCore.QThread):
    publishing = QtCore.pyqtSignal(str)

    def __init__(self, config, parent=None):
        super(PublishPostThread, self).__init__(parent)
        self.config = config

    def run(self):
        goto_dir(self.config['blog']['location'])
        publish()
        self.publishing.emit(PUBLISHALREADY)


if __name__ == '__main__':
    HPA()
