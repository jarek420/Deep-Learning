import numpy as np
from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB, MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC


def run(x_train,y_train,x_test,y_test,clf):
    clf.fit(x_train,y_train)
    print(" Przewidywania :",clf.predict(x_test))
    print(" Rzeczywiste etykiety:",y_test)
    print(" Ocena =%0.4f"%clf.score(x_test,y_test))
    print()

def main():
    x=np.load("iris_features.npy")
    y=np.load("iris_labels.npy")
    N=120
    x_train=x[:N]; x_test=x[N:]
    y_train=y[:N]; y_test=y[N:]
    xa_train=np.load("iris_train_features_augmented.npy")
    ya_train=np.load("iris_train_labels_augmented.npy")
    xa_test=np.load("iris_test_features_augmented.npy")
    ya_test=np.load("iris_test_labels_augmented.npy")

    print("Najblizszy centroid:")
    run(x_train,y_train,x_test,y_test,NearestCentroid())
    print("Klasyfikator k-NN (k=3): ")
    run(x_train,y_train,x_test,y_test,KNeighborsClassifier(n_neighbors=3))
    print("Naiwny klasyfikator Bayesa (gaussowski):")
    run(x_train,y_train,x_test,y_test,GaussianNB())
    print("Naiwny klasyfikator Baysa (wielomianowy): ")
    run(x_train,y_train,x_test,y_test,MultinomialNB())
    print("Klasyfikator drzewa decyzyjnego: ")
    run(x_train,y_train,x_test,y_test,DecisionTreeClassifier())
    print("klasyfikator lasu losowego (estimators=5):")
    run(xa_train,ya_train,xa_test,ya_test,RandomForestClassifier(n_estimators=5))

    print("Maszyna SVM (liniowa, C=1.0):")
    run(xa_train,ya_train,xa_test,ya_test,SVC(kernel="linear",C=1.0))
    print("Maszyna SVM (jądro RBF, C=1.0,gamma=0.25):")
    run(xa_train,ya_train,xa_test,ya_test,SVC(kernel="rbf",C=1.0,gamma=0.25))
    print("Maszyna SVM (jądro RBF, C=1.0,gamma=0.001, dane rozszerzone):")
    run(xa_train,ya_train,xa_test,ya_test,SVC(kernel="rbf",C=1.0,gamma=0.001))
    print("Maszyna SVM (jądro RBF, C=1.0,gamma=0.001, dane pierwotne):")
    run(x_train,y_train,x_test,y_test,SVC(kernel="rbf",C=1.0,gamma=0.001))

main()
