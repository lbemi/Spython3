import threading
import queue


class A(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print("I'm threading A!")


class B(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in range(10):
            print("I'm threading B  !")
# t1 = A()
# t = B()
# t1.start()
# t.start()
a = queue.Queue()
a.put("hello")
a.task_done()
a.put("1123")
a.task_done()
a.put("@#!@%%#")
a.task_done()

print(a.get())
print(a.get())
print(a.get())
