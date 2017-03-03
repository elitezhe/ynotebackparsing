# -*- coding: utf-8 -*-

import codecs
import string
import logging
import sys


def get_note_title_from_info(info_path):
    """
    传入笔记标题Info文件路径,返回笔记标题
    :param info_path:
    :return:
    """
    info_file = open(info_path, 'rb')
    info_file.seek(4)
    info_str = info_file.read()
    try:
        info_str = codecs.decode(info_str, 'utf-16', 'ignore')  # ignore参数很重要,调用时不可以用errors='ignore'
    except UnicodeDecodeError, Argument:
        logging.debug(Argument)

    title_rindex = string.find(info_str, '.note')
    note_title = info_str[0:title_rindex]
    return note_title


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    path = r'C:\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes\F098AF4EBCC64781916E8EA0F451257\Info'
    title = get_note_title_from_info(r'C:\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes\F098AF4EBCC64781916E8EA0F451257\Info')

    print title
    print type(title)


