# PROGRAMMER: REINER JOHN SANTIAGO
# DATE CREATED: OCTOBER 7, 2025  
import os
import subprocess
from pathlib import Path

def create_dognames_file():
    """Create dognames.txt from the dog breeds in pet_images"""
    
    # Dog breeds extracted from your image
    dog_breeds = [
        "Basenji",
        "Basset_hound", 
        "Beagle",
        "Boston_terrier",
        "Boxer",
        "Cocker_spaniel",
        "Collie",
        "Dalmatian",
        "German_shepherd_dog",
        "German_shorthaired_pointer",
        "Golden_retriever",
        "Great_dane",
        "Great_pyrenees",
        "Miniature_schnauzer",
        "Poodle",
        "Saint_bernard"
    ]
    
    # Write to dognames.txt
    with open('dognames.txt', 'w') as f:
        for breed in dog_breeds:
            f.write(breed + '\n')
    
    print(f"✓ Created dognames.txt with {len(dog_breeds)} dog breeds")
    return dog_breeds

def setup_paths():
    """Set up the correct file paths"""
    
    # Base directory where data is located
    base_dir = "/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/data"
    
    # Your working directory
    work_dir = "/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/project-workspace-classify-uploaded-images"
    
    paths = {
        'base_dir': base_dir,
        'work_dir': work_dir,
        'uploaded_images': os.path.join(base_dir, 'uploaded_images'),
        'pet_images': os.path.join(base_dir, 'pet_images'),
        'check_images.py': os.path.join(work_dir, 'check_images.py'),
        'dognames.txt': os.path.join(work_dir, 'dognames.txt'),
        'output_dir': work_dir  # Save results to your working directory
    }
    
    return paths

def check_required_files(paths):
    """Check if all required files exist"""
    print("Checking required files...")
    
    required_files = {
        'check_images.py': paths['check_images.py'],
        'dognames.txt': paths['dognames.txt'],
        'uploaded_images': paths['uploaded_images']
    }
    
    all_exist = True
    for name, path in required_files.items():
        if os.path.exists(path):
            print(f"✓ {name}: {path}")
        else:
            print(f"✗ {name}: {path} - NOT FOUND")
            all_exist = False
    
    # Check uploaded images contents
    print(f"\nChecking uploaded images in {paths['uploaded_images']}:")
    if os.path.exists(paths['uploaded_images']):
        images = os.listdir(paths['uploaded_images'])
        for img in images:
            print(f"  - {img}")
    else:
        print("  No uploaded_images folder found")
        all_exist = False
    
    return all_exist

def run_classification(paths):
    """Run the classification with correct paths"""
    print("\n" + "="*60)
    print("RUNNING CLASSIFICATION")
    print("="*60)
    
    models = ['resnet', 'alexnet', 'vgg']
    
    for model in models:
        output_file = os.path.join(paths['output_dir'], f"{model}_uploaded-images.txt")
        
        print(f"\nRunning {model.upper()} classification...")
        print(f"Output will be saved to: {output_file}")
        
        cmd = [
            'python', paths['check_images.py'],
            '--arch', model,
            '--dogfile', paths['dognames.txt'],
            paths['uploaded_images']
        ]
        
        try:
            # Change to the directory where check_images.py is located
            original_dir = os.getcwd()
            os.chdir(paths['work_dir'])
            
            with open(output_file, 'w') as f:
                result = subprocess.run(cmd, stdout=f, stderr=subprocess.PIPE, text=True)
            
            os.chdir(original_dir)
            
            if result.returncode == 0:
                print(f"✓ {model.upper()} classification completed!")
                # Show sample output
                if os.path.exists(output_file):
                    with open(output_file, 'r') as f:
                        lines = f.readlines()[:5]
                        print("  Sample output:")
                        for line in lines:
                            if line.strip():
                                print(f"    {line.strip()}")
            else:
                print(f"✗ {model.upper()} classification failed: {result.stderr}")
                
        except Exception as e:
            print(f"✗ Error running {model.upper()}: {e}")
            os.chdir(original_dir)

