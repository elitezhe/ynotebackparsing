# -*- coding: utf-8 -*-

import codecs
import string
import logging
import sys
import os
import unicodedata


def get_note_title_from_info(info_path):
    """
    传入笔记标题Info文件路径,返回笔记标题
    :param info_path:
    :return:
    """
    info_file = open(info_path, 'rb')
    info_file.seek(4)
    info_str = info_file.read()
    info_file.close()  # close file handle
    try:
        info_str = codecs.decode(info_str, 'utf-16', 'ignore')  # ignore参数很重要,调用时不可以用errors='ignore'
    except UnicodeDecodeError, Argument:
        logging.debug(Argument)

    title_rindex = string.find(info_str, '.note')
    if title_rindex > 0:  # 部分微信保存笔记没有.note结尾
        note_title = info_str[0:title_rindex]
    else:
        note_title = info_str[0:20]
    # 避免笔记标题有链接,包含win下不能作为路径的符号
    # note_title = unicodedata.normalize('NFC' ,note_title)
    note_title = string.replace(note_title, ur'/', u'')
    note_title = string.replace(note_title, u'\\', u'')
    note_title = string.replace(note_title, ur':', u'')
    note_title = string.replace(note_title, ur'|', u'')
    note_title = string.replace(note_title, ur' ', u'')
    note_title = string.replace(note_title, ur'\r', u'')
    note_title = string.replace(note_title, ur'\n', u'')
    note_title = string.replace(note_title, ur'\t', u'')
    note_title = string.replace(note_title, ur'?', u'')
    note_title = string.replace(note_title, b'\x00', u'')  # \x00在win路径中是非法的
    note_title = string.replace(note_title, ur'"', u'')
    note_title = string.replace(note_title, ur'<', u'')
    note_title = string.replace(note_title, ur'>', u'')
    note_title = string.replace(note_title, ur'.', u'')

    return note_title


def get_note_content_from_content(cont_path):

    cont_file = open(cont_path, 'rb')
    cont_file.seek(4)
    cont_bytes = cont_file.read()
    cont_file.close()
    try:
        note_content = codecs.decode(cont_bytes, 'utf-16', 'ignore')
    except UnicodeDecodeError, Argument:
        logging.debug(Argument)
    return note_content


def get_res_info_from_resources(res_folder_path):
    """
    输入Resources中子文件夹目录,从Info中读取附件的代码(用在笔记中的一串类HASH字串)和原文件名
    :param res_folder_path:
    :return: 长度为2的字符串数组,第一元素为类HASH字串,第二元素为文件名
    """
    info_path = os.path.join(res_folder_path, 'Info')
    res_path = os.path.join(res_folder_path, 'Content')
    with open(info_path, 'rb') as f:
        f.seek(4)
        info_hash_bytes = f.read(64)
        f.seek(4)
        info_bytes = f.read()  # seek4后的64个字节是类HASH串

    info_str = codecs.decode(info_bytes, 'utf-16', 'ignore')
    info_hash_str = codecs.decode(info_hash_bytes, 'utf-16', 'ignore')
    # logging.debug(info_hash_str)

    tmp_info_list = list(info_str)
    for idx, c in enumerate(tmp_info_list):
        if c not in string.printable:
            tmp_info_list[idx] = u'/'
    # Now we get pure utf info_str
    info_str = u''.join(tmp_info_list)
    info_str_splited = string.split(info_str, u'/')
    info_list = [info_hash_str]

    for tmp in info_str_splited:
        tmp = string.strip(tmp)
        if not tmp == u'':
            info_list.append(tmp)
    return info_list[0:3]  # 此处未做有效性检验


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)


    # 2BEA622B6A3A4B62907BE83FF46794B CAC7EDDA72454468B8CD4697743E5F3 手写笔记 有问题,分割符+
    # 2C1B689D0EA74CAEBEAC84FE09D7A80 Resources 7B1597BFC05F4BD89113906CD0503CD
    # 569BAC97C5484626B2F951B1E51FC9B 标题有斜杠
    main_path = ur'c:\\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes'  # 注意\u前也要转义
    main_path = os.path.normpath(main_path)  #

    folder = ur'2C1B689D0EA74CAEBEAC84FE09D7A80'
    sub_folder = u'7B1597BFC05F4BD89113906CD0503CD'

    path = os.path.join(main_path, folder)
    info_path = os.path.join(path, u'Info')
    content_path = os.path.join(path, u'Content')

    path2 = os.path.join(path, u'Resources')
    sub_path = os.path.join(path2, sub_folder)

    print get_note_title_from_info(info_path)
    print type(get_note_title_from_info(info_path))
    print get_note_content_from_content(content_path)
    print get_res_info_from_resources(sub_path)

