'''
    Storing all of the vocabs from text file & splitting them into training & validation set
'''

from pathlib import  Path
import os
import lzma
from tqdm import tqdm

DIRECTORY_PATH = './openwebtext/openwebtext'
TRAIN_PATH = "./train/output_T.txt"
VAL_PATH = "./validation/output_V.txt"

def read_files(path):
    """Function returning list of files."""
    path = Path(path)
    file = [file.name for file in path.iterdir() if file.suffix == ".xz" and file.is_file()]
    return file


files = read_files(DIRECTORY_PATH)
total_files = len(files)

size = int(total_files * 0.9)

train_files = files[:size]
val_files = files[size:]

vocab = set()

#training set
with open(TRAIN_PATH, "w", encoding="utf-8") as outfile:
    for file in tqdm(train_files, total=len(train_files)):
        file_path = os.path.join(DIRECTORY_PATH, file)
        with lzma.open(file_path, "rt", encoding="utf-8") as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

#validation set
with open(VAL_PATH, "w", encoding="utf-8") as outfile:
    for file in tqdm(val_files, total=len(val_files)):
        file_path = os.path.join(DIRECTORY_PATH, file)
        with lzma.open(file_path, "rt", encoding="utf-8") as infile:
            text = infile.read()
            outfile.write(text)
            characters = set(text)
            vocab.update(characters)

#store vocabs in txt file
with open('vocab.txt', "w", encoding="utf-8") as vfile:
    for char in vocab:
        vfile.write(char + '\n')