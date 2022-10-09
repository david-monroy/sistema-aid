from random import random
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import precision_score
from sklearn.model_selection import train_test_split
from PIL import Image, ImageDraw, ImageFont
from subprocess import check_call
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import accuracy_score
from sklearn import tree
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle
import matplotlib
matplotlib.use('SVG')
from tkinter.filedialog import asksaveasfilename

def entrenar(df):
    y = df['Probabilidad']
    x =df.drop(['Probabilidad'], axis=1)
    x.to_excel("backend/ia/patrones/data.xlsx")
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=123) 
    randomForest = RandomForestClassifier(max_depth=16, criterion="entropy", random_state=0, min_samples_split=100, min_samples_leaf=15,bootstrap=False)
    randomForest = randomForest.fit(X_train, y_train)
    save_classifier = open("backend/ia/patrones/RFClassifier", "wb")
    pickle.dump(randomForest, save_classifier)
    save_classifier.close()
    forest_training_preds = randomForest.predict(X_train)
    forest_training_accuracy = accuracy_score(y_train, forest_training_preds)
    return forest_training_accuracy


def exportarArbol():
    f = (open("backend/ia/patrones/RFClassifier", "rb"))
    classifier = pickle.load(f)
    f.close()
    data = pd.read_excel("backend/ia/patrones/data.xlsx")
    fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (10,10), dpi=800)
    tree.plot_tree(classifier.estimators_[0],
            feature_names = list(data), 
            class_names=['Poca probabilidad', 'Media', 'Mucha'],
            filled = True)
    file_name = asksaveasfilename(filetypes=[('*.png')], defaultextension='.png')
    fig.savefig(file_name)