#listing 4.2 Losowe konstruowanie pozdzbiorow uczacego, walidacyjnego i testowego
import numpy as np
from sklearn.datasets import make_classification

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
