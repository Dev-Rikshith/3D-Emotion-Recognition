# @author Rikshith Tirumanpuri
# @course Affective Computing

#Importing Basic Libraries
import os
import sys
import math

#Importing functions from supporting files
import data_preprocessing as dp
import classfiers as cls
import analysis_functions as af

#Program starts here
def main():
    #Checking the number of arguments and throwing an error if they are more or less
    no_of_args = len(sys.argv)
    if no_of_args < 4:
        print("Fewer arguments passed")
        sys.exit(1)
    elif no_of_args > 4:
        print("More arguments passed")
        sys.exit(1)
        
    #Storing the <classifier-type>, <data-orientation>, <data-directory> into the variables
    classifier_type, data_type, data_dir = sys.argv[1], sys.argv[2], sys.argv[3]

    #Calling the data reading and preprocessing functions and retrieving and processing
    #the data according the <data-orientation> given by the user
    final_processed_data, final_label_data = dp.data_preprocessing(data_dir, data_type)

    #Function to plot data
    # af.plotter(final_processed_data)

    #Debugging statements to print the processed data and its length
    #print(final_processed_data.shape)
    #print(final_label_data.shape)

    #print(len(final_processed_data))
    #print(len(final_label_data))

    #calling the Cross Validation function with the <classifier-type> provided by the user and
    #the preprocessed data from the previous step
    pred, test_indices, y = cls.CrossFoldValidation(classifier_type, final_processed_data, final_label_data)

    #Using the analysis functions provided in the project, we are printing the 
    #confusion matrix, precision-score, recall-score, accuracy-scores
    af.PrintEvalMetrics(pred, test_indices, y)
    

#Calling the main function
if __name__ == "__main__":
    main()




