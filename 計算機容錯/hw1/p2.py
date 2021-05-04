import matplotlib.pyplot as plt



def bigTruck (rate) :
    result = rate**18 + 18*(1-rate)*(rate**17) + 18*17*0.5*((1-rate)**2)*(rate**16)
    return result

def smallTruck (rate) :
    result = rate**4 + 4*(1-rate)*(rate**3)
    return result ;

b = []
s = []
r = []

for i in range(1,1000,1) :
    # rate of working fine of a tire
    rate =  1 - i / 1000
    r.append(rate)
    b.append(bigTruck(rate))
    s.append(smallTruck(rate))

for i in range(len(s)) :
    if s[i] < b[i] :
        print(r[i])

plt.plot(r,b,'b*',r,s,'g+');
plt.show()
