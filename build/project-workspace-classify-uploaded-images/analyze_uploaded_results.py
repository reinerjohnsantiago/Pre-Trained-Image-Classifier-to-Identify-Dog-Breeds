# analyze_uploaded_results.py
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
    
    # Extract image classifications using regex
    images = re.findall(r'Image:\s*(\S+)\s*Classifier:\s*\S+\s*Classification:\s*([^\n]+)', content)
    for image, classification in images:
        results[image] = {
            'classification': classification.strip(),
            'is_dog': 'dog' in classification.lower() or any(breed in classification.lower() for breed in ['beagle', 'retriever', 'terrier', 'shepherd', 'hound'])
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
    
    # Calculate scores for each model
    model_scores = {}
    for model in existing_models:
        score = 0
        
        # Check Dog_01 and Dog_02 consistency
        breed_01 = results[model].get('Dog_01.jpg', {}).get('classification')
        breed_02 = results[model].get('Dog_02.jpg', {}).get('classification')
        if breed_01 and breed_02 and breed_01 == breed_02:
            score += 1
        
        # Check non-dog classifications
        animal_is_dog = results[model].get('Animal_01.jpg', {}).get('is_dog', True)
        object_is_dog = results[model].get('Object_01.jpg', {}).get('is_dog', True)
        if not animal_is_dog:
            score += 1
        if not object_is_dog:
            score += 1
        
        model_scores[model] = score
    
    best_model = max(model_scores, key=model_scores.get) if model_scores else None
    best_score = model_scores.get(best_model, 0) if best_model else 0
    
    answers.append("   Model Performance Scores (out of 3):")
    for model, score in model_scores.items():
        answers.append(f"     {model.upper()}: {score}/3")
    
    if best_model:
        answers.append(f"   Selected Best Model: {best_model.upper()}")
        answers.append(f"   Reasoning: {best_model.upper()} achieved the highest score ({best_score}/3) based on:")
        answers.append("     - Consistent classification between Dog_01.jpg and Dog_02.jpg")
        answers.append("     - Correctly identifying non-dog images as not dogs")
    else:
        answers.append("   Could not determine best model - insufficient data")
    
    # Write answers to file
    with open('uploaded_images_analysis.txt', 'w') as f:
        f.write('\n'.join(answers))
    
    print('\n'.join(answers))
    print("\nAnalysis complete! Results saved to 'uploaded_images_analysis.txt'")

if __name__ == "__main__":
    analyze_uploaded_images()