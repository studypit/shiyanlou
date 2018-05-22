#!/usr/bin/env python3

from multiprocessing import Process, Pipe

conn1, conn2 = Pipe()

def f1():
    conn1.send('Great Ci Song')

def f2():
    data = conn2.recv()
    print(data)

def main():
    Process(target=f1).start()
    Process(target=f2).start()

if __name__ == '__main__':
    main() 
