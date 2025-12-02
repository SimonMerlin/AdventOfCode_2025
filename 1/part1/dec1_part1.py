import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def main():
    zeroCounter = 0
    pointer = 50
    for l in lines:
        direction = l[0]
        ticks = int(l[1:])
        if direction == 'L': #LEFT
            pointer -= ticks
            if pointer < 0:
                pointer += 100* (-1*(pointer//100))
        elif direction == 'R': #RIGHT
            pointer += ticks
            if pointer >= 100:
                pointer -= 100*(pointer//100)
        if pointer == 0:
            zeroCounter += 1
    return zeroCounter

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()