# Load libraries
import pandas as pd
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
from pickle import dump
import databaseHandler as dbHandler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.naive_bayes import GaussianNB,MultinomialNB,ComplementNB,BernoulliNB,CategoricalNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from datetime import datetime

def classificationDesionTree():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    # load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5) # 80% training and 20% test

    # Create Decision Tree classifer object
    clf = DecisionTreeClassifier(criterion="gini",max_depth =None)
    #gini
    #entropy

    # Train Decision Tree Classifer
    clf = clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))
    print()
    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))


def classificationSVM():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) # 80% training and 20% test

    clf=SVC(kernel='poly')
    clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))

def classificationGaussianNaiveBayes():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) # 80% training and 20% test

    clf=GaussianNB()
    clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))


def classificationMultinomialNaiveBayes():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) # 80% training and 20% test

    clf=MultinomialNB()
    clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))

def classificationComplementNaiveBayes():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) # 80% training and 20% test

    clf=ComplementNB()
    clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))


def classificationBernoulliNaiveBayes():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) # 80% training and 20% test

    clf=BernoulliNB()
    clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))

def classificationCategoricalNaiveBayes():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4) # 80% training and 20% test

    clf=CategoricalNB()
    clf.fit(X_train,y_train)

    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))


def classificationRandomForest():
    col_names = ['*','web1','web2','cosine', 'len', 'word', 'sameDomain', 'label']
    #load dataset
    pima = pd.read_csv("data.csv",  names=col_names)

    #split dataset in features and target variable
    feature_cols =['cosine', 'len', 'word', 'sameDomain']
    X = pima[feature_cols] # Features
    y = pima.label # Target variable

    #Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5) # 80% training and 20% test

    clf=RandomForestClassifier()
    clf.fit(X_train,y_train)
    # save the model
    dump(clf, open('model.pkl', 'wb'))
    startTime=datetime.now()
    #Predict the response for test dataset
    y_pred = clf.predict(X_test)
    endTime=datetime.now()

    print("exec time :",endTime-startTime)

    #Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    print("precision:",metrics.average_precision_score(y_test, y_pred))

    print("recall:",metrics.recall_score(y_test, y_pred))

    print()

    print(confusion_matrix(y_test, y_pred))
    #print(classification_report(y_test, y_pred))