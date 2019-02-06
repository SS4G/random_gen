import random
import os
import datetime as dt
if __name__ == "__main__":
    FILE_NUM = 520
    ts = dt.datetime.now().strftime("%Y%m%d-%H:%M:%S")
    with open("rec.dat", "r") as f:
        lines = [i for i in f.readlines()]
        nums = set([int(line.strip().split("\t")[0]) for line in lines])
        
    if len(nums) == FILE_NUM:
        print("file use up！")
        sys.exit(1)
        
    rand_num = None
    while True:
        rand_num = random.randint(0, FILE_NUM - 1)
        if rand_num not in nums:
            print("got {0} enjoy".format(rand_num))
            break
        
    with open("rec.dat", "w") as f:
        lines.append("{0}\t{1}\n".format(rand_num, ts))
        for line in lines:
            f.write(line)
            
    os.system("git add .; git commit -m {0}; git push origin master".format(ts))
            