def analyze_results(paths):
    """Run the analysis on the results"""
    print("\n" + "="*60)
    print("ANALYZING RESULTS")
    print("="*60)
    
    # Check if result files exist
    result_files = [
        os.path.join(paths['output_dir'], 'resnet_uploaded-images.txt'),
        os.path.join(paths['output_dir'], 'alexnet_uploaded-images.txt'),
        os.path.join(paths['output_dir'], 'vgg_uploaded-images.txt')
    ]
    
    all_exist = all(os.path.exists(f) for f in result_files)
    
    if all_exist:
        print("✓ All result files found!")
        
        # Try to run the analysis script
        analysis_script = os.path.join(paths['work_dir'], 'analyze_uploaded_results.py')
        if os.path.exists(analysis_script):
            print("Running analysis script...")
            try:
                # Change to working directory and run analysis
                original_dir = os.getcwd()
                os.chdir(paths['work_dir'])
                
                # Import and run the analysis
                from analyze_uploaded_results import analyze_uploaded_images
                analyze_uploaded_images()
                
                os.chdir(original_dir)
            except ImportError as e:
                print(f"Could not import analysis script: {e}")
                print("Make sure analyze_uploaded_results.py is in your working directory")
                os.chdir(original_dir)
        else:
            print("Analysis script not found. Creating a simple analysis...")
            create_simple_analysis(paths)
    else:
        print("✗ Some result files are missing:")
        for result_file in result_files:
            if os.path.exists(result_file):
                print(f"  ✓ {os.path.basename(result_file)}")
            else:
                print(f"  ✗ {os.path.basename(result_file)}")

def create_simple_analysis(paths):
    """Create a simple analysis if the main analysis script is missing"""
    print("\nCreating simple analysis...")
    
    result_files = {
        'resnet': os.path.join(paths['output_dir'], 'resnet_uploaded-images.txt'),
        'alexnet': os.path.join(paths['output_dir'], 'alexnet_uploaded-images.txt'),
        'vgg': os.path.join(paths['output_dir'], 'vgg_uploaded-images.txt')
    }
    
    analysis_output = []
    analysis_output.append("SIMPLE ANALYSIS OF UPLOADED IMAGES CLASSIFICATION")
    analysis_output.append("=" * 50)
    
    for model, file_path in result_files.items():
        if os.path.exists(file_path):
            analysis_output.append(f"\n{model.upper()} RESULTS:")
            with open(file_path, 'r') as f:
                lines = f.readlines()
                for line in lines[:10]:  # Show first 10 lines
                    if line.strip():
                        analysis_output.append(f"  {line.strip()}")
    
    # Write simple analysis to file
    with open('simple_analysis.txt', 'w') as f:
        f.write('\n'.join(analysis_output))
    
    print("✓ Simple analysis saved to simple_analysis.txt")

def main():
    """Main execution function"""
    print("=== COMPLETE UPLOADED IMAGES CLASSIFICATION SETUP ===\n")
    
    # Make sure we're in the working directory
    work_dir = "/workspace/cd0184/9664b117-d773-4799-b6a3-d4640ed70218/project-workspace-classify-uploaded-images"
    if os.getcwd() != work_dir:
        print(f"Changing to working directory: {work_dir}")
        os.chdir(work_dir)
    
    # Step 1: Create missing dognames.txt
    create_dognames_file()
    
    # Step 2: Set up paths
    paths = setup_paths()
    
    print(f"\nWorking directory: {paths['work_dir']}")
    print(f"Uploaded images: {paths['uploaded_images']}")
    
    # Step 3: Check files
    if not check_required_files(paths):
        print("\n✗ Some required files are missing.")
        return
    
    # Step 4: Run classification
    run_classification(paths)
    
    # Step 5: Analyze results
    analyze_results(paths)
    
    print("\n" + "="*60)
    print("PROCESS COMPLETE!")
    print("="*60)
    print(f"Check these files in {paths['work_dir']}:")
    print("- resnet_uploaded-images.txt")
    print("- alexnet_uploaded-images.txt") 
    print("- vgg_uploaded-images.txt")
    print("- uploaded_images_analysis.txt (or simple_analysis.txt)")

if __name__ == "__main__":
    main()