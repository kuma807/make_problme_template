import random
import numpy as np
random.seed(334)

def write_testcase(file_name, testcase):
    with open(file_name, "w") as f:
        f.write(testcase)

def random_AB():
    for i in range(0, 5):
        A = random.randint(1, 100000)
        B = random.randint(1, 100000)
        testcase = f"{A} {B}"
        write_testcase(f"../in/random{i}.txt", testcase)

def big_random_AB():
    for i in range(0, 5):
        A = random.randint(10000, 100000)
        B = random.randint(10000, 100000)
        testcase = f"{A} {B}"
        write_testcase(f"../in/big_random{i}.txt", testcase)

if __name__ == '__main__':
    random_AB()
    big_random_AB()
