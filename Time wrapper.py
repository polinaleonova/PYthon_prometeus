__author__ = 'polina'
def timeWrapper (func):
    import time
    def wrapper(*args, **kwargs):
        start = time.clock()
        func(*args, **kwargs)
        time_of_execution=time.clock()-start
        print 'Time of execution this function =', time_of_execution
    return wrapper

@timeWrapper
def tail(refer_last, n=3):
        refer_last = open(refer_last, 'rb')
        start = refer_last.tell()
        refer_last.seek(-0, 2)
        end = refer_last.tell()
        step = 20
        list_of_lines = []
        not_end = True
        while len(list_of_lines) != n + 1 and not_end:
            step = step if step <= end else end
            refer_last.seek(-step, 2)
            current = refer_last.tell()
            not_end = current != start
            list_of_lines = refer_last.readlines()
            step *= 2
        for x in list_of_lines[-n:]:
            print x.rstrip()

tail('New file from polina.txt', 10)
