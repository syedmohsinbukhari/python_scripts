import os
import math
import time
import sys

class ProgressBar:

    def __init__(self, num_iterations, func, *args):
        self.num_iterations = num_iterations
        self.func = func
        self.args = args

    def disp_prog(self, k, n):
        rows, columns = os.popen('stty size', 'r').read().split()
        w=int(columns)
        c=0
        if k>n or w<10:
            return
        m=w-8
        print('\r', end='')
        for i in range(w):
            print(' ', end='')
        print('\r[', end='')
        c+=1
        r = k/n
        b = round(r*m)
        g = range(b)
        for i in g:
            print('-', end='')
            c+=1
        print('>', end='')
        c+=1
        while (w-c)>6:
            print(' ', end='')
            c+=1
        print(']', end='')
        c+=1
        print(' ', end='')
        c+=1
        if r<1:
            print(' ', end='')
            t=math.floor(r*10)
            o=math.floor(10*((r*10)-t))
        else:
            print('1', end='')
            t=0
            o=0
        c+=1
        if r<0.1:
            print(' ', end='')
        else:
            print(t, end='')
        c+=1
        print(o, end='')
        c+=1
        print('%', end='')
        c+=1
        sys.stdout.flush()
        return c

    def execute(self):
        n = self.num_iterations
        for i in range(n):
            self.disp_prog(i, n)
            self.func(*self.args)
        self.disp_prog(n, n)
        print()
        sys.stdout.flush()

args_arr = [1]
prog_bar = ProgressBar(10, time.sleep, *args_arr)
prog_bar.execute()
