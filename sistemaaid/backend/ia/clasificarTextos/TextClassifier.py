from asyncio.windows_events import NULL
import pandas as pd
import pickle
from nltk import  word_tokenize
from nltk import NaiveBayesClassifier as nbc
from nltk.classify.scikitlearn import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB
import nltk
nltk.download('punkt')
from sklearn.model_selection import train_test_split 

##datos = pd.read_csv('train.csv', header=0,encoding='ISO-8859-1', delimiter=';')
vocabulary = []
array_words = []

def tokenization(df):
    for row in df.index:
        words = word_tokenize(df['respuesta'][row].lower())
        for word in words:
            vocabulary.append(word)
    return vocabulary

def tags(df):
    for row in df.index:
        print(row)
        array = ({i: (i in word_tokenize(df['respuesta'][row].lower())) for i in vocabulary}, df['Clasificación'][row])
        array_words.append(array)


def train(df, fileName):
    train, test = train_test_split(df, test_size = 0.20)
    tokenization(train)
    tags(train)
    SKClassifier = SklearnClassifier(MultinomialNB())
    SKClassifier.train(array_words)
    save_classifier = open("backend/ia/clasificarTextos/"+ fileName, "wb")
    pickle.dump(SKClassifier, save_classifier)
    save_classifier.close()
    return ("success")


def predict(df,fileName): 
    f = (open("backend/ia/clasificarTextos/"+ fileName, "rb"))
    classifier = pickle.load(f)
    f.close()
    vocabulary = tokenization(df)
    df["Prediccion"] = NULL
    for row in df.index:
        sentence = {i: (i in word_tokenize(df['respuesta'][row].lower())) for i in vocabulary}
        df['Prediccion'][row]=classifier.classify(sentence)
    return df



 
       

      





   





