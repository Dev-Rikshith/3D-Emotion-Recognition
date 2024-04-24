#Importing the necessary metric functions needed 
from sklearn.metrics import precision_score, recall_score, accuracy_score
from sklearn.metrics import confusion_matrix

#Import libraries needed to implement scatterplot
import matplotlib.pyplot as plt

#Function to print the confusion matrix
def PrintEvalMetrics(pred, indices, y):
    #Manually merge predictions and testing labels from each of the folds to make confusion matrix
    finalPredictions = []
    groundTruth = []

    for p in pred:
        #Extend the final predictions list with predictions from each fold
        finalPredictions.extend(p)
    for i in indices:
        #Extend the ground truth list with labels from each fold
        groundTruth.extend(y[i])

    #Compute and print the confusion matrix
    print(confusion_matrix(finalPredictions, groundTruth))

    #Compute and print precision-score, recall-score, and accuracy-score
    print("Precision: ", precision_score(groundTruth, finalPredictions, average='macro'))
    print("Recall: ", recall_score(groundTruth, finalPredictions, average='macro'))
    print("Accuracy: " , accuracy_score(groundTruth, finalPredictions))

#Function to implement a 3D scatter plot
def plotter(data_to_plot):

    #Reshaping and getting the data ready to plot
    axis = data_to_plot[0].reshape(-1, 3)

    #Extracting x, y, and z coordinates from the reshaped data
    x = axis[:, 0]
    y = axis[:, 1]
    z = axis[:, 2]

    #Defining the plot and adding 3d projection to it
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    #Scattering the data provided
    ax.scatter(x, y, z)

    #Setting the x, y, z labels
    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    
    #Setting the title of the plot
    ax.set_title('3D Scatter Plot')

    #Showing or displaying the plot
    plt.show()
