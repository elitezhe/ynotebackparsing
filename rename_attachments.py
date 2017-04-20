# -*- coding: utf-8 -*-

import sys
import os
import codecs
import logging
import shutil

from myconfig import ynote_bak_path
from ynoteutility import *

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert os.path.exists(ynote_bak_path)
    work_path = os.path.join(ynote_bak_path, 'Notes')
    # save_path = os.path.join(ynote_bak_path, 'new')
    save_path = os.path.join(ynote_bak_path, 'new2')
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    note_dirs = os.listdir(work_path)
    logging.debug(note_dirs)
    for adir in note_dirs:
        logging.info('Now deal with folder: ' + str(adir))
        cur_path = os.path.join(work_path, adir)
        info_path = os.path.join(cur_path, 'Info')
        note_title = get_note_title_from_info(info_path)
        logging.info(note_title)

        content_path = os.path.join(cur_path, 'Content')
        note_content = get_note_content_from_content(content_path)

        # new_note_folder_path = os.path.join(save_path, note_title)
        new_note_folder_path = save_path  # 所有笔记放在同一个文件夹中,不新建子目录了
        logging.debug(new_note_folder_path)
        if not os.path.exists(new_note_folder_path):
            os.mkdir(new_note_folder_path)

        new_note_file_path = os.path.join(new_note_folder_path, note_title+u'.html')
        with codecs.open(new_note_file_path, 'w', 'utf-8') as f:
            f.write(note_content)

        # 处理Resources中附件
        ress_path = os.path.join(cur_path, 'Resources')
        res_folders = os.listdir(ress_path)
        if len(res_folders) > 0:
            logging.info(res_folders)
            for r_path in res_folders:
                attach_path = os.path.join(ress_path, r_path)
                attach_info_path = os.path.join(attach_path, 'Info')
                attachment_path = os.path.join(attach_path, 'Content')
                attach_srieal = get_res_info_from_resources(attach_path)[0]  # 不要带Info结尾的路径 取第一个元素 得到类HASH的附件文件名
                # 复制附件到新文件夹
                new_attach_path = os.path.join(new_note_folder_path, attach_srieal)
                logging.info('attachment:' + attach_srieal)
                shutil.copy(attachment_path, new_attach_path)
        else:
            logging.info('No attachments!')

        # break

