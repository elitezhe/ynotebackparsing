# -*- coding: utf-8 -*-

import codecs
import string
import logging
import sys
import os


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
    note_title = info_str[0:title_rindex]
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
        info_bytes = f.read()
    info_str = codecs.decode(info_bytes, 'utf-16', 'ignore')
    tmp_info_list = list(info_str)
    for idx, c in enumerate(tmp_info_list):
        if c not in string.printable:
            tmp_info_list[idx] = u'/'
    # Now we get pure utf info_str
    info_str = u''.join(tmp_info_list)
    info_str_splited = string.split(info_str, u'/')
    info_list = []
    for tmp in info_str_splited:
        if not tmp == u'':
            info_list.append(tmp)
    return info_list[0:2]  # 此处未做有效性检验


if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

    # path = r'C:\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes\0E432AED88124A51973961CDA3ACDE1\Info'
    # title = get_note_title_from_info(path)
    #
    # print title
    # print type(title)
    #
    # cont_path1 = r'C:\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes\0E432AED88124A51973961CDA3ACDE1\Content'
    # content = get_note_content_from_content(cont_path1)
    # print content
    #
    # res_path = r'C:\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes\0E432AED88124A51973961CDA3ACDE1\Resources\66A38ADC69F64324ACCB6ED24C1DCCC'
    # res_info = get_res_info_from_resources(res_path)
    # print res_info
    # print res_info
    # print string.split(res_info, u' ')
    # print res_info[2:3] in string.printable
    # res_list = list(res_info)
    # print res_list
    # index = 0
    # for c in res_list:
    #     if c not in string.printable:
    #         res_list[index] = u' '
    #     index += 1
    # print res_list
    # print len(res_info), len(res_list)
    # res_info = u''.join(res_list)
    # print repr(res_info)
    # res_list2 = string.split(res_info, u' ')
    # print res_list2
    # res_list3 = []
    # for r in res_list2:
    #     if r is None:
    #         pass
    #     else:
    #         res_list3.append(r)
    # print 'res3 is: ', res_list3

    # 2BEA622B6A3A4B62907BE83FF46794B CAC7EDDA72454468B8CD4697743E5F3 手写笔记 有问题,分割符+
    # 2C1B689D0EA74CAEBEAC84FE09D7A80 Resources 7B1597BFC05F4BD89113906CD0503CD
    #
    main_path = r'C:\Users\Zhe Zhang\Desktop\yd\final\youdao_note_20170303\Notes'
    folder = ur'2C1B689D0EA74CAEBEAC84FE09D7A80'
    sub_folder = u'7B1597BFC05F4BD89113906CD0503CD'

    path = os.path.join(main_path, folder)
    info_path = os.path.join(path, u'Info')
    content_path = os.path.join(path, u'Content')

    path2 = os.path.join(path, u'Resources')
    sub_path = os.path.join(path2, sub_folder)

    print get_note_title_from_info(info_path)
    print get_note_content_from_content(content_path)
    print get_res_info_from_resources(sub_path)

