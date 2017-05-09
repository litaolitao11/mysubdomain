#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# import time

# print time.time()


# class Alimal(object):
#     """super class"""
#     def __init__(self):
#         pass

#     def run(self):
#         print 'Alimal is running! '


# class Person(Alimal):
#     def __init__(self, hight):
#         self.hight = hight
#         self.fun1()

#     def show(self):
#         print self.hight

#     def fun1(self):
#         print 'this is fun1'

#     @classmethod
#     def fun2(self):
#         print 'this is fun2'


# litao1 = Person('170')
# litao1.fun2()
# Person.fun2()



# from multiprocessing import Process, Queue
# import os
# import time
# import random


# def write(q):
#     for value in [1, 2, 3]:
#         print 'Put (%d) queue...' % value
#         q.put(value)
#         time.sleep(random.random())

# def read(q):
#     while True:
#         value = q.get(True)
#         print 'Get %s from queue...' % value

# if __name__ == '__main__':
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     pw.start()
#     pr.start()
#     pw.join()
#     pr.terminate()
# import time, threading

# 新线程执行的代码:
# def loop():
#     print 'thread %s is running...' % threading.current_thread().name
#     n = 0
#     while n < 5:
#         n = n + 1
#         print 'thread %s >>> %s' % (threading.current_thread().name, n)
#         time.sleep(1)
#     print 'thread %s ended.' % threading.current_thread().name

# print 'thread %s is running...' % threading.current_thread().name
# t = threading.Thread(target=loop, name='LoopThread')
# t.start()
# t.join()
# print 'thread %s ended.' % threading.current_thread().name
# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()

# def process_student():
#     print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     local_school.student = name
#     process_student()

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# import threading

# local_school = threading.local()
# def process_student():
#     print 'Hello, %s(in %s)' % (local_school.student, threading.current_thread().name)
#     print str(threading.active_count()) + '======='
# def process_thread(name):
#     local_school.student = name
#     process_student()


# t1 = threading.Thread(target=process_thread, args=('litao',))
# t2 = threading.Thread(target=process_thread, args=('huangjie',))

# while  True:
#     if threading.active_count() <10:
#         t = threading.Thread(target=process_thread, args=('oooooooo',))
#         t.start()
# print threading.current_thread().name
# print threading.active_count()
# t1.start()
# t2.start()

# t1.join()
# t2.join()
# print 'aa'
# import Queue

# msg_queue = Queue.Queue()

# msg_queue.put(12)
# msg_queue.put(14)
# msg_queue.put(16)

# print msg_queue.get()
# print msg_queue.get()
# print msg_queue.get()

# with open('test_php.php') as f:
#     for line in f.xreadlines():
#         print line
# a = {'alphnum'}
# sub = 'bcd332'
# print sub.find('{alphnum}') 

# import dns.resolver

# resolver = dns.resolver.Resolver()
# resolver.lifetime = resolver.timeout = 20.0
# server = ['114.114.114.114']
# resolver.nameservers = [server]
# answers = resolver.query('public-dns-a.baidu.com')
# # test lookup a existed domain
# # if answers[0].address != '180.76.76.76':
# print answers[0].address


# import dns.resolver
# resolver = dns.resolver.Resolver()
# resolver.lifetime = resolver.timeout = 20.0
# server = '114.114.114.114'
# resolver.nameservers = [server]
# answers = resolver.query('www.baidu.com')    # test lookup a existed domain
# for _ in answers:
#     print type(_)

# a= 'asdf45;lj;fffff'
# print a.split(';')[-1]

# import sys
# sys.stdout.write('hello!')

# a = 'aabbcc'
# print a.startswith('aab')
sub = '{alphnum}'
sub = sub.replace('{alphnum}', '[a-z0-9]')
print sub