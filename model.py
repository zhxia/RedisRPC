__author__ = 'zhxia'
import time

class test(object):
    def sum(self, *params):
        total = 0
        for it in params:
            total += it
        return total

    def getTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
