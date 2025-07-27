#lsiting 4.1 przeprowadzenie podzialu pierwotnych danych na podzbiory w stosunku 90/5/5
import numpy as np
from sklearn.datasets import make_classification
#utworzenbie sztucznego0 zestawu danych i podzielenie go na zbiory klas 0 i 1
a,b=make_classification(n_samples=10000,weights=(0.9,0.1))
idx=np.where(b==0)[0]
x0=a[idx,:]
y0=b[idx]
idx=np.where(b==1)[0]
x1=a[idx,:]
y1=b[idx]
#mieszanie losowo kolejnosc danych
idx=np.argsort(np.random.random(y0.shape))
y0=y0[idx]
x0=x0[idx]
idx=np.argsort(np.random.random(y1.shape))
y1=y1[idx]
x1=x1[idx]
#wydobywamy pierwszych 90% prob i budujemy podzbior
#danych uczacych gdzie w tablicy xtrn umieszcamy probyu
ntrn0=int(0.9*x0.shape[0])
ntrn1=int(0.9*x1.shape[0])
xtrn=np.zeros((int(ntrn0+ntrn1),20))
ytrn=np.zeros((int(ntrn0+ntrn1)))
xtrn[:ntrn0]=x0[:ntrn0]
xtrn[ntrn0:]=x1[:ntrn1]
ytrn[:ntrn0]=y0[:ntrn0]
ytrn[ntrn0:]=y1[:ntrn1]

n0=int(x0.shape[0]-ntrn0)
n1=int(x1.shape[0]-ntrn1)
xval=np.zeros((int(n0/2+n1/2),20))
yval=np.zeros((int(n0/2+n1/2)))
xval[:(n0//2)]=x0[ntrn0:(ntrn0+n0//2)]
xval[(n0//2):]=x1[ntrn1:(ntrn1+n1//2)]
yval[:(n0//2)]=y0[ntrn0:(ntrn0+n0//2)]
yval[(n0//2):]=y1[ntrn1:(ntrn1+n1//2)]

xtst=np.concatenate((x0[(ntrn0+n0//2):],x1[(ntrn1+n1//2):]))
ytst=np.concatenate((y0[(ntrn0+n0//2):],y1[(ntrn1+n1//2):]))

print(xtst)
print(ytst)
'''
#listing 4.2
#listing 4.2 Losowe konstruowanie pozdzbiorow uczacego, walidacyjnego
#i testowego

#wprowadzamy losowosc do sztucznego zestawu danych
x,y=make_classification(n_samples=10000,weights=(0.9,0.1))
idx=np.argsort(np.random.random(y.shape[0]))
x=x[idx]
y=y[idx]

#
ntrn=int(0.9*y.shape[0])
nval=int(0.05*y.shape[0])

xtrn=x[:ntrn]
ytrn=y[:ntrn]
xtrn=x[ntrn:(ntrn:(ntrn+nval))]
ytrn=y[ntrn:(ntrn:(ntrn+val))]

xtst=x[(ntrn+nval):]
ytst=y[(ntrn+nval):]
'''
