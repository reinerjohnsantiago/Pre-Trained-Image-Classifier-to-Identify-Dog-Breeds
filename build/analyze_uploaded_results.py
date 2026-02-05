import os
import re

def parse_results_file(filename):
    """Parse the results file and extract classification information"""
    results = {}
    
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found")
        return results
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract image blocks
    image_blocks = re.split(r'-{40}', content)
    
    for block in image_blocks:
        # Extract image name
        image_match = re.search(r'Image:\s*(\S+)', block)
        if image_match:
            image_name = image_match.group(1)
            classification_match = re.search(r'Classification:\s*([^\n]+)', block)
            classification = classification_match.group(1) if classification_match else "Unknown"
            
            results[image_name] = {
                'classification': classification,
                'is_dog': 'Dog Breed:' in block
            }
    
    return results

def analyze_uploaded_images():
    """Analyze the results from all three model architectures"""
    
    models = {
        'resnet': 'resnet_uploaded-images.txt',
        'alexnet': 'alexnet_uploaded-images.txt', 
        'vgg': 'vgg_uploaded-images.txt'
    }
    
    # Check which result files exist
    existing_models = {}
    for model, filename in models.items():
        if os.path.exists(filename):
            existing_models[model] = filename
            print(f"✓ Found {filename}")
        else:
            print(f"✗ Missing {filename}")
    
    if not existing_models:
        print("No result files found. Please run classification first.")
        return
    
    results = {}
    for model, filename in existing_models.items():
        results[model] = parse_results_file(filename)
        print(f"{model.upper()}: Found {len(results[model])} image classifications")
    
    # Generate answers
    answers = []
    answers.append("UPLOADED IMAGES CLASSIFICATION ANALYSIS")
    answers.append("=" * 50)
    
    # Question 1: Compare dog breed classification for Dog_01.jpg across models
    answers.append("\n1. Dog Breed Classification for Dog_01.jpg across Models:")
    dog01_classifications = {}
    for model in existing_models:
        if 'Dog_01.jpg' in results[model]:
            classification = results[model]['Dog_01.jpg']['classification']
            dog01_classifications[model] = classification
            answers.append(f"   {model.upper()}: {classification}")
        else:
            answers.append(f"   {model.upper()}: Dog_01.jpg not found in results")
    
    if dog01_classifications:
        same_classification = len(set(dog01_classifications.values())) == 1
        answers.append(f"   All models gave same classification: {same_classification}")
        if not same_classification:
            answers.append("   Differences in Dog_01.jpg classifications across models")
    
    # Question 2: Compare Dog_01.jpg vs Dog_02.jpg within each model
    answers.append("\n2. Dog_01.jpg vs Dog_02.jpg Classification Consistency:")
    for model in existing_models:
        classification_01 = results[model].get('Dog_01.jpg', {}).get('classification', 'Not found')
        classification_02 = results[model].get('Dog_02.jpg', {}).get('classification', 'Not found')
        consistent = classification_01 == classification_02
        answers.append(f"   {model.upper()}:")
        answers.append(f"     Dog_01.jpg: {classification_01}")
        answers.append(f"     Dog_02.jpg: {classification_02}")
        answers.append(f"     Consistent: {consistent}")
    
    # Question 3: Check non-dog classifications
    answers.append("\n3. Non-Dog Image Classifications:")
    for model in existing_models:
        answers.append(f"   {model.upper()}:")
        animal_class = results[model].get('Animal_01.jpg', {}).get('classification', 'Not found')
        object_class = results[model].get('Object_01.jpg', {}).get('classification', 'Not found')
        animal_is_dog = results[model].get('Animal_01.jpg', {}).get('is_dog', False)
        object_is_dog = results[model].get('Object_01.jpg', {}).get('is_dog', False)
        answers.append(f"     Animal_01.jpg: {animal_class} - Misclassified as dog: {animal_is_dog}")
        answers.append(f"     Object_01.jpg: {object_class} - Misclassified as dog: {object_is_dog}")
    
    # Question 4: Determine best model
    answers.append("\n4. Best Model Architecture Selection:")
    answers.append("   Based on the results above:")
    answers.append("   - Look for consistent classification between Dog_01.jpg and Dog_02.jpg")
    answers.append("   - Check that Animal_01.jpg and Object_01.jpg are not classified as dogs")
    answers.append("   - Choose the model with the most accurate and consistent results")
    
    # Write answers to file
    with open('uploaded_images_analysis.txt', 'w') as f:
        f.write('\n'.join(answers))
    
    print('\n'.join(answers))
    print("\nAnalysis complete! Results saved to 'uploaded_images_analysis.txt'")

if __name__ == "__main__":
    analyze_uploaded_images()
