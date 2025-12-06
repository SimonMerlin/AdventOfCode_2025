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

def removeRangeOverlap(ranges):
    updatedRanges = []
    for r in ranges:
        if len(updatedRanges) > 0:
            for up in updatedRanges:
                if r[0]>=up[0] and r[1]<=up[1]: # case where r is entirely included in up
                    r = None
                    break
                elif r[0]==up[0] and r[1]==up[1]: # case where r equals up
                    r = None
                    break
                elif r[0]<up[0] and r[1]<=up[0]:  # case where r is smaller than up 
                    if r[1] == up[0]:
                        r = (r[0], up[0]-1)
                elif r[0]>=up[1] and r[1]>up[1]:  # case where r is larger than up 
                    if r[0] == up[1]:
                        r = (up[1]+1, r[1])
                elif up[0]<=r[0]<=up[1] and r[1]>up[1]: # case where the left bound is in up but the right bound is outside
                    r = (up[1]+1, r[1])
                elif r[0]<up[0] and up[0]<=r[1]<=up[1]: # case where the left bound is outside but the right bound is in up
                    r = (r[0], up[0]-1)
                elif r[0]<up[0] and r[1]>up[1]: # case where r encompasses up
                    r1 = (r[0], up[0]-1)
                    r2 = (up[1]+1, r[1])
                    ranges.append(r2)
                    r = r1
        if r is not None:
            updatedRanges.append(r)
    return updatedRanges

def main():
    parseInput()
    noOverlapRanges = removeRangeOverlap(ranges)
    return sum([(b-a)+1 for a,b in noOverlapRanges])
    

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()