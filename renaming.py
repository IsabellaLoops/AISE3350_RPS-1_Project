import os

def rename_images_in_folder(folder_path):
    # List all files in the folder
    files = os.listdir(folder_path)
    
    # Filter only image files (common image extensions)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff']
    image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
    
    # Rename each image with the format paper#### (incremental)
    for index, filename in enumerate(image_files, start=1):
        # Extract file extension
        file_extension = os.path.splitext(filename)[1]
        
        # Create new filename with the desired format
        new_filename = f"scissors{index:04d}{file_extension}"
        
        # Get full paths for renaming
        old_file_path = os.path.join(folder_path, filename)
        new_file_path = os.path.join(folder_path, new_filename)
        
        # Rename the file
        os.rename(old_file_path, new_file_path)

# Specify the folder where your images are stored
folder_path = 'Data/scissorsRenamed'

# Run the function
rename_images_in_folder(folder_path)
