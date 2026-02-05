# PROGRAMMER: REINER JOHN SANTIAGO
# DATE CREATED: OCTOBER 7, 2025  
import os
import subprocess
import sys

def fix_check_images():
    """Fix the syntax error in check_images.py"""
    
    check_images_path = 'check_images.py'
    fixed_path = 'check_images_fixed.py'
    
    # Read the original file
    with open(check_images_path, 'r') as f:
        lines = f.readlines()
    
    # Fix line 43 (index 42 in 0-based indexing)
    if len(lines) > 42:
        print(f"Original line 43: {lines[42].strip()}")
        # Fix the incomplete assignment
        lines[42] = "    start_time = datetime.now()\n"
        print(f"Fixed line 43: {lines[42].strip()}")
    
    # Write the fixed version
    with open(fixed_path, 'w') as f:
        f.writelines(lines)
    
    print(f"✓ Created fixed version: {fixed_path}")
    return fixed_path

def run_fixed_classification():
    """Run classification with the fixed script"""
    
    uploaded_images_path = "/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data/uploaded_images"
    
    models = ['resnet', 'alexnet', 'vgg']
    
    for model in models:
        output_file = f"{model}_uploaded-images.txt"
        print(f"\nRunning {model.upper()} classification...")
        
        cmd = [
            'python', 'check_images_fixed.py',
            '--arch', model,
            '--dogfile', 'dognames.txt',
            uploaded_images_path
        ]
        
        try:
            with open(output_file, 'w') as f:
                result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True)
            
            if result.returncode == 0:
                print(f"✓ {model.upper()} classification completed!")
                # Show sample output
                with open(output_file, 'r') as f:
                    lines = f.readlines()[:10]
                    print("  Sample output:")
                    for line in lines:
                        if line.strip():
                            print(f"    {line.strip()}")
            else:
                print(f"✗ {model.upper()} classification failed: {result.stderr}")
                
        except Exception as e:
            print(f"✗ Error running {model.upper()}: {e}")

def create_analysis_script():
    """Create the analysis script if it's missing"""
    
    analysis_script = """
import os
import re

def parse_results_file(filename):
    \"\"\"Parse the results file and extract classification information\"\"\"
    results = {}
    
    if not os.path.exists(filename):
        print(f"Warning: {filename} not found")
        return results
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract image classifications using regex
    images = re.findall(r'Image: (\\S+)\\s*Classifier: \\S+\\s*Classification: ([^\\n]+)', content)
    for image, classification in images:
        results[image] = {
            'classification': classification,
            'is_dog': 'dog' in classification.lower() or any(breed in classification.lower() for breed in ['beagle', 'retriever', 'terrier', 'shepherd'])
        }
    
    return results

def analyze_uploaded_images():
    \"\"\"Analyze the results from all three model architectures\"\"\"
    
    models = {
        'resnet': 'resnet_uploaded-images.txt',
        'alexnet': 'alexnet_uploaded-images.txt', 
        'vgg': 'vgg_uploaded-images.txt'
    }
    
    results = {}
    for model, filename in models.items():
        results[model] = parse_results_file(filename)
        print(f"{model.upper()}: Found {len(results[model])} image classifications")
    
    # Generate answers
    answers = []
    answers.append("UPLOADED IMAGES CLASSIFICATION ANALYSIS")
    answers.append("=" * 50)
    
    # Question 1: Compare dog breed classification for Dog_01.jpg across models
    answers.append("\\n1. Dog Breed Classification for Dog_01.jpg across Models:")
    dog01_classifications = {}
    for model in models:
        if 'Dog_01.jpg' in results[model]:
            classification = results[model]['Dog_01.jpg']['classification']
            dog01_classifications[model] = classification
            answers.append(f"   {model.upper()}: {classification}")
    
    same_classification = len(set(dog01_classifications.values())) == 1
    answers.append(f"   All models gave same classification: {same_classification}")
    
    # Question 2: Compare Dog_01.jpg vs Dog_02.jpg within each model
    answers.append("\\n2. Dog_01.jpg vs Dog_02.jpg Classification Consistency:")
    for model in models:
        classification_01 = results[model].get('Dog_01.jpg', {}).get('classification', 'Not found')
        classification_02 = results[model].get('Dog_02.jpg', {}).get('classification', 'Not found')
        consistent = classification_01 == classification_02
        answers.append(f"   {model.upper()}:")
        answers.append(f"     Dog_01.jpg: {classification_01}")
        answers.append(f"     Dog_02.jpg: {classification_02}")
        answers.append(f"     Consistent: {consistent}")
    
    # Question 3: Check non-dog classifications
    answers.append("\\n3. Non-Dog Image Classifications:")
    for model in models:
        answers.append(f"   {model.upper()}:")
        animal_class = results[model].get('Animal_01.jpg', {}).get('classification', 'Not found')
        object_class = results[model].get('Object_01.jpg', {}).get('classification', 'Not found')
        animal_is_dog = 'dog' in animal_class.lower()
        object_is_dog = 'dog' in object_class.lower()
        answers.append(f"     Animal_01.jpg: {animal_class} - Misclassified as dog: {animal_is_dog}")
        answers.append(f"     Object_01.jpg: {object_class} - Misclassified as dog: {object_is_dog}")
    
    # Question 4: Determine best model
    answers.append("\\n4. Best Model Architecture Selection:")
    answers.append("   Based on the results above, select the model that:")
    answers.append("   - Consistently classifies Dog_01.jpg and Dog_02.jpg the same")
    answers.append("   - Correctly identifies non-dog images as not dogs")
    answers.append("   - Provides reasonable breed classifications")
    
    # Write answers to file
    with open('uploaded_images_analysis.txt', 'w') as f:
        f.write('\\n'.join(answers))
    
    print('\\n'.join(answers))
    print("\\nAnalysis complete! Results saved to 'uploaded_images_analysis.txt'")

if __name__ == "__main__":
    analyze_uploaded_images()
"""
    
    with open('analyze_uploaded_results.py', 'w') as f:
        f.write(analysis_script)
    
    print("✓ Created analysis script: analyze_uploaded_results.py")

def main():
    """Main execution"""
    print("=== FIXING AND RUNNING CLASSIFICATION ===\\n")
    
    # Step 1: Fix the check_images.py syntax error
    fixed_script = fix_check_images()
    
    # Step 2: Run classification with fixed script
    run_fixed_classification()
    
    # Step 3: Create analysis script
    create_analysis_script()
    
    # Step 4: Run analysis
    print("\\n" + "="*50)
    print("RUNNING ANALYSIS")
    print("="*50)
    
    try:
        from analyze_uploaded_results import analyze_uploaded_images
        analyze_uploaded_images()
    except Exception as e:
        print(f"Error running analysis: {e}")

if __name__ == "__main__":
    main()