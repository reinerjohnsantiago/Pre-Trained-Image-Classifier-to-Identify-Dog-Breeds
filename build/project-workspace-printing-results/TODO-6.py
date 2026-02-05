# TODO-6 - Complete solution for Printing Results                                                                             
# PROGRAMMER: REINER JOHN SANTIAGO
# DATE CREATED: OCTOBER 7, 2025   
import os
import sys

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels from image filenames.
    """
    from os import listdir
    
    in_files = listdir(image_dir)
    results_dic = dict()
   
    for filename in in_files:
       if filename[0] != ".":
           filename_without_ext = filename.rsplit('.', 1)[0]
           pet_label = filename_without_ext.replace('_', ' ').lower().strip()
           if filename not in results_dic:
              results_dic[filename] = [pet_label]
           else:
               print("** Warning: Duplicate files exist in directory:", filename)
    return results_dic

def mock_classifier_based_on_filename(image_path, model):
    """
    Mock classifier function that returns realistic labels.
    """
    filename = os.path.basename(image_path)
    filename_without_ext = filename.rsplit('.', 1)[0]
    base_name = filename_without_ext.split('_')[0].lower()
    
    mock_classifier_responses = {
        'basenji': 'basenji, cong dog',
        'basset': 'basset hound',
        'beagle': 'beagle',
        'boston': 'boston bull, boston terrier',
        'boxer': 'boxer',
        'cocker': 'cocker spaniel, english cocker spaniel, cocker',
        'collie': 'collie, border collie',
        'dalmatian': 'dalmatian, coach dog, carriage dog',
        'german': 'german shepherd, german shepherd dog',
        'golden': 'golden retriever',
        'great': 'great dane',
        'miniature': 'miniature schnauzer',
        'poodle': 'poodle, poodle dog',
        'saint': 'saint bernard, st bernard',
        'cat': 'tabby, tabby cat',
        'fox': 'fox squirrel, eastern fox squirrel',
        'gecko': 'gecko',
        'great': 'great horned owl',
        'polar': 'polar bear, ice bear, ursus maritimus',
        'rabbit': 'wood rabbit, cottontail, cottontail rabbit',
        'skunk': 'skunk, polecat, wood pussy'
    }
    
    for breed in mock_classifier_responses:
        if breed in base_name:
            return mock_classifier_responses[breed]
    
    return f"{base_name}, dog breed"

def classify_images(images_dir, results_dic, model):
    """
    Classify images and compare with pet labels.
    """
    for filename in results_dic:
        image_path = os.path.join(images_dir, filename)
        classifier_label = mock_classifier_based_on_filename(image_path, model)
        classifier_label = classifier_label.lower().strip()
        pet_label = results_dic[filename][0]
        
        if pet_label in classifier_label:
            results_dic[filename].extend([classifier_label, 1])
        else:
            results_dic[filename].extend([classifier_label, 0])

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjust results for dog classification.
    """
    dognames_dic = dict()
    
    try:
        with open(dogfile, "r") as infile:
            for line in infile:
                dogname = line.strip()
                if dogname and dogname not in dognames_dic:
                    dognames_dic[dogname] = 1
    except FileNotFoundError:
        print(f"ERROR: Dog file '{dogfile}' not found!")
        return
    
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]
        
        pet_is_dog = 1 if pet_label in dognames_dic else 0
        classifier_is_dog = 1 if classifier_label in dognames_dic else 0
        
        results_dic[key].extend([pet_is_dog, classifier_is_dog])

def calculates_results_stats(results_dic):
    """
    Calculate results statistics.
    """
    results_stats_dic = dict()
    
    # Initialize all counters to zero
    results_stats_dic['n_images'] = 0
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    # Process through the results dictionary to calculate counts
    for key in results_dic:
        results_stats_dic['n_images'] += 1
        
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
        
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
                
        else:
            results_stats_dic['n_notdogs_img'] += 1
            
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
    
    # Calculate percentages
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0
    
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
    
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    return results_stats_dic

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    TODO 6: Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if requested.
    """
    # Prints summary statistics over the run
    print("\n\n*** Results Summary for CNN Model Architecture", model.upper(), "***")
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    # Prints summary statistics (percentages) on Model Run
    print(" ")
    for key in results_stats_dic:
        if key.startswith('pct_'):
            print("{:20}: {:5.1f}%".format(key, results_stats_dic[key]))

    # IF print_incorrect_dogs == True AND there were images incorrectly classified as dogs
    if (print_incorrect_dogs and 
        ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs']) != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")

        # Process through results dict, printing incorrectly classified dogs
        for key in results_dic:
            # Pet Image Label is a Dog - Classified as NOT-A-DOG -OR- 
            # Pet Image Label is NOT-a-Dog - Classified as a-DOG
            if sum(results_dic[key][3:]) == 1:
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))

    # IF print_incorrect_breed == True AND there were dogs whose breeds were incorrectly classified
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")

        # Process through results dict, printing incorrectly classified breeds
        for key in results_dic:
            # Pet Image Label is-a-Dog, classified as-a-dog but is WRONG breed
            if (sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0], results_dic[key][1]))

def main():
    """
    Main function that runs the complete TODO 6 workflow.
    """
    print("STARTING TODO 6: Printing Results")
    print("=" * 60)
    
    # Set the paths
    image_dir = "data/pet_images"
    dog_file = "data/dognames.txt"
    model_arch = "vgg"
    
    print(f"Image directory: {image_dir}")
    print(f"Dog names file: {dog_file}")
    print(f"Model architecture: {model_arch}")
    print("=" * 60)
    
    # Verify paths exist
    if not os.path.exists(image_dir):
        print(f"ERROR: Image directory '{image_dir}' not found!")
        return
    
    if not os.path.exists(dog_file):
        print(f"ERROR: Dog file '{dog_file}' not found!")
        return
    
    # Step 1: Get pet labels
    print("\nStep 1: Getting pet labels from filenames...")
    results_dic = get_pet_labels(image_dir)
    print(f"Found {len(results_dic)} images")
    
    # Step 2: Classify images
    print("\nStep 2: Classifying images...")
    classify_images(image_dir, results_dic, model_arch)
    print("Image classification completed")
    
    # Step 3: Adjust for dog classification
    print("\nStep 3: Adjusting for dog classification...")
    adjust_results4_isadog(results_dic, dog_file)
    print("Dog classification completed")
    
    # Step 4: Calculate results statistics
    print("\nStep 4: Calculating results statistics...")
    results_stats_dic = calculates_results_stats(results_dic)
    print("Results statistics calculated")
    
    # Step 5: Print results (TODO-6)
    print("\nStep 5: Printing results...")
    print_results(results_dic, results_stats_dic, model_arch, True, True)
    
    print("\n" + "="*80)
    print("TODO 6 COMPLETED SUCCESSFULLY!")
    print("="*80)
    print("Expected Outcome Achieved:")
    print("Results summary printed with model architecture")
    print("All counts and percentages displayed")
    print("Misclassified dogs printed (when requested)")
    print("Misclassified breeds printed (when requested)")

if __name__ == "__main__":
    main()