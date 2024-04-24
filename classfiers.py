#Importing Basic Libraries
import os
import sys
import math

#Importing KFold to compute Cross Fold Validation
from sklearn.model_selection import KFold

#Importing the classifiers needed
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier


def CrossFoldValidation(classifier, final_processed_data, final_label_data, k=10):
    
    #Instantiate the classifier based on the classifier-type provided by the user
    if classifier == "RF":
        #Random Forest Classifier
        clf = RandomForestClassifier()
    elif classifier == "SVM":
        #Support Vector Machine Classifier
        clf = SVC()
    elif classifier == "TREE":
        #Decision Tree Classifier
        clf = DecisionTreeClassifier()
    
    #Preprocessed features and labels
    X = final_processed_data
    y = final_label_data

    #Lists to store predictions and test-indices
    pred=[]
    test_indices=[]

    #Create a k-fold cross-validation splitter
    kf = KFold(n_splits = k)

    for i, (train_index, test_index) in enumerate(kf.split(X)):
        #Train the classifier on the training data
        clf.fit(X[train_index], y[train_index])
        #Predict labels for the test data
        pred.append(clf.predict(X[test_index]))
        #Store the test indices for later evaluation
        test_indices.append(test_index)

    #Return predictions, test indices, and true labels
    return pred, test_indices, y