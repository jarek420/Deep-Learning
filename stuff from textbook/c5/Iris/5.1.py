import numpy as np

#wczytanie pliku danych
with open("iris.data") as f:
    lines=[i[:-1] for i in f.readlines()]

#tworzenie wektora etykiet
n=["Iris-setosa","Iris-versicolor","Iris-virginica"]
x=[n.index(i.split(",")[-1]) for i in lines if i != ""]
x=np.array(x,dtype="uint8")


#tworzenie wektora cech jako macierz 150 x 4
y=[[float(j) for j in i.split(",")[:-1]]for i in lines if i !=""]
y=np.array(y)

i=np.argsort(np.random.random(x.shape[0]))
x=x[i]
y=y[i]

np.save("iris_features.npy",y)
np.save("iris_labels.npy",x)

