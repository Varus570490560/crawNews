import os
import muti_thread


if __name__ == '__main__':
    muti_thread.GetTodayStory(0).start()
    os.system('mitmweb -s ./src/proxy.py;')



