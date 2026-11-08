import os
import zipfile

data_dir = "../data/soccernet_data/calibration"

for filename in os.listdir(data_dir):
    if filename.endswith(".zip"):
        zip_path = os.path.join(data_dir, filename)
        print(f"Extracting {filename}...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extracts contents into a folder named after the zip file (minus .zip)
            extract_path = os.path.join(data_dir, filename[:-4])
            zip_ref.extractall(extract_path)
        print(f"Finished extracting {filename}.")

print("All datasets extracted successfully.")