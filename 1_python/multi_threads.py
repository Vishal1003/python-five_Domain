import multiprocessing
import time

def somefun(i):
    return i*i

def otherfun(m, i):
    return m+i

def process():
    for j in range(100):
        result = j
        for i in range(100000):
            result = otherfun(result, somefun(i))

if __name__ == "__main__":
    start = time.time()
    process()
    print("One process took %.2f s" % (time.time() - start))

    # Using multiprocessing : Dividing the tasks into batch of processes so that the result can be generator faster than expected

    start = time.time()
    processes = [multiprocessing.Process(target=process) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("Four processes run tool in %.2f sec" %(time.time() - start ))



