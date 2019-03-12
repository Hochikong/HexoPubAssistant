import os
import re
import time
import signal
import psutil
import subprocess


def goto_dir(path):
    """
    Go to any dir.
    :param path:
    :return:
    """
    os.chdir(path)


def read_markdown_head(file):
    """
    Read the head of one hexo blog file(.md)
    hexo的categories项并不关注有没有引号！
    :param file:
    :return:
    """
    with open(file, 'r', encoding='utf-8') as fl:
        content = fl.readlines()
    blog_head_location = content.index("---\n", 1)
    blog_head = content[:blog_head_location+1]
    category_pattern = re.compile(r"categories:.*")
    raw_category = list(filter(category_pattern.match, blog_head))[0]
    return re.split(re.compile(r"categories: "), raw_category)[-1]


def collect_all_categories():
    """
    You should use goto_dir push into HEXOBLOG\source\_posts before you run this function.
    :return:
    """
    files = os.listdir()
    markdown_pattern = re.compile(r".*\.md")
    cates = list(set([read_markdown_head(file) for file in filter(markdown_pattern.match, files)]))
    return [cat.strip() for cat in cates]


def new_page(file):
    """
    create new page
    :param file:
    :return:
    """
    os.system("hexo new {}".format(file))


def preview():
    """
    You should use goto_dir push into HEXOBLOG\ before you run this function.
    :return:
    """
    os.system("hexo clean && hexo g")
    subprocess.Popen("hexo s", shell=True)
    time.sleep(4)
    return 'http://localhost:4000'


def cancel_preview():
    """
    WARNING: You should not use any nodejs program while you preview
    :return:
    """
    process_info = [p.info for p in psutil.process_iter(attrs=['pid', 'name']) if 'node' in p.info['name']]
    [os.kill(i['pid'], signal.SIGINT) for i in process_info]
    return


def publish():
    """
    发布博客
    :return:
    """
    os.system("hexo clean && hexo g && hexo d")


def open_file(file, postfix):
    """
    Open the .md file with default app on Windows
    :param file:
    :param postfix: eg. '.md'
    :return:
    """
    os.startfile(file+postfix)


def rewrite_blog_head(file, title, category, tag):
    """
    本程序为了适配hiker主题，只用一个category和tag
    :param file:
    :param title:
    :param category:
    :param tag:
    :return:
    """
    full_name = file+'.md'
    with open(full_name, 'r', encoding='utf-8') as fl:
        content = fl.readlines()
    blog_head_location = content.index("---\n", 1)
    blog_head = content[:blog_head_location+1]

    new_title = "title: {}\n".format(title)
    new_category = "categories: {}\n".format(category)
    new_tag = "tags: {}\n".format(tag)

    for i, element in enumerate(blog_head):
        if 'title' in element:
            blog_head[i] = new_title
        if 'tags' in element:
            blog_head[i] = new_tag
        if 'date' in element:
            blog_head.insert(i+1, new_category)

    with open(full_name, 'w', encoding='utf-8') as fl1:
        fl1.writelines(blog_head)


def length_check(*args):
    """
    对create窗口的内容进行长度检查
    :param args:
    :return:
    """
    for arg in args:
        if len(arg) < 1:
            return False
