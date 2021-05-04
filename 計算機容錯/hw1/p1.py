x = [] ;
x.append(1) ;
print(range(10)) ;
N = 366 ;
for i in range(1,N) :
    if i <= 365 :
        x.append(x[i-1]*(366-i)/(365))
    else :
        x.append(x[i-1])

    if (1 - x[i]) >= 0.5**(i) :
        print (i) ;
        break ;

