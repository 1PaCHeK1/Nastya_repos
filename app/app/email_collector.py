import os
import time
import threading


class EmailThread(threading.Thread):

    def __init__(self, timeout):
        super().__init__()
        self.tasks = []
        self.timeout = timeout

    def run(self):
        while True:
            task = None
            if self.tasks:
                task = self.tasks.pop(0)
            if task is not None:
                task()
                time.sleep(self.timeout)

    def append_task(self, task):
        self.tasks.append(task)


class EmailCollector:
    
    def __init__(self):
        self.email_from = os.environ.get("EMAIL_SENDER")
        self.password = os.environ.get("EMAIL_PASSWORD")
        self.email_client = print
        self.max_messages = 20
        self.timeout = 60 / self.max_messages
        self.thread = EmailThread(self.timeout)
        self.thread.start()

    def __new__(cls):
        if hasattr(cls, "instance"):
            return cls.instance
        cls.instance = super().__new__(cls)
        return cls.instance

    def append_email(self, to_email, message):
        self.thread.append_task(lambda: self.email_client(to_email, message))
        
    
    def extend_email(self, to_emails, message):
        self.email_client(to_emails, message)


a = EmailCollector()
print("point 1")

a.append_email("a", "b")
print("point 2")

a.append_email("c", "d")

print("point 3")

a.append_email("c", "d")
