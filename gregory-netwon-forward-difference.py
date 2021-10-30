import numpy as np

x = np.loadtxt('dati_1.txt')[:,0]
f = np.loadtxt('dati_1.txt')[:,1]

x_o = 0.55
h = x[1] - x[0]
n = 8 #degree of the polynomial
#if n >= len(x):
#    print('NO!!!!!')


#find the index of the closest point
def find_index(x_o = x_o):
    #print(h)
    diff = h
    for i in range(0,len(x)):
        #print(i)
        if diff*(-0.5)< np.abs(x_o - x[i]) < diff*0.5:
            #diff = np.abs(x_o - x[i])
            #print(diff)
            index = i
    return index


def gregory_netwon_forward_difference(x=x,f=f,x_o=x_o):
    f = f.copy()
    #print(f)
    #h = x[1] - x[0]
    j = find_index(x_o)
    #print(j)
    r = (x_o - x[j])/h
    #print(r)
    
    results = np.zeros(n)
    errors = np.zeros(n)
    fx_o = f[j]
    c = 1
    
    for i in range(n):
        print(("%g° degree finite differences") % (i+1))
        #print(" ")
        c *= (r-i)/(i+1)
        #print(("c %8.3f")%(c))
        #print(" ")
        for k in range(n-i):
            #print("... k",k)
            f[k] = f[k+1] - f[k] #computing the forward difference
            print(('%f')%(f[k]))  
        #j=0
        #print(f)
        fx_o += c*f[0]
        error = np.abs(c*f[0])
        print(" ")
        #print(" ")
        results[i] = fx_o
        errors[i] = error
    
    print(" ")
    print(("fx_o was estimated to be: %10.7f +- %10.7f")%(fx_o, error))
    return results, errors


results, errors = gregory_netwon_forward_difference()


## Risposta (b)
a = 0.786488
for i in range(n):
    print(("%g degree, solution: %10.7f, error: %10.7f")%(i+1, results[i], errors[i]))


## Risposta (c)
a = 1.606830
for i in range(0,n):
    b = results[i]
    difference = abs(a-b)
    error = errors[i]
    print(("%g degree, interpolation error: %10.7f, difference with real solution: %10.7f")%(i+1, error, difference))



