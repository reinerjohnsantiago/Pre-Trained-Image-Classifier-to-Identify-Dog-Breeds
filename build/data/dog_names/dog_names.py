# List of dog breeds from your pet_images folder
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

# Create dognames.txt file
with open('dognames.txt', 'w') as f:
    for breed in dog_breeds:
        f.write(breed + '\n')

print("Created dognames.txt with", len(dog_breeds), "dog breeds")