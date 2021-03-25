import numpy as np
import matplotlib.pyplot as plt
import random

def split_data(filename):
    x = []
    y = []
    data = open(filename)
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

def pocket(w, x, y):
    w_temp = w.copy()
    indexs = list(range(len(x)))
    
    updates = 100
    while(updates>0):
        random.shuffle(indexs)
        for i in indexs:
            sign = 0
            if(np.dot(w_temp,x[i])>0):
                sign = 1
            else:
                sign = -1
            if(sign!=y[i]):
                w_temp += y[i]* x[i]
                updates -= 1
                error = test(w, x, y)
                error_temp = test(w_temp, x, y)
                if(error_temp<error):
                    w = w_temp.copy()
                #print(updates)
    return w

def test(w, x, y):
    count = 0
    for i in range(len(x)):
        sign = 0
        if(np.dot(w,x[i])>0):
            sign = 1
        else:
            sign = -1
        if(sign!=y[i]):
            count += 1
    return count

if __name__ == '__main__':
    train_x,train_y = split_data("hw1_7_train.dat")
    test_x,test_y = split_data("hw1_7_test.dat")
    
    error_list = []
    repeat = int(input("Repeat times: "))
    for i in range(repeat):
        w = np.array([0,0,0,0,0],dtype=float)
        w_pocket = pocket(w, train_x, train_y)
        
        error_test = test(w_pocket, test_x, test_y)/len(test_x)
        print(i+1, "times error:", error_test)
        error_list.append(error_test)
    print("average error:", sum(error_list)/repeat)
    plt.hist(error_list)
    plt.savefig("error_histogram.png")
    