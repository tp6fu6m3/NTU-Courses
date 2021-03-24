import numpy as np
import matplotlib.pyplot as plt
import random

def split_data():
    x = []
    y = []
    data = open("hw1_6_train.dat")
    while 1:
        line = data.readline()
        if line=="":
            break
        line = line[:-1].split("\t")
        line[0] = list(map(float, line[0].split()))
        x.append([1] + line[0])
        y.append(int(line[1]))
    #print(x, y)
    return np.array(x), np.array(y)

def PLA(w, x, y):
    updates = 0
    no_error = False
    while(not no_error):
        no_error = True
        indexs = list(range(len(x)))
        random.shuffle(indexs)
        for i in indexs:
            sign = 0
            if(np.dot(w,x[i])>0):
                sign = 1
            else:
                sign = -1
            if(sign!=y[i]):
                w += y[i]* x[i]
                updates += 1
                no_error = False
                #print(updates)
    return w, updates

if __name__ == '__main__':
    x, y = split_data()
    updates_list = []
    repeat = int(input("Repeat times: "))
    for i in range(repeat):
        w = np.array([0,0,0,0,0],dtype=float)
        w_pla, updates = PLA(w, x, y)
        print(i+1, "times update:", updates)
        updates_list.append(updates)
    print("average update:", int(sum(updates_list)/repeat))
    plt.hist(updates_list)
    plt.savefig("update_histogram.png")
    