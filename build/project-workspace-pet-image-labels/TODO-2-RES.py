#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# PROGRAMMER: REINER JOHN SANTIAGO
# DATE CREATED: OCTOBER 7, 2025  
import argparse
from os import listdir

# TODO 1: get_input_args function
def get_input_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='data/pet_images/', help='path to pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='dog names file')
    return parser.parse_args()

# TODO 2: get_pet_labels function
def get_pet_labels(image_dir):
    filename_list = listdir(image_dir)
    results_dic = dict()
    
    for filename in filename_list:
        if not filename.startswith('.') and filename.lower().endswith(('.jpg', '.jpeg', '.png')):
            low_filename = filename.lower()
            word_list = low_filename.split('_')
            
            pet_name = ""
            for word in word_list:
                if '.' in word:
                    word = word.split('.')[0]
                if word.isalpha():
                    pet_name += word + " "
            
            pet_label = pet_name.strip()
            if filename not in results_dic:
                results_dic[filename] = [pet_label]
    
    return results_dic

def check_command_line_arguments(in_arg):
    print("\nTODO1 - Command Line Arguments Check:")
    print(f"   Image Directory: {in_arg.dir}")
    print(f"   CNN Model Architecture: {in_arg.arch}")
    print(f"   Dog Names File: {in_arg.dogfile}")
    print("TODO1 completed successfully!")

def check_creating_pet_image_labels(results_dic):
    num_items = len(results_dic)
    print(f"\nTODO2 - Pet Image Labels Check:")
    print(f"   Number of items in dictionary: {num_items}")
    
    if num_items == 40:
        print("✓ Dictionary contains exactly 40 items")
    else:
        print(f"✗ Expected 40 items, but got {num_items}")
    
    print("\n   First 10 key-value pairs:")
    count = 0
    for key, value in results_dic.items():
        if count < 10:
            print(f"      {key}: {value}")
            count += 1
    
    #test cases based on actual filenames
    test_cases = {
        'Boston_terrier_02259.jpg': ['boston terrier'],
        'cat_01.jpg': ['cat'],
        'fox_squirrel_01.jpg': ['fox squirrel'],
        'great_horned_owl_02.jpg': ['great horned owl'],  #error? underscore between horned and owl
        'Beagle_01125.jpg': ['beagle'],
        'gecko_80.jpg': ['gecko'],
        'polar_bear_04.jpg': ['polar bear'],
        'skunk_029.jpg': ['skunk']
    }
    
    print("\n   Format verification:")
    all_correct = True
    for filename, expected_label in test_cases.items():
        if filename in results_dic:
            if results_dic[filename] == expected_label:
                print(f"   ✓ {filename} → {results_dic[filename]}")
            else:
                print(f"   ✗ {filename} → {results_dic[filename]} (expected {expected_label})")
                all_correct = False
        else:
            print(f"   ✗ {filename} not found in dictionary")
            all_correct = False
    
    #final verification
    print("\n" + "=" * 50)
    if num_items == 40 and all_correct:
        print("SUCCESS: TODO 2 COMPLETED!")
        print("Expected outcome achieved:")
        print("   - Dictionary with 40 key-value pairs")
        print("   - Key = pet image filename") 
        print("   - Value = List containing formatted pet image label")
        print("   - All labels properly formatted (lowercase, no numbers)")
    else:
        print("Some issues need attention")
        if num_items == 40:
            print("✓ But we have the correct number of items (40)")

def main():
    print("Starting Pet Image Classifier Program...")
    print("=" * 60)
    
    in_arg = get_input_args()
    check_command_line_arguments(in_arg)
    
    print("\n" + "=" * 60)
    print("TODO 2 - Creating Pet Image Labels...")
    results = get_pet_labels(in_arg.dir)
    check_creating_pet_image_labels(results)

if __name__ == "__main__":
    main()