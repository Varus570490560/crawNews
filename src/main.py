import os
import sys

import muti_thread


if __name__ == '__main__':
    lst = list()
    lst.append(sys.argv[1])
    muti_thread.visit_page(lst)

