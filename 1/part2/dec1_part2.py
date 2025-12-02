import os
import time

f = open(os.path.dirname(__file__) + '/../input.txt', 'r')
lines = [l.rstrip() for l in f.readlines()]

def main():
    pointer = 50
    zeroCounter = 0
    previousDirection = None
    previousPointer = pointer

    for l in lines:
        direction = l[0]
        ticks = int(l[1:])
       
        if direction == 'L': #LEFT
            pointer -= ticks
            if pointer < 0 and (previousPointer != 0 or previousDirection == 'L'):
                zeroCounter += (-1*(pointer//100))
                if pointer % 100 == 0:
                    pointer = 0
                else:
                    pointer += 100* (-1*(pointer//100))
            if previousDirection == 'R' and previousPointer == 100:
                zeroCounter += 1
        elif direction == 'R': #RIGHT
            pointer += ticks
            if previousDirection == 'L' and previousPointer == 0:
                zeroCounter += 1
            if pointer > 100 and (previousPointer != 100 or previousDirection == 'R'):
                zeroCounter += pointer//100
                if pointer % 100 == 0:
                    pointer = 100
                    zeroCounter -= 1
                else:
                    pointer -= 100 * (pointer//100)
            
        previousDirection = direction
        previousPointer = pointer
    
    if pointer % 100 == 0:
        zeroCounter += 1

    return zeroCounter

if __name__ == '__main__': 
    start = time.perf_counter()
    print(main())
    end = time.perf_counter()
    print(f"Executed in {((end - start)*1000):0.2f} milliseconds")
    f.close()