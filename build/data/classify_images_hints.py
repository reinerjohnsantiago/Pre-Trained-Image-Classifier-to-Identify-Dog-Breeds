#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Creates list of files in directory
    in_files = listdir(image_dir)
    
    # Creates empty dictionary for the results
    results_dic = dict()
   
    # Processes through each file in the directory
    for idx in range(0, len(in_files), 1):
       
       # Skips file if starts with . (like .DS_Store of Mac OSX)
       if in_files[idx][0] != ".":
           
           # Creates temporary label variable to hold pet label name
           pet_label = ""

           # Process filename to extract pet label
           filename = in_files[idx]
           
           # Remove the file extension
           filename_without_ext = filename.rsplit('.', 1)[0]
           
           # Replace underscores with spaces and convert to lowercase
           pet_label = filename_without_ext.replace('_', ' ').lower()
           
           # Strip any leading/trailing whitespace
           pet_label = pet_label.strip()

           # If filename doesn't already exist in dictionary add it and its pet label
           if in_files[idx] not in results_dic:
              results_dic[in_files[idx]] = [pet_label]
              
           else:
               print("** Warning: Duplicate files exist in directory:", 
                     in_files[idx])
 
    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic


# Main program function defined below
def main():
    # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
    # Once the get_pet_labels function has been defined replace 'None' 
    # in the function call with in_arg.dir  Once you have done the replacements
    # your function call should look like this: 
    #             get_pet_labels(in_arg.dir)
    # This function creates the results dictionary that contains the results, 
    # this dictionary is returned from the function call as the variable results
    
    # For now, we'll use a test directory since in_arg is not defined
    # You'll need to replace this with actual argument parsing later
    test_image_dir = "pet_images"  # Replace with your actual image directory path
    results = get_pet_labels(test_image_dir)

    # Function that checks Pet Images in the results Dictionary using results    
    # Note: You'll need to define or import the check_creating_pet_image_labels function
    # For now, let's create a simple version for testing
    check_creating_pet_image_labels(results)

def check_creating_pet_image_labels(results):
    """
    Simple function to check the results of get_pet_labels function.
    This is a placeholder - you may need to replace this with the actual
    checking function from your project.
    """
    print("\n--- Checking Pet Image Labels ---")
    print(f"Number of images processed: {len(results)}")
    
    # Print first 10 items to verify the format
    print("\nFirst 10 items in results:")
    count = 0
    for filename, label_list in results.items():
        if count < 10:
            print(f"  {filename}: {label_list}")
            count += 1
        else:
            break
    
    # Check if dictionary has the correct structure
    if len(results) > 0:
        sample_key = list(results.keys())[0]
        sample_value = results[sample_key]
        if isinstance(sample_value, list) and len(sample_value) > 0:
            print(f"\nSample label format check: OK")
            print(f"  Key type: {type(sample_key)}")
            print(f"  Value type: {type(sample_value)}")
            print(f"  Label type: {type(sample_value[0])}")
        else:
            print(f"\nSample label format check: FAILED")
    else:
        print("\nNo images were processed. Check your image directory path.")

# Call to main function to run the program
if __name__ == "__main__":
    main()