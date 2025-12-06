import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

ranges = []
ids = []

def parseInput():
    i = 0
    while lines[i] != '':
        l = lines[i].split('-')
        ranges.append((int(l[0]), int(l[1])))
        i += 1
    i += 1
    while i < len(lines):
        ids.append(int(lines[i]))
        i += 1

def isFresh(id):
    for r in ranges:
        if r[0] <= id <= r[1]:
            return True
    return False

def main():
    parseInput()
    return sum(1 for id in ids if isFresh(id))
    

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()