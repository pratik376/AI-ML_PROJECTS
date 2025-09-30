from kaggle.api.kaggle_api_extended import KaggleApi
import os

# Initialize Kaggle API
api = KaggleApi()
api.authenticate()

# Dataset name on Kaggle
dataset = "arashnic/book-recommendation-dataset"

# Download path: current folder (where this script is located)
download_path = os.getcwd()  # current working directory

# Download and unzip the dataset directly in the main folder
api.dataset_download_files(dataset, path=download_path, unzip=True)

print(f"Dataset downloaded and extracted to '{download_path}' successfully!")
