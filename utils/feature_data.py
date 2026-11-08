from SoccerNet.Downloader import SoccerNetDownloader

# Download calibration and feature data
downloader = SoccerNetDownloader(LocalDirectory="./soccernet_data")
downloader.downloadDataTask(task="calibration", split=["train", "valid", "test"])