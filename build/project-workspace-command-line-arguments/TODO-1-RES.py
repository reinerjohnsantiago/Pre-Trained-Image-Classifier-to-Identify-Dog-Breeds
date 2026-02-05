#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: REINER JOHN SANTIAGO
# DATE CREATED: OCTOBER 7, 2025                                 
# REVISED DATE: 
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##
# Import python modules
import argparse

# TODO 1: Define get_input_args function below please be certain to replace None
#       in the return statement with parser.parse_args() parsed argument 
#       collection that you created with this function
def get_input_args():
    """
    Retrieves and parses the 3 command line arguments provided by the user when
    they run the program from a terminal window. This function uses Python's 
    argparse module to created and defined these 3 command line arguments. If 
    the user fails to provide some or all of the 3 arguments, then the default 
    values are used for the missing arguments. 
    Command Line Arguments:
      1. Image Folder as --dir with default value 'pet_images'
      2. CNN Model Architecture as --arch with default value 'vgg'
      3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
    This function returns these arguments as an ArgumentParser object.
    Parameters:
     None - simply using argparse module to create & store command line arguments
    Returns:
     parse_args() -data structure that stores the command line arguments object  
    """
    # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    
    # Create 3 command line arguments as mentioned above using add_argument() from ArgumentParser method
    # Argument 1: Image Folder
    parser.add_argument('--dir', 
                        type=str, 
                        default='pet_images/', 
                        help='path to the folder of pet images')
    
    # Argument 2: CNN Model Architecture
    parser.add_argument('--arch', 
                        type=str, 
                        default='vgg', 
                        help='CNN model architecture: resnet, alexnet, or vgg')
    
    # Argument 3: Text File with Dog Names
    parser.add_argument('--dogfile', 
                        type=str, 
                        default='dognames.txt', 
                        help='file that contains the list of valid dognames')
    
    # Replace None with parser.parse_args() parsed argument collection that 
    # create this function 
    return parser.parse_args()

# Main program function defined below
    # Function that checks command line arguments using in_arg  
def check_command_line_arguments(in_arg):
    """
    Simple function to check and display the command line arguments
    """
    print("\nTODO1 - Command Line Arguments Check:")
    print(f"   Image Directory: {in_arg.dir}")
    print(f"   CNN Model Architecture: {in_arg.arch}")
    print(f"   Dog Names File: {in_arg.dogfile}")
    print("TODO1 completed successfully!")

def main():
  # TODO 1: Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg

    print("Testing TODO 1 - Command Line Arguments...")
    in_arg = get_input_args()

# Function that checks command line arguments using in_arg  
    check_command_line_arguments(in_arg)

if __name__ == "__main__":
    main()

    