###########################################
#
#    HW3
#           made by R07943034 2019/12/28
###########################################

import numpy as np
import matplotlib.pyplot as plt

def get_data(path):
    x = []
    y = []
    data = open(path)
    while 1:
        line = data.readline().split()
        if line==[]:
            break
        temp = []
        for i in line:
            temp.append(float(i))
        x.append([1]+temp[1:-1])
        y.append(float(line[-1]))
    return np.array(x), np.array(y)

def gradient(w, x, y):
    s = -y*np.dot(w.T, x)
    theta = 1/(1 + np.exp(-s))
    g = theta*(-y*x)
    return g

def logistic(w, x, y, ita=0.001, SGD=False):
    #print(np.shape(w), np.shape(x), np.shape(y))
    if SGD:
        n = np.random.randint(len(y))
        g = gradient(w, x[n], y[n])
        w = w - ita*g
    else:
        temp = np.zeros_like(w)
        for n in range(len(y)):
            temp += gradient(w, x[n], y[n])
        g = temp/len(y)
        w = w - ita*g
    return w

def error(w, x, y):
    predict_y = np.sign(np.dot(x, w))
    err = np.sum(predict_y!=y)/len(y)
    return err

def main(iteration=2000, ita=0.001, SGD=False):
    train_x, train_y = get_data("hw3_train.dat")
    test_x, test_y = get_data("hw3_test.dat")
    
    list_e_in = []
    list_e_out = []
    w = np.zeros_like(train_x[0])
    
    for i in range(iteration):
        if(i%500==0):
            print("iteration:", i)
        w = logistic(w, train_x, train_y, ita, SGD)
        e_in = error(w, train_x, train_y)
        e_out = error(w, test_x, test_y)
        list_e_in.append(e_in)
        list_e_out.append(e_out)
    print("Ein:", e_in)
    print("Eout:", e_out)
    
    return list_e_in, list_e_out
    
def plot(iteration, type, err_GD, err_SGD):
    plt.grid(True, which="both", axis="both")
    plt.xlabel("T")
    plt.ylabel(type)
    plt.axis([0,iteration,0,1])
    plt.plot(range(iteration), err_GD, color="red", label="GD")
    plt.plot(range(iteration), err_SGD, color="blue", label="SGD")
    plt.legend()
    plt.savefig(type+".png")
    plt.show()
    
if __name__ == '__main__':

    print("\nlinear regression with gradient descent")
    gd_e_in, gd_e_out = main(iteration=2000, ita=0.01, SGD=False)
    print("\nlinear regression with SGD")
    sgd_e_in, sgd_e_out = main(iteration=2000, ita=0.001, SGD=True)
    
    plot(2000, "Ein", gd_e_in, sgd_e_in)
    plot(2000, "Eout", gd_e_out, sgd_e_out)
    
    