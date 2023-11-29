import zipfile

# Path to your zip file
zip_file_path = './data/tweets.zip'

# Directory where you want to extract the files
extract_to_directory = './data/'

# Create a ZipFile object
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    # Extract all the contents into the directory
    zip_ref.extractall(extract_to_directory)

