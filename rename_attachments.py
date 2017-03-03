# -*- coding: utf-8 -*-

import sys
import os
import codecs
import logging

from myconfig import ynote_bak_path
from ynoteutility import *

if __name__ == '__main__':
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    assert os.path.exists(ynote_bak_path)
    work_path = os.path.join(ynote_bak_path, 'Notes')
    save_path = os.path.join(ynote_bak_path, 'new')
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


        # break

