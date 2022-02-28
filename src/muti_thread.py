import threading
import visit


class GetTodayStory(threading.Thread):
    def __init__(self, thread_id):
        threading.Thread.__init__(self)
        self.thread_id = thread_id

    def run(self):
        visit.get_today_story()
