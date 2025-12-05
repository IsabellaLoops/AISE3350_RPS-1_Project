import os
import random
import shutil

def split_images(folder_path, train_folder, val_folder, test_folder, train_ratio=0.7, val_ratio=0.2, test_ratio=0.1):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only image files (common image extensions)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Shuffle the image files to ensure randomness in the split
    random.shuffle(image_files)
    
    # Calculate the number of files for each set
    total_files = len(image_files)
    train_count = int(total_files * train_ratio)
    val_count = int(total_files * val_ratio)
    test_count = total_files - train_count - val_count  # Remainder goes to the test set

    # Split the images into train, validation, and test sets
    train_images = image_files[:train_count]
    val_images = image_files[train_count:train_count + val_count]
    test_images = image_files[train_count + val_count:]
    
    # Create directories for train, validation, and test if they don't exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(val_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)
    
    # Move files to the corresponding folders
    def move_files(image_list, target_folder):
        for image in image_list:
            src_path = os.path.join(folder_path, image)
            dest_path = os.path.join(target_folder, image)
            shutil.move(src_path, dest_path)
            print(f"Moved: {image} -> {target_folder}")
    
    # Move the images to the corresponding folders
    move_files(train_images, train_folder)
    move_files(val_images, val_folder)
    move_files(test_images, test_folder)
    
    print(f"Split completed: {len(train_images)} for training, {len(val_images)} for validation, {len(test_images)} for testing")

# Specify the folder where your images are stored
folder_path = 'Data/scissorsRenamed'

# Specify the target folders for train, validation, and test
train_folder = 'Data/scissorsTrain'
val_folder = 'Data/scissorsVal'
test_folder = 'Data/scissorsTest'

# Run the function
split_images(folder_path, train_folder, val_folder, test_folder)
