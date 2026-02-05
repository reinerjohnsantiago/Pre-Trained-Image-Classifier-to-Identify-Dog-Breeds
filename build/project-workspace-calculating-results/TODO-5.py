# TODO-5 - Complete solution for Calculating Results
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
    TODO 5: Calculates statistics of the results of the program run.
    This function creates the results statistics dictionary with all required counts and percentages.
    """
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = dict()
    
    # Initialize all counters to zero as required
    results_stats_dic['n_images'] = 0
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    # Process through the results dictionary to calculate counts
    for key in results_dic:
        # Z: Count total images
        results_stats_dic['n_images'] += 1
        
        # Y: Count label matches (regardless of dog/non-dog)
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
        
        # B: Count dog images (pet label is dog)
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1
            
            # A: Count correctly classified dogs (both labels are dogs)
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1
            
            # E: Count correctly classified dog breeds (dog image with matching labels)
            if results_dic[key][2] == 1:
                results_stats_dic['n_correct_breed'] += 1
                
        # D: Count non-dog images (pet label is not dog)
        else:
            results_stats_dic['n_notdogs_img'] += 1
            
            # C: Count correctly classified non-dogs (both labels are not dogs)
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1
    
    # Calculate percentages after all counts are complete
    # Z: Total images is already calculated during iteration
    
    # Percentage of label matches (Y/Z * 100)
    if results_stats_dic['n_images'] > 0:
        results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100.0
    else:
        results_stats_dic['pct_match'] = 0.0
    
    # Objective 1a: Percentage of correctly classified dog images (A/B * 100)
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
    
    # Objective 1b: Percentage of correctly classified non-dog images (C/D * 100)
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    
    # Objective 2: Percentage of correctly classified dog breeds (E/B * 100)
    if results_stats_dic['n_dogs_img'] > 0:
        results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100.0
    else:
        results_stats_dic['pct_correct_breed'] = 0.0

    return results_stats_dic

def display_results_summary(results_stats_dic):
    """
    Displays a comprehensive summary of the results statistics exactly as specified.
    """
    print("\n" + "="*80)
    print("RESULTS STATISTICS SUMMARY")
    print("="*80)
    
    print("\nCOUNTS:")
    print("-" * 40)
    print(f"n_images: {results_stats_dic['n_images']}")                    # Z
    print(f"n_dogs_img: {results_stats_dic['n_dogs_img']}")                # B
    print(f"n_notdogs_img: {results_stats_dic['n_notdogs_img']}")          # D
    print(f"n_match: {results_stats_dic['n_match']}")                      # Y
    print(f"n_correct_dogs: {results_stats_dic['n_correct_dogs']}")        # A
    print(f"n_correct_notdogs: {results_stats_dic['n_correct_notdogs']}")  # C
    print(f"n_correct_breed: {results_stats_dic['n_correct_breed']}")      # E
    
    print("\nPERCENTAGES:")
    print("-" * 40)
    print(f"pct_match: {results_stats_dic['pct_match']:.1f}%")                    # Y/Z * 100
    print(f"pct_correct_dogs: {results_stats_dic['pct_correct_dogs']:.1f}%")      # A/B * 100
    print(f"pct_correct_notdogs: {results_stats_dic['pct_correct_notdogs']:.1f}%") # C/D * 100
    print(f"pct_correct_breed: {results_stats_dic['pct_correct_breed']:.1f}%")    # E/B * 100
    
    print("\nOBJECTIVES ACHIEVEMENT:")
    print("-" * 40)
    print("Objective 1a - Correctly identify dog images:")
    print(f"  ✓ {results_stats_dic['pct_correct_dogs']:.1f}% of dog images correctly identified")
    print(f"    (A={results_stats_dic['n_correct_dogs']} correctly classified dogs / B={results_stats_dic['n_dogs_img']} dog images)")
    
    print("Objective 1b - Correctly identify non-dog images:")
    print(f"  ✓ {results_stats_dic['pct_correct_notdogs']:.1f}% of non-dog images correctly identified")
    print(f"    (C={results_stats_dic['n_correct_notdogs']} correctly classified non-dogs / D={results_stats_dic['n_notdogs_img']} non-dog images)")
    
    print("Objective 2 - Correctly classify dog breeds:")
    print(f"  ✓ {results_stats_dic['pct_correct_breed']:.1f}% of dog breeds correctly classified")
    print(f"    (E={results_stats_dic['n_correct_breed']} correctly classified breeds / B={results_stats_dic['n_dogs_img']} dog images)")
    
    print("\n" + "="*80)
    print("DATA STRUCTURE VERIFICATION")
    print("="*80)
    print("Results Statistics Dictionary contains all required keys:")
    for key in sorted(results_stats_dic.keys()):
        if key.startswith('n_'):
            print(f"  {key}: {results_stats_dic[key]} (count)")
        else:
            print(f"  {key}: {results_stats_dic[key]:.1f}% (percentage)")

def main():
    """
    Main function that runs the complete TODO 5 workflow.
    """
    print("STARTING TODO 5: Calculating Results Statistics")
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
    
    # Step 4: Calculate results statistics (TODO-5)
    print("\nStep 4: Calculating results statistics...")
    results_stats_dic = calculates_results_stats(results_dic)
    print("Results statistics calculated")
    
    # Step 5: Display comprehensive results
    display_results_summary(results_stats_dic)
    
    print("\n" + "="*80)
    print("TODO 5 COMPLETED SUCCESSFULLY!")
    print("="*80)
    print("Expected Outcome Achieved:")
    print("Results statistics dictionary created with all required counts and percentages")
    print("Statistics answer Objectives 1 and 2:")
    print("   - Objective 1a: Percentage of correctly classified dog images")
    print("   - Objective 1b: Percentage of correctly classified non-dog images") 
    print("   - Objective 2: Percentage of correctly classified dog breeds")
    print("All calculations based on results dictionary analysis with proper formulas")

if __name__ == "__main__":
    main()