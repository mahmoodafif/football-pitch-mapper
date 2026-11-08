import os
from SoccerNet.Downloader import SoccerNetDownloader

# Define your data root directory
data_dir = "./soccernet_data"

# Check what files are available in the calibration task
calibration_path = os.path.join(data_dir, "calibration")
if os.path.exists(calibration_path):
    print("Calibration data folder found!")
    # List a few sample match directories
    matches = os.listdir(calibration_path)
    print(f"Sample matches available: {matches[:5]}")
else:
    print("Calibration folder not found. Double-check your download path.")