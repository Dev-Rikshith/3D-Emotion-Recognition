#Importing Basic Libraries
import os
import sys
import math

#Import numpy for computation functions
import numpy as np

#Importing functions from supporting files
import analysis_functions as af

#Function to preprocess the data
def data_preprocessing(data_dir, data_type):
    #Lists to store processed data and the labels
    processed_data = []
    labels = []

    #Loop through directories in the data directory
    for directory in os.listdir(data_dir):
        sub_dir  = os.path.join(data_dir, directory)
        #Check if it's a directory
        if not os.path.isdir(sub_dir):
            continue
        #Loop through subjects in the sub-directory
        for subject in os.listdir(sub_dir):
            expr_dir = os.path.join(sub_dir, subject)
            #Check if it's a directory
            if not os.path.isdir(expr_dir):
                continue
            #Loop through files in the expression directory
            for expr_file in os.listdir(expr_dir):
                #Check if file ends with ".bnd"
                if expr_file.endswith(".bnd"):
                    file_path = os.path.join(expr_dir, expr_file)

                    #Read coordinates from the file
                    coordinates = read_file(file_path)

                    #Pass the coordinates to the process function according to the data_type
                    #provided by the user
                    modified_coordinates = process_data(coordinates, data_type)

                    #Flatten coordinates
                    flattened_coordinates = modified_coordinates.flatten()


                    #Append flattened coordinates to processed data
                    processed_data.append(flattened_coordinates)

                    #Append subject label to labels list
                    labels.append(subject)

    #Returning the processed data and labels by converting them into numpy arrays
    return np.array(processed_data), np.array(labels)


#Function to read coordinates from a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        #Saving coordinates in a list
        coordinates = []
        #Iterating over each line and storing each coordinates
        for line in file:
            coordinate = line.split(' ')
            #Appending each coordinate to the list
            coordinates.append(coordinate[1:])
            
    #Returning an array of coordinates
    return np.array(coordinates, dtype=float)

#Function to process data based on data type
def process_data(coordinates, data_type):
    if data_type == 'o':
        #Returning the original raw data
        return coordinates
    elif data_type == 't':
        #Returning the translated coordinates
        return translate_to_origin(coordinates)
    elif data_type == 'x' or data_type == 'y' or data_type == 'z':
        #Returning the rotated data on axis x, y, z as given by the user
        return rotate_data(coordinates, data_type)

#Function to translate coordinates to origin by subtracting the average coordinate
def translate_to_origin(coordinates):
    #Calculate the average coordinate for each dimension (x, y, z)
    avg_coordinate = np.mean(coordinates, axis=0)

    #Subtract the average coordinate from each coordinate to center the face at the origin
    translated_coordinates = coordinates - avg_coordinate

    #Returning the translated coordinates
    return translated_coordinates

#Function to rotate coordinates 180 degrees around x-axis, y-axis, and z-axis as given by the user
def rotate_data(coordinates, data_type):
    #Calculate PI
    Pi = round(2 * math.acos(0.0), 3)

    #Rotation matrices based on x, y, and z axes
    #Computing equation provided in the project
    if data_type == 'x':
        rotation_matrix = np.array([
            [1, 0, 0],
            [0, np.cos(Pi), np.sin(Pi)],
            [0, -np.sin(Pi), np.cos(Pi)]
        ])
    elif data_type == 'y':
        rotation_matrix = np.array([
            [np.cos(Pi), 0, -np.sin(Pi)],
            [0, 1, 0],
            [np.sin(Pi), 0, np.cos(Pi)]
        ])
    elif data_type == 'z':
        rotation_matrix = np.array([
            [np.cos(Pi), np.sin(Pi), 0],
            [-np.sin(Pi), np.cos(Pi), 0],
            [0, 0, 1]
        ])
    
    #Rotate coordinates around the respective axes
    rotated_coordinates = np.dot(rotation_matrix, coordinates.T).T

    #Returning the rotated-coordinates
    return rotated_coordinates