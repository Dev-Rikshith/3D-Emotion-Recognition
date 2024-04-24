Packages list used:

scikit-learn
matplotlib
numpy

To run commands manually:

python Project1.py RF o BU4DFE_BND_V1.1
python Project1.py RF t BU4DFE_BND_V1.1
python Project1.py RF x BU4DFE_BND_V1.1
python Project1.py RF y BU4DFE_BND_V1.1
python Project1.py RF z BU4DFE_BND_V1.1
python Project1.py SVM o BU4DFE_BND_V1.1
python Project1.py SVM t BU4DFE_BND_V1.1
python Project1.py SVM x BU4DFE_BND_V1.1
python Project1.py SVM y BU4DFE_BND_V1.1
python Project1.py SVM z BU4DFE_BND_V1.1
python Project1.py TREE o BU4DFE_BND_V1.1
python Project1.py TREE t BU4DFE_BND_V1.1
python Project1.py TREE x BU4DFE_BND_V1.1
python Project1.py TREE y BU4DFE_BND_V1.1
python Project1.py TREE z BU4DFE_BND_V1.1

Note: run_command.sh is a bash script to run all the commands automatically and write the results to the file named "script_log.txt"

File Names and what they do:

Project1.py: It is the main file where the program exection starts (main function), processes the data according to the user inputs and trains the appropriate classifier and provides the metrics and confusion matrix.

Data_preprocessing.py: It is file that contains the data preprocessing functions of the data, which navigates to the folder where .bnd files are present and reads the data and processes them according to the user needs such as original, translated, rotated X or Y or Z and returns the data in the form of compact np arrays.

classifiers.py: It has the necessary classifier declarations and passing it the the cross validation functions for the processing.

analysis_functions.py: These are functions provided on the Canvas under the project, it has functions to print the required metrics, confusion matrix and I have also added the plot function to this which plots each sample of a subject(Original, Translated, Rotated X, Rotated Y, Rotated Z)

Sample_Data: It is the folder which has the subset of the original dataset for faster runtime to use for the purpose of debugging.

Data_Plots: It is the folder that has the data of one subject that is used for plotting and all the png images of the plots.

Results: It is the folder which has .txt files with results (confusion matrix, metrics) sorted with respect to the classifier.

Affective Computing - Project 1: This is the report for the project which has the results, questions and plots all at one place.


Note: Static Code for reference, data is protected under a license