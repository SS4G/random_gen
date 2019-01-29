import random
import sys
if __name__ == "__main__":
    FILE_NUM = 520
    with open("rec.dat", "r") as f:
        nums = set([int(i.strip()) for i in f.readlines()])
    if len(nums) == FILE_NUM:
        print("file use up！")
        sys.exit(1)
        
    while True:
        rand_num = random.randint(0, FILE_NUM - 1)
        if rand_num not in nums:
            print("got {0} enjoy".format(rand_num))
            nums.add(rand_num)
            break
        
    with open("rec.dat", "w") as f:
        for n in nums:
            f.write("{0}\n".format(n))
            