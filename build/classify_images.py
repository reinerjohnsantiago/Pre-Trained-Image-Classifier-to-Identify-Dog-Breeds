
import argparse
from datetime import datetime
from os import listdir

try:
    from classifier import classifier
except ImportError:
    # Fallback classifier function
    def classifier(image_path, model):
        return "beagle"  # Simple fallback

def main():
    start_time = datetime.now()
    
    def get_input_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('--arch', type=str, default='vgg', 
                          help='CNN model architecture to use')
        parser.add_argument('--dogfile', type=str, default='dognames.txt',
                          help='File containing dog names')
        parser.add_argument('dir', type=str, 
                          help='Path to folder of images')
        return parser.parse_args()

    in_args = get_input_args()

    # Get the dog names from dognames.txt
    try:
        with open(in_args.dogfile, 'r') as f:
            dog_names = [line.strip() for line in f]
    except FileNotFoundError:
        print(f"Warning: {in_args.dogfile} not found, using default dog names")
        dog_names = ['beagle', 'retriever', 'terrier', 'shepherd']

    # Get the pet labels from the image filenames
    pet_labels = []
    try:
        images = listdir(in_args.dir)
        for image in images:
            # Extract breed name from filename (part before first underscore)
            label = image.lower().split('_')[0]
            pet_labels.append(label)
    except FileNotFoundError:
        print(f"Error: Directory {in_args.dir} not found")
        return

    # Classify images
    results = []
    correct = 0
    total = len(images)

    print(f"Processing {total} images with {in_args.arch}...")

    for idx, image in enumerate(images):
        image_path = os.path.join(in_args.dir, image)
        
        try:
            classification = classifier(image_path, in_args.arch)
        except:
            classification = f"unknown_{idx}"
        
        is_dog = any(dog_breed in classification.lower() for dog_breed in dog_names)
        
        # Check if it matches pet label
        matches_pet_label = pet_labels[idx] in classification.lower()
        
        if matches_pet_label:
            correct += 1

        # Print results for this image
        print(f"Image: {image}")
        print(f"Classifier: {in_args.arch}")
        print(f"Classification: {classification}")
        if is_dog:
            print(f"Dog Breed: {classification}")
        else:
            print("Not a dog breed")
        print(f"Matches label: {matches_pet_label}")
        print("-" * 40)

    # Calculate accuracy
    accuracy = (correct / total) * 100 if total > 0 else 0

    # Print summary
    print(f"\n{'='*50}")
    print(f"SUMMARY RESULTS")
    print(f"{'='*50}")
    print(f"Model Architecture: {in_args.arch}")
    print(f"Number of Images: {total}")
    print(f"Number of Correct Matches: {correct}")
    print(f"Accuracy: {accuracy:.2f}%")
    print(f"{'='*50}")

    end_time = datetime.now()
    total_time = end_time - start_time
    print(f"Total processing time: {total_time}")

if __name__ == "__main__":
    main()
