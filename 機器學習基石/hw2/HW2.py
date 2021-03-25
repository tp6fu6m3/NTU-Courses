###########################################
#
#    HW2
#           made by R07943034 2019/12/05
###########################################

import numpy as np
import random
import matplotlib.pyplot as plt

DATA_SIZE = 2000
REAPEAT = 1000
NOISE = 0.2

def get_dataset(size):
    dataset = [[] for i in range(2)]
    for i in range(size):
        x = random.uniform(-1, 1)
        y = np.sign(x)*np.sign(random.uniform(0, 1)-NOISE)
        dataset[0].append(x)
        dataset[1].append(y)
    return dataset

def get_theta(dataset):
    temp = np.sort(dataset[0])
    theta = [0. for i in range(DATA_SIZE)]
    for i in range(DATA_SIZE-1):
        theta[i] = (temp[i]+temp[i+1])/2
    theta[-1] = 1
    return theta

def error(dataset, theta):
    dataset = np.array(dataset)
    theta = np.array(theta)
    E = np.zeros((2, DATA_SIZE))
    for i in range(DATA_SIZE):
        h = dataset[1]*np.sign(dataset[0]-theta[i])
        #error rate = n/(p+n) = ((p+n)-(p-n))/(2*(p+n))
        E[0][i] = (DATA_SIZE - np.sum(h))/(2*DATA_SIZE)     #s=1
        E[1][i] = (DATA_SIZE - np.sum(-h))/(2*DATA_SIZE)    #s=-1
    if np.min(E[0]) < np.min(E[1]):
        e_in = np.min(E[0])
        e_out = 0.5+0.3*(np.abs(theta[np.argmin(E[0])])-1)
    else:
        e_in = np.min(E[1])
        e_out = 0.5-0.3*(np.abs(theta[np.argmin(E[1])])-1)
    return e_in, e_out

if __name__ == '__main__':
    list_e_in = []
    list_e_out = []
    for i in range(REAPEAT):
        dataset = get_dataset(DATA_SIZE)
        theta = get_theta(dataset)
        e_in, e_out = error(dataset, theta)
        list_e_in.append(e_in)
        list_e_out.append(e_out)
    print("Ein:", sum(list_e_in)/REAPEAT)
    print("Eout:", sum(list_e_out)/REAPEAT)
    
    plt.hist(np.array(list_e_in)-np.array(list_e_out))
    plt.savefig("Ein-Eout.png")
    