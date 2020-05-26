# Let's say you want to download several pages of a website and compile them into a single phase
import requests
from threading import Thread
from queue import Queue

q = Queue(maxsize=20)

def put_page(page_num):
    q.put(requests.get('http://google.com/page_%s.html' %page_num))


def compile(q):
    if not q.full():
        raise ValueError

    else:
        print("Done Compiling")


threads = []
for page_num in range(20):
    t = Thread
    t = Thread(target=put_page, args=(page_num,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

compile(q)