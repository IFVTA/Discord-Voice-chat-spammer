import time
import discord
import asyncio
import logging
import youtube_dl
from token1 import*
from token2 import*
from token3 import*
from token4 import*
from token5 import*
from token6 import *
from token7 import *
from token8 import *
from token9 import *
from token10 import *

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
from threading import Thread
from queue import Queue

class Worker(Thread):
    """
    Pooling
    """

    def __init__(self, tasks):
        Thread.__init__(self)
        self.tasks = tasks
        self.daemon = True
        self.start()

    def run(self):
        while True:
            func, args, kargs = self.tasks.get()
            try:
                func(*args, **kargs)
            except Exception as ex:
                pass
            finally:
                self.tasks.task_done()

class ThreadPool:
    """
    Pooling
    """

    def __init__(self, num_threads):
        self.tasks = Queue(num_threads)
        for _ in range(num_threads):
            Worker(self.tasks)

    def add_task(self, func, *args, **kargs):
        """
        Add a task to be completed by the thread pool
        """
        self.tasks.put((func, args, kargs))

    def map(self, func, args_list):
        """
        Map an array to the thread pool
        """
        for args in args_list:
            self.add_task(func, args)

    def wait_completion(self):
        """
        Await completions
        """
        self.tasks.join()

def one():
    time.sleep(1)
    client1.run(token1, bot=False)

def two():
    time.sleep(2)
    client2.run(token2, bot=False)

def three():
    time.sleep(3)
    client3.run(token3, bot=False)

def four():
    time.sleep(4)
    client4.run(token4, bot=False)

def five():
    time.sleep(5)
    client5.run(token5, bot=False)

def six():
    time.sleep(6)
    client6.run(token6, bot=False)

def seven():
    time.sleep(7)
    client7.run(token7, bot=False)

def eight():
    time.sleep(8)
    client8.run(token8, bot=False)

def nine():
    time.sleep(9)
    client9.run(token9, bot=False)

def ten():
    time.sleep(10)
    client10.run(token10, bot=False)
  
pool = ThreadPool(10)
pool.add_task(one)
pool.add_task(two)
pool.add_task(three)
pool.add_task(four)
pool.add_task(five)
pool.add_task(six)
pool.add_task(seven)
pool.add_task(eight)
pool.add_task(nine)
pool.add_task(ten)
pool.wait_completion()














