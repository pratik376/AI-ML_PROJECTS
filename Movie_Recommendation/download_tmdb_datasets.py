import os
from kaggle.api.kaggle_api_extended import KaggleApi

def download_tmdb_dataset():
    api = KaggleApi()
    api.authenticate()

    dataset = "tmdb/tmdb-movie-metadata"
    download_path = os.getcwd()  # download into current folder

    print(f"Downloading {dataset} into {download_path} ...")
    api.dataset_download_files(dataset, path=download_path, unzip=True)
    print("Download and extraction done.")

if __name__ == "__main__":
    download_tmdb_dataset()
