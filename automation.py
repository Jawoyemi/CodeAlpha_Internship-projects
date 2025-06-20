import os # Import necessary libraries
import shutil # For file operations

source_folder = r"C:\path\to\source\folder"  # Change this to your source folder path
destination_folder = r"C:\path\to\destination\folder"  # Change this to your destination folder path

# Create destination folder if it doesn't exist
os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(".jpg"):
        src_path = os.path.join(source_folder, filename)
        dst_path = os.path.join(destination_folder, filename)
        shutil.move(src_path, dst_path)
        print(f"Moved: {filename}")

print("All .jpg images have been moved.")