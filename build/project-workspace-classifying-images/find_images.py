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
import os

def find_pet_images():
    print("=" * 60)
    print("SEARCHING FOR PET_IMAGES DIRECTORY")
    print("=" * 60)
    
    current_dir = os.getcwd()
    print(f"Current working directory: {current_dir}")
    print("\nContents of current directory:")
    print("-" * 40)
    
    items = os.listdir('.')
    for item in items:
        full_path = os.path.join('.', item)
        if os.path.isdir(full_path):
            print(f"📁 {item}/")
            #check if this directory contains images
            try:
                sub_items = os.listdir(full_path)
                image_files = [f for f in sub_items if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
                if image_files:
                    print(f"   Found {len(image_files)} image files")
                    if len(image_files) <= 5:
                        for img in image_files[:5]:
                            print(f"   - {img}")
                    else:
                        print(f"   - {image_files[0]}")
                        print(f"   - {image_files[1]}")
                        print(f"   - ... and {len(image_files) - 2} more")
            except Exception as e:
                print(f"   Error reading: {e}")
        else:
            print(f"📄 {item}")
    
    print("\n" + "=" * 60)
    print("SEARCHING IN COMMON LOCATIONS:")
    print("-" * 40)
    
    #common locations
    common_paths = [
        '.',
        './pet_images',
        '../pet_images',
        '../../pet_images',
        '/workspace/cd0184/pet_images',
        '/workspace/pet_images',
        '/pet_images'
    ]
    
    for path in common_paths:
        if os.path.exists(path):
            print(f"✓ EXISTS: {path}")
            if os.path.isdir(path):
                try:
                    files = os.listdir(path)
                    image_count = len([f for f in files if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
                    if image_count > 0:
                        print(f"  → Contains {image_count} image files")
                    if image_count == 40:
                        print(f"  🎯 FOUND PET_IMAGES! → {path}")
                except:
                    pass
        else:
            print(f"✗ NOT FOUND: {path}")
    
    print("\n" + "=" * 60)
    print("SEARCHING RECURSIVELY FOR IMAGE FILES:")
    print("-" * 40)
    
    #search for image files
    image_extensions = ('.jpg', '.jpeg', '.png')
    found_dirs = set()
    
    for root, dirs, files in os.walk('.'):
        image_files = [f for f in files if f.lower().endswith(image_extensions)]
        if image_files:
            dir_name = os.path.basename(root)
            if 'pet' in dir_name.lower() or len(image_files) >= 10:
                print(f"📁 {root}/ → {len(image_files)} images")
                found_dirs.add(root)
                if len(image_files) >= 30:
                    print(f"LIKELY PET_IMAGES DIRECTORY!")
    
    if found_dirs:
        print(f"\nFound {len(found_dirs)} directories containing images")
    else:
        print("No directories with images found in current location")

if __name__ == "__main__":
    find_pet_images()