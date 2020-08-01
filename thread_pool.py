import multiprocessing
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED

#Creating a thread pool to manage calls equal to
class ThreadPool(object):

    def __init__(self, machine):
        self.outlets = machine.outlets_getter()
        self.pool = ThreadPoolExecutor(max_workers=self.outlets)
        m = multiprocessing.Manager()
        self.lock = m.Lock()
        self.machine = machine
        #futures denote number of threads running in parallel
        self.futures = []

    def make_beverage(self, name):
        try:
            future = self.pool.submit(self.machine.make_beverage, name, self.lock)
            if not future.done():
                self.futures.append(future)
        except:
            print("Something is wrong with the machine")

    #This function returns true if there are less beverages being made in parallel than outlets number, else false
    def isPoolAvailable(self):
        #We remove finished threads from futures variables
        self.futures = [future for future in self.futures if future._state=="RUNNING"]
        #If there are already n(outlets) number of beverages being brewed, we don't want to brew more
        if len(self.futures) >= self.outlets:
            return False
        else:
            return True
