import os
import muti_thread


if __name__ == '__main__':
    lst = list()
    lst.append('https://www.ign.com/articles/pokemon-scarlet-and-pokemon-violet-announced-for-late-2022')
    muti_thread.visit_page(lst)



