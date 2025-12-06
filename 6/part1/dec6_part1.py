import os
import time
from functools import reduce
import operator

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def parseInput():
    return [[v.strip() for v in l.split(' ') if v != ''] for l in lines]

def solveProblem(problem):
    if problem[-1] == '+':
        return sum([int(c) for c in problem[:-1]])
    else:
        return reduce(operator.mul, [int(c) for c in problem[:-1]], 1)
    
def main():
    problems = parseInput()
    nbProblems = len(problems[0])
    s = 0
    for i in range(nbProblems):
        problem = [p[i] for p in problems]
        s += solveProblem(problem)
    return s



if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()