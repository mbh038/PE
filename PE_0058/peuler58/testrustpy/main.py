from primal import is_prime
import time

def main():
    start = time.time()
    counter = 1
    side = 0
    nprimes = 0
    total = 1
    while True:
        side += 2
        for _ in range(4):
            counter += side
            total += 1
            if is_prime(counter):
                nprimes += 1
        if nprimes / total < 0.1:
            end = time.time()
            print("{}, time: {} s".format(side + 1, end - start))
            return

if __name__ == "__main__":
    main()