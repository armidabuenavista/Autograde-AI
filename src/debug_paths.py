# src/debug_paths.py
import os

# Get the current working directory (where the terminal is running from)
current_directory = os.getcwd()
print(f"Current Working Directory: {current_directory}")

# Check if the relative path we are using exists
relative_path = "../data/raw/test_car.jpg"
absolute_path = os.path.abspath(relative_path)
print(f"Looking for image at: {absolute_path}")

# Check if the path exists
if os.path.exists(absolute_path):
    print("✅ SUCCESS: The file exists!")
else:
    print("❌ PROBLEM: The file does not exist at that path.")
    
    # Let's see what IS in the data/raw directory
    data_raw_path = os.path.abspath("../data/raw")
    if os.path.exists(data_raw_path):
        print(f"\nContents of {data_raw_path}:")
        for file in os.listdir(data_raw_path):
            print(f"  - {file}")
    else:
        print(f"\nThe folder {data_raw_path} doesn't even exist.")