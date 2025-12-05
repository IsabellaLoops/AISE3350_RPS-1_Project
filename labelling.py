import os

# Define the class names and their corresponding indices
class_mapping = {
    'rock': 0,
    'paper': 1,
    'scissors': 2
}

# Directory containing the images
image_dir = 'Data/val/scissors'  # Replace with the actual path to your images

# Loop over the image files in the directory
for filename in os.listdir(image_dir):
    # Only process image files with a .jpg or .png extension (you can adjust if needed)
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        # Get the class name from the first part of the filename (e.g., 'paper001.jpg' -> 'paper')
        class_name = filename[0:8] # 0:4 for rock, 0:5 for paper, 0:8 for scissors
        print(class_name)

        # Check if the class is valid (rock, paper, or scissors)
        if class_name in class_mapping:
            # Get the class ID based on the class name
            class_id = class_mapping[class_name]

            # Create the corresponding .txt file
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_file_path = os.path.join(image_dir, txt_filename)

            # Write the class ID to the .txt file (just the class ID as a single number)
            with open(txt_file_path, 'w') as f:
                f.write(str(class_id))

            print(f"Generated label for {filename}: {class_id}")
        else:
            print(f"Invalid class in filename {filename}. Skipping.")
