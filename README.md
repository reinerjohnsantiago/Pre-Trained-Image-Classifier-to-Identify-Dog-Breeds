🐶 Dog Breed Classifier
A Python-based image classifier that identifies dog breeds using pre-trained deep learning models. Developed to assist with contestant registration for a citywide dog show by verifying submitted images are actual dogs and classifying their breeds.

📋 Table of Contents
Overview
Features
Technologies
Installation
Usage
Project Structure
Results & Performance
Acknowledgements
Contact
License

🎯 Overview
This project addresses the challenge of validating dog show registrations by:

Verifying dog images - Identifying whether submitted images contain dogs

Classifying breeds - Determining the specific breed for confirmed dog images

Model comparison - Evaluating performance across multiple CNN architectures

Efficiency analysis - Balancing accuracy with computational requirements

Objectives
✅ Distinguish between dog and non-dog images
✅ Accurately classify dog breeds
✅ Compare ResNet, AlexNet, and VGG model performance
✅ Analyze time-performance trade-offs

✨ Features
Multi-Model Support: Three CNN architectures for comparison:
ResNet - Deep residual networks
AlexNet - Classic CNN architecture
VGG - Very deep convolutional networks
Batch Processing: Classify multiple images efficiently
Custom Image Support: Upload and classify your own images
Performance Metrics: Detailed accuracy and timing reports

🛠️ Technologies
Python 3.x - Primary programming language
PyTorch - Deep learning framework
ImageNet Pre-trained Models - Leveraging transfer learning
Convolutional Neural Networks (CNNs) - For image feature extraction and classification

📥 Installation
Prerequisites
Python 3.6 or higher
pip package manager

Setup
Clone the repository:
bash
git clone https://github.com/yourusername/dog-breed-classifier.git
cd dog-breed-classifier
Install required dependencies (create a requirements.txt if available):

bash
pip install torch torchvision pillow
Ensure workspace structure:

text
workspace/
├── pet_images/           # Sample images for testing
├── uploaded_images/      # User-uploaded images
├── check_images.py       # Main classification script
└── run_models_batch_uploaded.sh  # Batch processing script

🚀 Usage
Basic Classification
Run the classifier on sample images:

bash
python check_images.py
Batch Processing with All Models
Classify uploaded images using all three architectures:

bash
cd uploaded_images
sh run_models_batch_uploaded.sh
Preparing Your Own Images
For best results, ensure images are:

In JPG format with .jpg extension

Approximately square (similar height and width)

Clearly visible subject

Required Test Images:
Dog image - Named Dog_01.jpg

Non-dog animal - Named Animal_Name_01.jpg (e.g., Black_bear_01.jpg)

Non-animal object - Named Object_Name_01.jpg (e.g., Coffee_mug_01.jpg)

Modified dog image - Create Dog_02.jpg by horizontally flipping Dog_01.jpg

📁 Project Structure
text
.
├── check_images.py              # Main classification script
├── run_models_batch_uploaded.sh # Batch processing script
├── pet_images/                  # Provided test images
├── uploaded_images/             # User image uploads
├── results/                     # Classification outputs
│   ├── resnet_pet-images.txt
│   ├── alexnet_pet-images.txt
│   └── vgg_pet-images.txt
└── hints/                       # Guidance documentation
📊 Results & Performance
The project evaluates three CNN models based on:

Classification accuracy for dog vs. non-dog images

Breed identification precision

Processing time and computational efficiency

Resource requirements

🙏 Acknowledgements
Udacity - For providing the foundational curriculum and project structure

Open Source Community - For the pre-trained models and tools that made this project possible

📞 Contact
Reiner John Santiago
LinkedIn Profile
Feel free to reach out for questions, collaborations, or feedback!

📄 License
This project is open source and available under the Udacity License.
